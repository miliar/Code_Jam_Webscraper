//Akshay Vats
//quasar

#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

int main()
{
	ll n, t;
	cin.tie(0);
	ios::sync_with_stdio(false);
	cin >> t;
	int cs = 1;
	while (t--) {
		cin >> n;
		ll arr[10] = { 0 };
		cout << "Case #"<<cs<<": ";
		cs++;
		
		if (n == 0)
			cout << "INSOMNIA\n";
		else
		{
			for (ll i = 1; ; ++i)
			{
				ll num = i*n;
				while (num)
				{
					arr[num % 10] = 1;
					num /= 10;
				}
				int flag = 1;
				for (int j = 0; j < 10; ++j)
				{
					if (!arr[j])
					{
						flag = 0;
						break;
					}
				}
				if (flag)
				{
					cout << (i*n) << "\n";
					break;
				}
			}
		}

	}
	return 0;
}