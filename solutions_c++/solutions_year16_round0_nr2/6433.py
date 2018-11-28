#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<string>
#include<queue>
#include<algorithm>
#include<map>
#include<iomanip>
#include<set>

using namespace std;

int n;
char s[110];

int main()
{
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);

	int T, n;
	cin >> T;
	for (int t = 1;t <= T;t++)
	{
		cin >> s;
		
		int len = strlen(s);
		int ans = 0;
		for (int i = len - 1;i >= 0;i--)
		{
			if (s[i] == '-')
			{
				ans++;
				for (int j = 0;j <= i;j++)
				{
					if (s[j] == '-') s[j] = '+';
					else s[j] = '-';
				}
			}
		}
		
		printf("Case #%d: %d\n", t, ans);
	}
	return 0;
}