#include <bits/stdc++.h>

using namespace std;

char winner(char ch1, char ch2)
{
	if (ch2 < ch1)
		swap(ch1, ch2);
	if (ch1 == 'P' && ch2 == 'R')
		return 'P';
	if (ch1 == 'R' && ch2 == 'S')
		return 'R';
	if (ch1 == 'P' && ch2 == 'S')
		return 'S';
}

bool check(string s)
{
	// cout << s << endl;
	if (s.length() == 1)
		return true;
	for (int i = 0; i < s.length() / 2; i++)
		if (s[2 * i] == s[2 * i + 1])
			return false;
	string tmp = "";
	for (int i = 0; i < s.length() / 2; i++)
		tmp.push_back(winner(s[2 * i], s[2 * i + 1]));
	return check(tmp);
}

int t;

int main()
{
	cin >> t;
	for (int tt = 1; tt <= t; tt++)
	{
		cout << "Case #" << tt << ": ";
		int n, r, p, s, total;
		cin >> n >> r >> p >> s;
		total = (1 << n);
		string str = string(p, 'P') + string(r, 'R') + string(s, 'S');
		string minStr = string(total, 'Z');
		sort(str.begin(), str.end());
		bool found = false;
		do
		{
			// cout << endl;
			if (check(str))
			{
				minStr = min(minStr, str);
				found = true;
			}
		} while (next_permutation(str.begin(), str.end()));
		if (!found)
			cout << "IMPOSSIBLE" << endl;
		else
			cout << minStr << endl;
	}
	return 0;
}