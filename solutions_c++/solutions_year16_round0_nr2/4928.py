#include <bits/stdc++.h>
using namespace std;

/*
*/

char s[105];

int main()
{
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	int T;
	scanf("%d", &T);
	for (int z = 1; z <= T; z++)
	{
		scanf("%s", s);
		int n = strlen(s);
		int cnt = 0;
		for (int i = n-1; i >= 0; i--)
		{
			if (cnt == 0 && s[i] == '-')
			{
				cnt++;
			}
			else if (cnt > 0 && s[i] != s[i+1])
			{
				cnt++;
			}
		}
		printf("Case #%d: %d\n", z, cnt);
	}
}