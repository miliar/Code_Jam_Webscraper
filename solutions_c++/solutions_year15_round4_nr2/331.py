#include <map>
#include <set>
#include <cstdio>
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

typedef long long lint;
#define pp(a,b) push_back(make_pair((a),(b)))
#define pb push_back
#define mp make_pair
#define buybuy {printf("-1\n");return 0;}

int next() {int x; cin >> x; return x;}
lint lnext() {lint x; cin >> x; return x;}
double dnext() {double x; cin >> x; return x;}
//template<typename T> outln(T x) {cout << x; cout << "\n";}
#define prt(a) cout << a << "\n";
#define prtn(a, n) for(int iiiiiiiiiii = 0; iiiiiiiiiii < n; iiiiiiiiiii++) cout << a[iiiiiiiiiii] << " "; cout << "\n;"
#define prtall(a) for (auto iiiiiiiiiii : a) cout << iiiiiiiiiii << " "; cout << "\n";

int main() {
	int tests = next();
	double eps = 1e-11;
	for (int test = 1; test <= tests; test++) {
		int n = next();
		double v = dnext();
		double x = dnext();
		
		double r[n];
		double c[n];
		for (int i = 0; i < n; i++) {
			r[i] = dnext();
			c[i] = dnext() - x;
		}

		bool ispos = false;
		bool isneg = false;
		for (int i = 0; i < n; i++) {
			ispos |= c[i] > -eps;
			isneg |= c[i] < eps;
		}

		if (!ispos || !isneg) {
			printf("Case #%d: IMPOSSIBLE\n", test);
			continue;
		}

		for (int i = 0; i < n; i++) c[i] *= r[i];

		for (int i = 0; i < n; i++)
			for (int j = 0; j < n - 1; j++)
				if (c[j] * r[j + 1] > c[j + 1] * r[j]) {
					swap(c[j], c[j + 1]);
					swap(r[j], r[j + 1]);
				}

		/*for (int i = 0; i < n; i++) {
			printf("%.5f %.5f\n", r[i], c[i]);
		}*/

		double ux[n + 1];
		double uy[n + 1];
		double dx[n + 1];
		double dy[n + 1];
		
		ux[0] = uy[0] = 0;
		for (int i = 0; i < n; i++) {
			ux[i + 1] = ux[i] + r[n - 1 - i];
			uy[i + 1] = uy[i] + c[n - 1 - i];
		}
		dx[0] = dy[0] = 0;
		for (int i = 0; i < n; i++) {
			dx[i + 1] = dx[i] + r[i];
			dy[i + 1] = dy[i] + c[i];
		}

		double L = 0;
		double R = ux[n];

		//printf("!! %.8f\n", R);

		while (R - L > eps) {
			double M = (L + R) / 2;

			int up = 0;
			while (up < n && ux[up + 1] < M) up++;
			int down = 0;
			while (down < n && dx[down + 1] < M) down++;

			double y1 = (uy[up] * (ux[up + 1] - M) + uy[up + 1] * (M - ux[up])) / (ux[up + 1] - ux[up]);
			double y2 = (dy[down] * (dx[down + 1] - M) + dy[down + 1] * (M - dx[down])) / (dx[down + 1] - dx[down]);

			if (y1 >= 0 && y2 <= 0) L = M; else R = M;
		}

		//printf("!! %.8f\n", R);

		printf("Case #%d: %.8f\n", test, v/R);


	}

}
