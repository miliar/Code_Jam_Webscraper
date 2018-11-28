#include <functional>
#include <sstream>
#include <vector>
#include <algorithm>
#include <cstring>
#include <cstdlib>
#include <iostream>
#include <string>
#include <cassert>
#include <ctime>
#include <map>
#include <math.h>
#include <cstdio>
#include <set>
#include <deque>
#include <memory.h>
#include <queue>


using namespace std;

#pragma comment(linker, "/STACK:64000000")

typedef long long ll;

const int MAXK = -1;
const int MAXN = 1 << MAXK;
const int INF = (int)1e9;

int sqr(int x) {
	return x * x;
}

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	cout.precision(10);
	cout << fixed;
	cerr.precision(10);
	cerr << fixed;

	int tests;
	cin >> tests;
	for (int test = 1; test <= tests; test++) {
		cout << "Case #" << test << ": ";
		cerr << "Case #" << test << ": ";
		
		int n, s;
		cin >> n >> s;
		vector<int> x(n), y(n), z(n), vx(n), vy(n), vz(n);
		for (int i = 0; i < n; i++) {
			cin >> x[i] >> y[i] >> z[i] >> vx[i] >> vy[i] >> vz[i];
		}

		double l = 0, r = 2e3;
		for (int it = 0; it < 100; it++) {
			double m = (l + r) / 2.0;

			vector<char> can(n);
			can[0] = 1;
			while (1) {
				int v = -1;
				for (int i = 0; i < n; i++) if (can[i] == 1 && v == -1) v = i;
				if (v == -1) break;
				can[v] = 2;
				for (int i = 0; i < n; i++) {
					double dist = sqrt(sqr(x[v] - x[i]) + sqr(y[v] - y[i]) + sqr(z[v] - z[i]));
					if (dist <= m && can[i] == 0) {
						can[i] = 1;
					}
				}
			}
			if (can[1]) r = m;
			else l = m;
		}

		double ans = r;
		cout << ans << endl;
		cerr << ans << endl;
	}

	return 0;
}