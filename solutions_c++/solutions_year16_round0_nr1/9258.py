#include <iostream>
#include <cstring>

using namespace std;

typedef long long ll;

int main()
{
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	ll t; cin >> t;
	for (ll tc = 1; tc <= t; tc++)
	{
		ll n; cin >> n;

		bool appeared[10], ok = false;
		memset(appeared, false, sizeof(appeared));
		

		for (ll times = 1; times <= 10000000; times++)
		{
			ll temp = n*times;

			while (temp > 0)
			{
				appeared[temp % 10] = true;
				temp /= 10;
			}

			ok = true;

			for (ll i = 0; i < 10; i++)
			{
				if (appeared[i] == false)
					ok = false;
			}
			if (ok)
			{
				cout << "Case #" << tc << ": " << n*times << '\n';
				break;
			}
		}

		if (!ok)
			cout << "Case #" << tc << ": " << "INSOMNIA\n";
	}
	return 0;
}