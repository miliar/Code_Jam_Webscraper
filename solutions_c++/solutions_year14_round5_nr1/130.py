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
#include <limits>
#include <iterator>
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

int A[1000000];
long long Asum[1000001];
int main() {
	int T;
	scanf("%d", &T);
	rep(ii, T) {
		int N, p, q, r, s;
		scanf("%d%d%d%d%d", &N, &p, &q, &r, &s);
		rep(i, N)
			A[i] = ((long long)i * p + q) % r + s;
		Asum[0] = 0;
		rep(i, N) Asum[i+1] = Asum[i] + A[i];
		long long total = Asum[N];
		long long l = 0, u = (long long)1e12 + 10;
		while(u - l > 0) {
			long long mid = (l + u) / 2;
			bool ok = false;
			for(int i = 0, j = 0; i < N; i ++) {
				while(j+1 <= N && Asum[j+1] - Asum[i] <= mid)
					j ++;
				if(Asum[j] - Asum[i] > mid) cerr << "Error!!!!!!" << endl;
				if(i < j) {
					long long x = max(Asum[i], total - Asum[j]);
					ok |= x <= mid;
				}
			}
			if(ok) u = mid; else l = mid+1;
		}
		double ansd = (total - u) * 1. / total;
		printf("Case #%d: %.10f\n", ii+1, ansd);
	}
    return 0;
}
