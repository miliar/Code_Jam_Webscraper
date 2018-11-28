#pragma comment(linker,"/stack:256000000")

#include <cmath> 
#include <ctime> 
#include <iostream> 
#include <string> 
#include <vector> 
#include <algorithm> 
#include <set> 
#include <map> 
#include <cstring> 
#include <cstdlib> 
#include <queue> 
#include <cstdio> 
#include <cfloat>
#include <cassert>

using namespace std; 

#define REP(i, n) for (int (i) = 0; (i) < (n); (i)++) 
#define sz(v) (int)(v).size() 
#define all(v) (v).begin(), (v).end()

const int N = 1000100;

long long a[N];
long long pr[N];
int n;
long long total, best;

void F(int p, int q) {
	long long s1 = pr[p];
	if (s1 < 0) s1 = 0;
	long long s2 = pr[q] - pr[p];
	if (s2 < 0) s2 = 0;
	long long s3 = pr[n] - pr[q];
	if (s3 < 0) s3 = 0;
	best = max(best, total - max(max(s1, s2), s3));
}

void solve() {
	long long p, q, r, s;
	cin >> n >> p >> q >> r >> s;
	REP(i, n) a[i + 1] = (i * p + q) % r + s;
	pr[0] = 0;
	total = 0;
	for (int i = 1; i <= n; i++) {
		pr[i] = pr[i - 1] + a[i];
		total += a[i];
	}
	best = 0;
	for (int lf = 0; lf < n; lf++) {
		long long s1 = pr[lf];
		//can choose from [lf + 1, n]
		int L = lf, R = n + 1;
		while (L + 1 < R) {
			int M = (L + R) / 2;
			if (pr[M] - pr[lf] < pr[n] - pr[M]) {
				L = M;
			} else {
				R = M;
			}
		}
		assert(lf <= L && L <= n);
		if (lf == L) {
			assert(a[lf + 1] >= pr[n] - pr[lf + 1]);
			F(lf, lf + 1);
		} else {
			assert(L < n);
			F(lf, L);
			F(lf, L + 1);
		}
	}
	printf("%.20lf", (double)best / total);
}

int main() {
#ifdef LOCAL
	freopen("A-large.in", "r", stdin);
	freopen("A-lrg.out", "w", stdout);
#endif
	int T;
	cin >> T;
	for (int tst = 1; tst <= T; tst++) {
		cout << "Case #" << tst << ": ";
		solve();
		cout << endl;
	}
	return 0;
}