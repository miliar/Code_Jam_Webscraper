#include<iostream>
#include<string>
using namespace std;
int main()
{
	freopen("input.in", "r", stdin);
	freopen("output.txt", "w", stdout);
	int t;
	cin >> t;
	int k = 1;
	while (t--)
	{
		cout << "Case #" << k << ": ";
		k++;
		string s;
		cin >> s;
		int ans = 0;
		for (int i = s.length() - 1; i >= 0; i--)
		{
			if (ans % 2 == 0)
			{
				if (s[i] == '-')
				{
					ans++;
				}
			}
			else
			{
				if (s[i] == '+')
					ans++;
			}
		}
		cout << ans << endl;
	}
	return 0;
}