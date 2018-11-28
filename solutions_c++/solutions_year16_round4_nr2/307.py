#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <cstdio>
#include <vector>
#include <set>
#include <map>
#include <algorithm>
#include <cassert>
#include <utility>
#include <ctime>
#include <string>
#include <sstream>
#include <queue>
#include <cstring>
#include <functional>

using namespace std;
typedef long long ll;
typedef long double ld;
#define ZERO(x) memset((x), 0, sizeof(x))
#define NEGATE(x) memset((x), 255, sizeof(x))
#define mp make_pair
#define mt(a, b, c) mp(a, mp(b, c))

int main()
{
#ifdef XXX
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif

	int tests;
	cin >> tests;
	for (int q = 0; q < tests; q++)
	{

		int n, k;
		cin >> n >> k;
		vector<double> v(n);
		for (int i = 0; i < n; i++) cin >> v[i];
		
		sort(v.begin(), v.end());

		double ans = -1e9;

		for (int i = 0; i <= k; i++)
		{
			vector<double> g(k);
			for (int i = 0; i < k; i++) g[i] = 0;
			g[0] = 1;
			vector<double> r;
			for (int j = 0; j < i; j++)
			{
				r.push_back(v[j]);
			}
			int last = n - 1;
			while (r.size() < k)
				r.push_back(v[last--]);

			for (int i = 0; i < k; i++)
			{
				double vr = r[i];
				vector<double> d(k);
				for (int j = 0; j < k; j++) d[j] = 0;
				for (int j = 0; j < k; j++)
				{
					double add = 0;
					if (j)
					{
						add = vr * g[j - 1];
					}
					d[j] = (1.0 - vr) * g[j] + add;
				}
				g = d;
			}
			ans = max(ans, g[k / 2]);
		}

		printf("Case #%d: ", q + 1);
		printf("%.12lf\n", ans);
	}

	return 0;
}