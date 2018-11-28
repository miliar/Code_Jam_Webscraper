#include <bits/stdc++.h>
using namespace std;
#define debug(x) cout << #x << " = (" << x << ")\n"
typedef long long int ll;
int main(void)
{
	ios::sync_with_stdio(0);
	cout.tie(0); cin.tie(0);
	int caseno = 1;
	int t; cin >> t; while(t--)
	{
		set<int> s;
		ll n; cin >> n;
		bool ans = false;
		cout << "Case #" << caseno++ << ": ";
		for(ll i = 1; i <= ll(1e3); i++)
		{
			ll a = i * n;
			while(a != 0)
			{
				s.insert(a % 10);
				a /= 10;
			}
			if (s.size() == 10 && !ans)
			{
				cout << i * n << endl;
				ans = true;
			}
		}	
		if (!ans)
			cout << "INSOMNIA" << endl;
	}
	return (0);
}
