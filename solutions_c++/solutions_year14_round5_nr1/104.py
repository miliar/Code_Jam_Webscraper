#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
 
using namespace std;

typedef long long ll;
typedef unsigned long long ull;

#define FOR(i, a, b) for (auto i = (a); i < (b); i++)
#define FORD(i, a, b) for (auto i = (b)-1; i >= (a); i--)
#define FORE(it, x) for (auto it = (x).begin(); it != (x).end(); ++it)
#define ALL(x) (x).begin(), (x).end()

int main(void)
{
	int tn;
	cin >> tn;
	for (int ti = 1; ti <= tn; ti++) {
		int n;
		ll p, q, r, s;
		cin >> n >> p >> q >> r >> s;
		vector<ll> v(n), sums(n);
		for (int i = 0; i < n; i++) {
			v[i] = (i*p+q)%r+s;
		}
		sums[0] = v[0];
		for (int i = 1; i < n; i++) {
			sums[i] = sums[i-1] + v[i];
		}
		ll best = 0;
		auto f = [&](int a, int b) {
			ll x = 0, y = 0, z = 0;
			if (a > 0 && a < n) x = sums[a-1];
			if (b < n-1 && b >= 0) z = sums[n-1] - sums[b];
			y = sums[n-1] - x - z;
			ll mi = min(min(x+y, x+z), y+z);
			if (best < mi) best = mi;
		};
		int a = n, b = n;
		for (int i = 0; i < n; i++) {
			if (3*sums[i] > sums[n-1]) {
				a = i;
				break;
			}
		}
		for (int i = 0; i < n; i++) {
			if (3*sums[i] > 2*sums[n-1]) {
				b = i;
				break;
			}
		}
		for (int ax = a-2; ax <= a+2; ax++) {
			for (int bx = a-2; bx <= b+2; bx++) {
				f(ax, bx);
			}

		}
		cout << "Case #" << ti << ": " << setprecision(12) << (double)best/(double)sums[n-1] << endl << flush;
	}
	return 0;
}
