#include <iostream>
#include <cstdio>
#include <cstring>

using namespace std;

int solve()
{
	int smax;
	scanf("%d", &smax);
	int ans = 0;
	int num = 0;
	char s[1002];
	scanf("%s", &s);
	for (int i = 0; i <= smax; i++)
	{
		if (num < i)
		{
			ans += i - num;
			num = i;
		}
		num += int(s[i] - '0');
	}
	return ans;
}

int main()
{
	int t;
	scanf("%d", &t);
	for (int i = 0; i < t; i++)
	{
		printf("Case #%d: %d\n", i + 1, solve());
	}
}