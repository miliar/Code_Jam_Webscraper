#include <iostream>

using namespace std;

int const Max = 10101;
long long s[Max];

int main()
{
	freopen("out.txt", "w", stdout);
	int T;
	cin >> T;
	for (int t = 1; t <= T; t++)
	{
		long long ans = 0;
		for (int i = 0; i < Max; i++)
			s[i] = 0;
		int n, x;
		cin >> n >> x;
		for (int i = 1; i <= n; i++)
		{
			int a;
			cin >> a;
			s[a]++;
		}
		int ind = x;
		while (true)
		{
			if (ind == 0)
				break;
			if (s[ind] > 0)
			{
				ans++;
				s[ind]--;
				for (int i = ind; i >= 1; i--)
					if (s[i] > 0 && ind + i <= x)
					{
						s[i]--;
						break;
					}
			}
			else
				ind--;
		}
		cout << "Case #" << t << ": " << ans << endl;
	}
	return 0;
}