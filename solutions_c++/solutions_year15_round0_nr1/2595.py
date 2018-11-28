#include<bits/stdc++.h>
using namespace std;
#define ll long long int
int main()
{
	ll i, j, k, t, n, m, x;
	cin >> t;
	for (x = 1; x <= t; ++x)
	{
		cin >> k;
		string s;
		cin >> s;
		ll ans = 0;
		ll curr = 0;
		for (i = 0; i < s.length(); ++i)
		{
			if (s[i] != '0')
			{
				if (curr < i)
				{
					ans = ans + (i - curr);
					curr = i;
				}
				curr += s[i] - '0';
			}
		}
		cout << "Case #" << x << ": " << ans << endl;
	}
	return 0;
}