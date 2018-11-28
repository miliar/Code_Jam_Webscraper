#include <map>
#include <set>
#include <cmath>
#include <ctime>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <cctype>
#include <cstdio>
#include <vector>
#include <cassert>
#include <complex>
#include <cstdlib>
#include <cstring>
#include <fstream>
#include <iomanip>
#include <sstream>
#include <iostream>
#include <algorithm>
using namespace std;
#define int long long
#define double long double

const double eps = 1e-9;

#undef int
int main()
{
#define int long long
	int t; cin >> t;
	for (int tt = 1; tt <= t; tt++)
	{
		cerr << "Executing Case #" << tt << "\n";
		cout << "Case #" << tt << ": ";

		int n; cin >> n;
		if (n == 1)
		{
			double v, x, r, c;
			cin >> v >> x >> r >> c;
			double t = v / r;
			if (fabs(c - x) > eps) puts("IMPOSSIBLE");
			else printf("%.8Lf\n", t);
		}
		else if (n == 2)
		{
			double v, x, r1, c1, r2, c2;
			cin >> v >> x >> r1 >> c1 >> r2 >> c2;

			if (fabs(c1 - c2) < eps)
			{
				if (fabs(x - c1) >= eps) puts("IMPOSSIBLE");
				else printf("%.8Lf\n", v / (r1 + r2));
				continue;
			}

			if (c1 > c2)
				swap(c1, c2), swap(r1, r2);

			if (x < c1 or x > c2)
			{
				puts("IMPOSSIBLE");
				continue;
			}

			double t1 = (x - c1) / r2;
			double t2 = (c2 - x) / r1;
			printf("%.8Lf\n", max(t1, t2) * v / (c2 - c1));
		}
		else puts("LOLZ, NOT NOW");
	}
	return 0;
}