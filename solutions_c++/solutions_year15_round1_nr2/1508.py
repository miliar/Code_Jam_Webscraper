#include<bits/stdc++.h>
using namespace std;
#define ll long long int
int main()
{
	ll i, j, k, t, n, m, x, b;
	cin >> t;
	for (x = 1; x <= t;++x)
	{
		cin >> b >> n;
		ll a[100005];
		ll tmp = 1;
		for (i = 1; i <= b; ++i)
		{
			cin >> a[i];
			tmp = (tmp*a[i]) / __gcd(tmp, a[i]);
		}
		ll time[100005] = { 0 };
		vector<ll> ans;
		ll cnt = 0;
		for (i = 1; i <= tmp; ++i)
		{
			if (i == 1)
			{
				for (j = 1; j <= b && j <= n; ++j)
				{
					ans.push_back(j);
					time[j] = a[j];
					++cnt;
				}
			}
			else
			{
				for (j = 1; j <= b; ++j)
				{
					if (time[j] - 1 == 0)
					{
						ans.push_back(j);
						time[j] = a[j];
						++cnt;
					}
					else
						--time[j];
				}
			}
		}
		if (ans.size() >= n)
			cout << "Case #" << x << ": " << ans[n - 1] << endl;
		else
			cout << "Case #" << x << ": " << ans[(n-1)%cnt] << endl;
	}
	return 0;
}