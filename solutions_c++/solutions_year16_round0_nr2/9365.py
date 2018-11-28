#include <iostream>
#include <cstdio>
#include <string>
#include <algorithm>

using namespace std;

int main()
{
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	int t; cin >> t;
	for (int tc = 1; tc <= t; tc++)
	{
		string s; cin >> s;

		int ans = 1;

		for (int i = 1; i < s.length(); i++)
		{
			if (s[i] != s[i - 1])
				ans++;
		}

		if (s.back() == '+')
			ans--;

		/*int nMinus = 0, tries = 0;
		for (int i = 0; i < s.length(); i++)
			if (s[i] == '-')
				nMinus++;


		int nPlus = 0;
		for (int i = s.length() - 1; i > 0 && s[i] == '+'; i--)
			nPlus++;

		s = s.substr(0, s.length() - nPlus);
 		
		while (s.length() != 0 && nMinus > 0)
		{
			tries++;
			int cnt = 0;
			for (int i = 0; i < s.length() && s[i] == '-'; i++)
				cnt++;

			if (cnt == 0)
			{
				for (int i = 0; i < s.length() && s[i] == '+'; i++)
				{
					s[i] = '-';
					nMinus++;
				}
				continue;
			}
			reverse(s.begin(), s.end());

			if (nMinus == 0)
				break;

			s = s.substr(0, s.length() - cnt);
			nMinus = 0;
			for (int i = 0; i < s.length(); i++)
			{
				if (s[i] == '-')
					nMinus++;
				s[i] = (s[i] == '-') ? '+' : '-';
			}
			
		}*/
		//cout << "Differnce in testcase " << tc << " is : " << ans - tries << '\n';
		cout << "Case #" << tc << ": " << ans << '\n';
	}
	return 0;
}