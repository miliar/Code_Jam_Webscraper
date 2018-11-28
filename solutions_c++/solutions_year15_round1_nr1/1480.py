#include<bits/stdc++.h>
using namespace std;
#define ll long long int
int main()
{
	ll i, j, k, t, n, m, x;
	cin >> t;
	for (x = 1; x <= t;++x)
	{
		ll a[100005], ans1 = 0, ans2 = 0;
		cin >> n;
		ll rate = 0;
		for (i = 0; i < n; ++i)
		{
			cin >> a[i];
			if (i != 0)
			{
				if (a[i] < a[i - 1])
					ans1 += a[i - 1] - a[i];
			}
			if (i != 0)
			{
				if (a[i] < a[i - 1])
					rate = max(rate, a[i - 1] - a[i]);
			}
		}
		for (i = 0; i < n - 1; ++i)
		{
			ans2 += min(rate, a[i]);
		}
		cout << "Case #" << x << ": " << ans1 << " " << ans2 << endl;
	}
	return 0;
}