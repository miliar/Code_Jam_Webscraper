#include <bits/stdc++.h>
#define REP(a,b) for(int a=0; a<(b); ++a)
#define FWD(a,b,c) for(int a=(b); a<(c); ++a)
#define FWDS(a,b,c,d) for(int a=(b); a<(c); a+=d)
#define BCK(a,b,c) for(int a=(b); a>(c); --a)
#define ALL(a) (a).begin(), (a).end()
#define SIZE(a) ((int)(a).size())
#define VAR(x) #x ": " << x << " "
#define popcount __builtin_popcount
#define popcountll __builtin_popcountll
#define gcd __gcd
#define x first
#define y second
#define st first
#define nd second
#define pb push_back

using namespace std;

template<typename T> ostream& operator<<(ostream &out, const vector<T> &v){ out << "{"; for(const T &a : v) out << a << ", "; out << "}"; return out; }
template<typename S, typename T> ostream& operator<<(ostream &out, const pair<S,T> &p){ out << "(" << p.st << ", " << p.nd << ")"; return out; }

typedef long long int64;
typedef pair<int, int> PII;
typedef long double dd;
typedef vector<int> VI;

const int dx[] = {0,0,-1,1}; //1,1,-1,1};
const int dy[] = {-1,1,0,0}; //1,-1,1,-1};

int N, K;
dd dp[210][210];
dd pi[210];

dd calc(){
	dp[0][0] = 1;
	FWD(i,0,K){
		FWD(y,0,i+2) dp[i+1][y] = 0;
		FWD(y,0,i+1){
			dp[i+1][y] += dp[i][y] * (1-pi[i]);
			dp[i+1][y+1] += dp[i][y] * pi[i];
		}
	}
	return dp[K][K/2];
}

dd inpi[210];
void solve(){
	scanf("%d %d", &N, &K);
	FWD(i,0,N) scanf("%Lf", &inpi[i]);
	sort(inpi, inpi+N);
	dd res = 0;
	FWD(i,0,K+1){
		FWD(j,0,K-i)
			pi[K-1-j] = inpi[N-1-j];
		res = max(res, calc());
		pi[i] = inpi[i];
	}
	printf("%.8Lf\n", res);
}

int main(){
	int zzz;
	scanf("%d", &zzz);
	FWD(zz,1,zzz+1){
		printf("Case #%d: ", zz);
		solve();
	}
	return 0;
}
