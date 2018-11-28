#include <bits/stdc++.h>

using namespace std;

int flip(string& s, int n)
{
	if (n == 0)
		return 0;
	
	reverse(s.begin(), s.begin()+n);
	for (int i = 0; i < n; i++)
		s[i] = (s[i] == '+' ? '-' : '+');

	return 1;
}

int fm(string& s)
{
	for (int i = 0; i < s.size(); i++)
	{
		if (s[i] == '-')
			return i;
	}
	return -1;
}

int fp(string& s)
{
	for (int i = 0; i < s.size(); i++)
	{
		if (s[i] == '+')
			return i;
	}
	return s.size();
}

int main()
{
	ios::sync_with_stdio(false);
	int T, casecnt = 0;
	cin >> T;
	while(T--)
	{
		string s;
		int pos, ans = 0;
		cin >> s;
		while((pos = fm(s)) != -1)
		{
			ans += flip(s, pos);
			ans += flip(s, fp(s));
		}
		printf("Case #%d: %d\n", ++casecnt, ans);
	}
	return 0;
}
