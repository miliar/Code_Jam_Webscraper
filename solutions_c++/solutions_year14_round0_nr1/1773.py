#include <iostream>
#include <stdio.h>
#include <string.h>

using namespace std;
const long long MOD = 1000000007;

int set[100];

int main()
{
	freopen("A-small-attempt0.in", "r", stdin);
	freopen("A-small-attempt0.out", "w", stdout);

	int T;
	scanf("%d", &T);
	
	for (int nt = 1; nt <= T; ++nt)
	{
		memset(set, 0, sizeof(set));
		int t, a;
		scanf("%d", &a);
		for (int i = 1; i <= 4; ++i)
			for (int j = 0; j < 4; ++j)
			{
				scanf("%d", &t);
				if (i == a)
					set[t] = 1;
			}

		scanf("%d", &a);
		int ans = -1;
		int dou = 0;
		for (int i = 1; i <= 4; ++i)
			for (int j = 0; j < 4; ++j)
			{
				scanf("%d", &t);
				if ((i == a) && (set[t] == 1))
				{
					if (ans >= 0)
						dou = 1;
					ans = t;
					
				}
			}
		if (dou == 1)
			printf("Case #%d: Bad magician!\n", nt);
		else if (ans < 0)
			printf("Case #%d: Volunteer cheated!\n", nt);
		else
			printf("Case #%d: %d\n", nt, ans);
	}
	return 0;
}