#include <cstdio>
#include <iostream>
#include <string>

using namespace std;

char buf[10000];

int solve(string s)
{
	int ans = 0;
	int sum = 0;

	for (int i = 0; i < s.size(); i++)
	{
		if (s[i] != '0')
		{
			ans = max(ans, i - sum);
			sum += s[i] - '0';
		}
	}

	return ans;
}

int main()
{
	int TC;

	scanf("%d\n", &TC);

	for (int tc = 1; tc <= TC; tc++)
	{
		int n;
		string s;
		scanf("%d %s", &n, buf);
		s = buf;
		printf("Case #%d: %d\n", tc, solve(s));
	}
}