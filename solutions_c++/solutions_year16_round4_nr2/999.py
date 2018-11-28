#include <iostream>
#include <string>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <vector>
#include <set>
#include <map>
#include <cstring>
#include <algorithm>
#include <queue>
#include <iomanip>
using namespace std;

int count_ones(int x)
{
	int cnt = 0;
	for (int j = 0; j < 30; j++)
	{
		if ((x >> j) & 1) cnt++;
	}
	return cnt;
}


double get_prob(vector <double> & p)
{
	int k = p.size();
	double ans = 0.00;
	for (int i = 0; i < (1 << k); i++)
	{
		
		if (count_ones(i) == k / 2)
		{
			double cur;

			for (int j = 0; j < k; j++)
			{
				if (j == 0) cur = ((i >> j) & 1) ? p[j] : 1 - p[j];
				else cur *= (((i >> j) & 1) ? p[j] : 1 - p[j]);
			}

			ans += cur;
		}
	}
	return ans;
}


int main()
{
#if !ONLINE_JUDGE
	freopen("input.in", "r", stdin);
	freopen("output.out", "w", stdout);
#endif

	ios_base::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);

	int t;
	cin >> t;

	for (int z = 1; z <= t; z++)
	{
		int n, k;
		cin >> n >> k;
		vector <double> p(n);
		for (int i = 0; i < n; i++) cin >> p[i];
		double ans = 0.00;

		for (int i = 0; i < (1 << n); i++)
		{
			if (count_ones(i) == k)
			{
				vector <double> p2;
				for (int j = 0; j < n;j++)
				{
					if ((i >> j) & 1) p2.push_back(p[j]);
				}
				double t1 = get_prob(p2);
				if (t1 > ans) ans = t1;
			}
		}

		cout << "Case #" << z << ": " << setprecision(7) << fixed << ans << endl;
	}


	return 0;
}