#include <iostream>
using namespace std;

int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);

	int cases;
	cin >> cases;
	for (int _case = 0; _case < cases; _case++)
	{
		string s;
		cin >> s;
		int k;
		cin >> k;

		int ans = 0;
		for (int i = 0; i <= s.length() - k; i++)
			if (s[i] == '-')
			{
				ans++;
				for (int j = i; j < i + k; j++)
					if (s[j] == '-')
						s[j] = '+';
					else if (s[j] == '+')
						s[j] = '-';
			}

		bool flag = true;
		for (int i = s.length() - k + 1; i < s.length(); i++)
			if (s[i] != '+')
			{
				flag = false;
				break;
			}

		cout << "Case #" << _case + 1 << ": ";
		if (!flag)
			cout << "IMPOSSIBLE" << endl;
		else
			cout << ans << endl;
	}
	return 0;
}