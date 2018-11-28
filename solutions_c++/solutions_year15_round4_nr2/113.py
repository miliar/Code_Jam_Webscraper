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
#include <functional>
#define rep(i,n) for(int (i)=0;(i)<(int)(n);++(i))
#define rer(i,l,u) for(int (i)=(int)(l);(i)<=(int)(u);++(i))
#define reu(i,l,u) for(int (i)=(int)(l);(i)<(int)(u);++(i))
#if defined(_MSC_VER) || __cplusplus > 199711L
#define aut(r,v) auto r = (v)
#else
#define aut(r,v) __typeof(v) r = (v)
#endif
#define each(it,o) for(aut(it, (o).begin()); it != (o).end(); ++ it)
#define all(o) (o).begin(), (o).end()
#define pb(x) push_back(x)
#define mp(x,y) make_pair((x),(y))
#define mset(m,v) memset(m,v,sizeof(m))
#define INF 0x3f3f3f3f
#define INFL 0x3f3f3f3f3f3f3f3fLL
using namespace std;
typedef vector<int> vi; typedef pair<int,int> pii; typedef vector<pair<int,int> > vpii; typedef long long ll;
template<typename T, typename U> inline void amin(T &x, U y) { if(y < x) x = y; }
template<typename T, typename U> inline void amax(T &x, U y) { if(x < y) x = y; }

int main() {
	int T;
	scanf("%d", &T);
	rep(ii, T) {
		cerr << "case " << ii+1 << "..." << endl;
		int N; double V, X;
		cin >> N >> V >> X;
		vector<double> R, C;
		double free = 0;
		int freen = 0;
		rep(i, N) {
			double r, c;
			cin >> r >> c;
			if(c == X) {
				free += r;
				++ freen;
			}else {
				R.push_back(r);
				C.push_back(c);
			}
		}
		double ans = 1e99;
		N -= freen;
		if(N <= 1) {
			ans = V / free;
		}else if(N == 2) {
			if(C[0] > C[1]) swap(C[0], C[1]), swap(R[0], R[1]);
			if((C[0] < X && C[1] < X) || (C[0] > X && C[1] > X)) {
			}else {
				double ratio = (X - C[0]) / (C[1] - X);
				ans = V / (1 + ratio) / min(R[0], R[1] / ratio);
			}
		}else {
			cerr <<"not small" << endl;
			abort();
		}
		printf("Case #%d: ", ii+1);
		if(ans >= 1e99)
			puts("IMPOSSIBLE");
		else
			printf("%.10f\n", ans);
	}
	return 0;
}
