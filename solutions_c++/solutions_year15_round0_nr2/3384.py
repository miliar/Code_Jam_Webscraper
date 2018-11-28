#include <iostream>
#include <vector>

using namespace std;

int f[1009];

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int t;
	cin >> t;
	for (int T = 0; T < t; ++T)
	{
		int d;
		cin >> d;
		vector<int> v(d);
		for (int i = 0; i < d; ++i)
			cin >> v[i];
		int bestans = 1000000;
		int imax = 0;
		for (int i = 0; i < (int)v.size(); ++i)
			if (v[i] > v[imax])
				imax = i;
		bestans = v[imax];
		for (int k = 1; k <= 1009; ++k)
		{
			int ans = 0;
			for (int i = 0; i < d; ++i)
				if (v[i] > k)
				{
					ans += (v[i] / k) + (bool)(v[i] % k) - 1;
				}
			ans += k;
			bestans = min(bestans, ans);
		}
		cout << "Case #" << T + 1 << ":" << ' ' << bestans << endl;
	}
}