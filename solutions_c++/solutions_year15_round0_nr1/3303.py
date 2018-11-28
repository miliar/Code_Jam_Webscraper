#include<iostream>
#include<cstdio>
#include<cstring>
#include<algorithm>
using namespace std;
char s[1002];
int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	int T, t = 0, n;
	cin >> T;
	while (T--)
	{
		cin >> n;
		scanf("%s", s);
		int now = 0, ans = 0;
		for (int i = 0; i <= n; i++)
		{
			if (now < i) ans += i - now, now = i;
			now += s[i] - '0';
		}
		cout << "Case #" << ++t << ": ";
		cout << ans << endl;
	}
}