#include <iostream>
#include <algorithm>
#include <cstdio>
#include <cstdlib>
#include <ctime>
#include <memory.h>
#include <cmath>
#include <string>
#include <cstring>
#include <queue>
#include <vector>
#include <set>
#include <deque>
#include <map>
#include <functional>
#include <numeric>
#include <sstream>
#include <complex>

typedef long double LD;
typedef long long LL;
typedef unsigned long long ULL;
typedef unsigned int uint;

#define PI 3.1415926535897932384626433832795
#define sqr(x) ((x)*(x))

using namespace std;

const double EPS = 1e-8;

int main() {
    freopen(".in", "r", stdin);
    freopen(".out", "w", stdout);
	
	int T;
	cin >> T;
	cout.precision(12);
	cout << fixed;
	for (int __it = 1; __it <= T; ++__it) {
		int n;

		double V, X;
		cin >> n >> V >> X;
		vector<double> r(n);
		vector<double> c(n);    

		int nn = 0;
		for (int i = 0; i < n; ++i) {
			cin >> r[nn] >> c[nn];
			bool f = 0;
			for (int j = 0; j < i; ++j) {
				if (fabs(c[nn] - c[j]) < EPS) {
					r[j] += r[nn];
					f = 1;
					break;
				}
			}
			if (!f)
				++nn;
		}
		n = nn;

		double ans = 1e300;
		for (int i = 0; i < n; ++i)
			if (fabs(c[i] - X) < EPS) {
				ans = min(ans, V / r[i]);
			}
		for (int i = 0; i < n; ++i) {
			for (int j = 0; j < n; ++j) if (fabs(c[i] - c[j]) > EPS) {
				double v1 = (X - c[j]) / (c[i] - c[j]) * V;
				double v2 = V - v1;
				if (v1 >= -EPS && v2 >= -EPS)
					ans = max(v1 / r[i], v2 / r[j]);
			}
		}
		if (ans > 1e100) {
			cout << "Case #" << __it << ": " << "IMPOSSIBLE" << endl;			
		} else
			cout << "Case #" << __it << ": " << ans << endl;			
	}
    
    return 0;
}
