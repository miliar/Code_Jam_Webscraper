#define _CRT_SECURE_NO_WARNINGS
#include <string>
#include <vector>
#include <algorithm>
#include <numeric>
#include <set>
#include <map>
#include <queue>
#include <iostream>
#include <sstream>
#include <cstdio>
#include <cmath>
#include <ctime>
#include <cstring>
#include <cctype>
#include <cassert>
#define rep(i,n) for(int (i)=0;(i)<(int)(n);++(i))
#define rer(i,l,u) for(int (i)=(int)(l);(i)<=(int)(u);++(i))
#define reu(i,l,u) for(int (i)=(int)(l);(i)<(int)(u);++(i))
#if defined(_MSC_VER) || __cplusplus > 199711L
#define aut(r,v) auto r = (v)
#else
#define aut(r,v) typeof(v) r = (v)
#endif
#define each(it,o) for(aut(it, (o).begin()); it != (o).end(); ++ it)
#define all(o) (o).begin(), (o).end()
#define pb(x) push_back(x)
#define mp(x,y) make_pair((x),(y))
#define mset(m,v) memset(m,v,sizeof(m))
#define INF 0x3f3f3f3f
#define INFL 0x3f3f3f3f3f3f3f3fLL
using namespace std;
typedef vector<int> vi; typedef pair<int,int> pii; typedef vector<pair<int,int> > vpii;
typedef long long ll; typedef vector<long long> vl; typedef pair<long long,long long> pll; typedef vector<pair<long long,long long> > vpll;
typedef vector<string> vs; typedef long double ld;
template<typename T, typename U> inline void amin(T &x, U y) { if(y < x) x = y; }
template<typename T, typename U> inline void amax(T &x, U y) { if(x < y) x = y; }

template<int MOD>
struct ModInt {
	static const int Mod = MOD;
	unsigned x;
	ModInt(): x(0) { }
	ModInt(signed sig) { int sigt = sig % MOD; if(sigt < 0) sigt += MOD; x = sigt; }
	ModInt(signed long long sig) { int sigt = sig % MOD; if(sigt < 0) sigt += MOD; x = sigt; }
	int get() const { return (int)x; }
	
	ModInt &operator+=(ModInt that) { if((x += that.x) >= MOD) x -= MOD; return *this; }
	ModInt &operator-=(ModInt that) { if((x += MOD - that.x) >= MOD) x -= MOD; return *this; }
	ModInt &operator*=(ModInt that) { x = (unsigned long long)x * that.x % MOD; return *this; }
	
	ModInt operator+(ModInt that) const { return ModInt(*this) += that; }
	ModInt operator-(ModInt that) const { return ModInt(*this) -= that; }
	ModInt operator*(ModInt that) const { return ModInt(*this) *= that; }
};
typedef ModInt<1000000007> mint;

int M, N;
char Sbuf[1000][101];
const char *S[1000];
int len[1000];

int calcnodes(int subset) {
	int res = 0;
	const char *prev = "";
	rep(i, M) if(subset >> i & 1) {
		const char *s = S[i];
		int lcp = 0;
		while(prev[lcp] != 0 && s[lcp] != 0 && prev[lcp] == s[lcp])
			lcp ++;
		res += len[i] - lcp;
		prev = s;
	}
//	rep(i, M) if(subset >> i & 1) cerr << S[i] <<", "; cerr << ": "<< res << endl;
	return res;
}

struct CmpStr {
	bool operator()(const char *x, const char *y) const {
		return strcmp(x, y) < 0;
	}
};

mint dp[5][1<<8][81];

int main() {
	int T;
	scanf("%d", &T);
	rep(ii, T) {
		scanf("%d%d", &M, &N);
		rep(i, M) scanf("%s", Sbuf[i]);
		rep(i, M) S[i] = Sbuf[i];
		sort(S, S + M, CmpStr());
		rep(i, M) len[i] = strlen(S[i]);
		//small!!!
		mset(dp, 0);
		dp[0][(1<<M)-1][0] = 1;
		rep(i, N) rep(subset, 1<<M) rer(j, 0, M * 10) {
			mint x = dp[i][subset][j];
			if(x.get() == 0) continue;
			for(int s = subset; s > 0; (-- s) &= subset)
				dp[i+1][subset - s][j + calcnodes(s)] += x;
		}
		int maxnodes = -1;
		for(int j = M * 10; j >= 0; j --) if(dp[N][0][j].get() != 0) {
			maxnodes = j;
			break;
		}
		printf("Case #%d: %d %d\n", ii+1, maxnodes + N, dp[N][0][maxnodes].get());
	}
	return 0;
}
