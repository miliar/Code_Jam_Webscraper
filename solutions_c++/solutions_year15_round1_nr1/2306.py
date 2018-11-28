/* Written By Manav Aggarwal */
#include <bits/stdc++.h>
using namespace std;
#define endl '\n'
#define ll long long
int main()
{	
	ios_base::sync_with_stdio(false); cin.tie(0);
	freopen("Mushroom-large.in", "r", stdin);
	freopen("Mushroom-Monster-out.out", "w", stdout);
	ll t, cases;
	cin >> t;
	cases = t;
	while(t--)
	{
		ll n, i, y = 0, z = 0, max_diff = 0;
		cin >> n;
		ll m[n];
		for(i = 0; i < n; i++)
		{
			cin >> m[i];
		}
		for(i = 1; i < n; i++)
		{
			if(m[i] < m[i-1])
			{
				y += m[i-1] - m[i];
			}
			max_diff = max(max_diff, m[i-1] - m[i]);
		}
		for(i = 0; i < n-1; i++)
		{
			if(m[i] < max_diff)
			{
				z += m[i];
			}
			else
			{
				z += max_diff;
			}
		}
		cout << "Case #" << cases - t << ": " << y << " " << z << endl;
	}
	return 0;
}
