#include <iostream>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <set>
#include <map>
#include <vector>
#include <string>
#include <cstring>

using namespace std;

int n, t, l;
long long ans;
string s;

long long num(int v)
{
	return (v * (long long)(v + 1)) / 2;
}

bool cons(char c)
{
	return !(c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u');
}

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	cin >> t;
	for (int q = 0; q < t; q++)
	{
		cin >> s >> n;
		ans = 0;
		int l = 0;
		int cnt = 0;
		int blocks = 0;
		for (int r = 0; r < s.length(); r++)
		{
			if (cons(s[r]))
			{
				cnt++;
			}
			else
			{
				cnt = 0;
			}
			if (cnt == n)
			{
				ans += num(r - l) - num(n - 2);
				l = r - n + 2;
				cnt--;
			}
		}
		ans += num(s.length() - l);
		printf("Case #%d: %lld\n", q + 1, num(s.length()) - ans + blocks);
	}
	return 0;
}