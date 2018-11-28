#include<cstdio>
#include<iostream>
#include<string>
#include<algorithm>
using namespace std;

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int t;
	cin >> t;
	for (int q = 0; q < t; q++)
	{
		string s;
		cin >> s;
		cout << "Case #" << (q + 1) << ": ";
		int n = (int)s.length();
		int pos = n - 1;
		int ans = 0;
		while (pos >= 0 && s[pos] == '+')
			pos--;
		pos++;
		while (pos > 0)
		{
			int i = 0;
			int f = 0;
			while (i < n && s[i] == '+')
			{
				s[i++] = '-';
				f = 1;
			}
			ans += f;
			reverse(s.begin(), s.begin() + pos);
			ans++;
			i = 0;
			while (i < pos)
			{
				if (s[i] == '-')
					s[i] = '+';
				else
					s[i] = '-';
				i++;
			}
			pos--;
			while (pos >= 0 && s[pos] == '+')
				pos--;
			pos++;
		}
		cout << ans << "\n";
	}
	return 0;
}