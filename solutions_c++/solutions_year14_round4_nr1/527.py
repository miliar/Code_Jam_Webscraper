#include <algorithm>
#include <iostream>
#include <cstring>
#include <cstdio>
using namespace std;
int t, n, x, s[1000];

int main()
{
	scanf("%d", &t);
	for (int tt = 1; tt <= t; tt++)
	{
		memset(s, 0, sizeof(s));
		scanf("%d%d", &n, &x);
		for (int i = 1; i <= n; i++)
		{
			int k;
			scanf("%d", &k);
			s[k]++;
		}
		int ans = 0;
		for (int i = x; i >= 1; i--){
			if (s[i])
			{
				int j = x - i;
				while (s[i])
				{
					while (j && s[j] == 0) j--;
					if (j == 0)
					{
						ans += s[i];
						s[i] = 0;
					}
					else
					{
						while (s[i] && s[j])
						{
							if (i == j && s[i] == 1)
							{
								j--;
								break;
							}
							s[i]--;
							s[j]--;
							ans++;
						}
					}
				}
			}
		}
		printf("Case #%d: %d\n", tt, ans);
	}
	return 0;
}
