#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <vector>
#include <string>

using namespace std;

inline bool isVowel(char c)
{
	return c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u';
}

inline bool isConsonant(char c)
{
	return !isVowel(c);
}

int check(const string &s, int n)
{
	for (int i = 0; i < s.length() - n + 1; ++i)
	{
		int x = 0;
		for (; x < n; ++x)
			if (isVowel(s[i + x]))
				break;
		if (x == n)
			return 1;
	}
	return 0;
}

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int tt;
	cin >> tt;
	for (int t = 1; t <=  tt; ++t)
	{
		string s;
		int n;
		cin >> s >> n;
		int res = 0;
		for (int len = n; len <= s.length(); ++len)
		{
			for (int st = 0; st + len <= s.length(); ++st)
			{
				string ss = s.substr(st, len);
				res += check(ss, n);
			}
		}
		printf("Case #%i: %i\n", t, res);
	}
	return 0;
}

