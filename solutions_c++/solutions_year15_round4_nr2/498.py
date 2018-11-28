#include <iostream>
#include <math.h>
#include <string.h>
#include <string>
#include <cmath>
#include <stdio.h>
#include <vector>
#include <map>
#include <list>
#include <queue>
#include <functional>
#include <algorithm>
#include <bitset>
#include <set>
#include <stack>
#include <limits>
#include <sstream>
#include <ctime> 
#define endl '\n'
#pragma warning (disable : 4996)

using namespace std;

#define lli long long int
#define ull unsigned long long int
#define MP make_pair

const int N = (int)(5e2 + 20);
const int L = 20;
const lli M = 1000000007;
const double E = 1e-7;

double det(double x11, double x12, double x21, double x22) {
	return x11*x22 - x12*x21;
}

int main()
{
	ios_base::sync_with_stdio(0);
#ifdef FILE_IO
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif 
	int T;
	cin >> T;
	for (int qq = 0; qq < T; ++qq) {
		cout << "Case #" << (qq + 1) << ": ";
		
		int n;
		double v, x;
		cin >> n >> v >> x;
		if (n == 2) {
			double r1, r0, x0, x1;
			cin >> r0 >> x0 >> r1 >> x1;

			if (fabs(x0 - x1) > 1e-7) {
				double delta = det(1, 1, x0, x1);
				double delta1 = det(v, 1, v*x, x1);
				double delta2 = det(1, v, x0, v*x);
				double root1 = delta1 / delta;
				double root2 = delta2 / delta;
				if (root1 < -1e-7 || root2 < -1e-7 || (root1 + root2) < 1e-7 || (x - 1e-7 > max(x0, x1))) printf("IMPOSSIBLE");
				else {
					double ans = max(root1 / r0, root2 / r1);
					printf("%.12lf", ans);
				}

			} else {
				if (fabs(x - x1) > 1e-7) printf("IMPOSSIBLE");
				else printf("%.12lf", v / (r0 + r1));
			}
		} else {
			double r0, x0;
			cin >> r0 >> x0;
			if (fabs(x0 - x) > 1e-7) {
				printf("IMPOSSIBLE");
			} else {
				printf("%.12lf", v / r0);
			}
		}
		

		cout << endl;
	}
}
