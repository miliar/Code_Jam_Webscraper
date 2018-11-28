#include <iostream>
#include <vector>
#include <algorithm>
#include <cstdio>
#include <ctime>
#include <string>
using namespace std;

int n;
string s;

void solve()
{
	cin >> n >> s;
	int cnt=0,ans=0;
	for (int i = 0; i <= n; ++i)
	{
		if (cnt >= i)
			cnt += s[i]-'0';
		else
		{
			if (s[i] != '0')
			{
				ans += i-cnt;
				cnt = i+s[i]-'0';
			}
		}
	}
	printf("%d", ans);
}


int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	int tests;
	cin >> tests;
	for (int test = 1; test <= tests; ++test)
	{
		printf("Case #%d: ", test);
		solve();
		printf("\n");
	}
}