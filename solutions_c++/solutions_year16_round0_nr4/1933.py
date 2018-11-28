#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

ll myexp(ll x, ll n)
{
	ll res = 1;
	while (n > 0)
	{
		if (n&1)
		{
			res = res*x;
			n -= 1;
		}
		else
		{
			x = x*x;
			n /= 2;
		}
	}
	return res;
}

int main()
{
	ll t, T, k, c, kc, s, i;
	double res;
	cin >> T;
	for (t = 1; t <= T; ++t)
	{
		cin >> k >> c >> s;
		kc = myexp(k, c);
		res = (double)kc/(2*s);
		cout << "Case #" << t << ": ";
		for (i = 0; i < s; ++i)
		{
			cout << (ll)ceil(res) << " ";
			res += (kc/s);
		}
		cout << endl;
	}
	return 0;
}