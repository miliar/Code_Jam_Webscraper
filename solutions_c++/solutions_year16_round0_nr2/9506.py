#include <iostream>
#include <string>
#include <algorithm>

using namespace std;

bool good(string& s)
{
	for (auto& c : s)
		if (c == '-')
			return false;

	return true;
}

int main()
{
#ifndef ONLINE_JUDGE
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif

	int T;
	cin >> T;

	for (int i = 1; i <= T; i++)
	{
		string s;
		cin >> s;

		int cnt = 0;
		while (!good(s))
		{
			cnt++;

			if (s[0] == '+')
			{
				cnt++;
				for (auto& c : s)
				{
					if (c == '-') break;
					c = '-';
				}
			}

			auto firstMinus = s.rfind('-');

			reverse(s.begin(), s.begin() + firstMinus + 1);

			for (int i = 0; i <= firstMinus; i++)
				s[i] = (s[i] == '-' ? '+' : '-');
		}

		cout << "Case #" << i << ": " << cnt << endl;
	}
}