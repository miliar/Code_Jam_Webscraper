#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <math.h>

int main(void)
{
	freopen("A-small-attempt0.in", "r", stdin);
	freopen("out.txt", "w", stdout);
	int T;
	scanf("%d", &T);
	for (int nT = 1; nT <= T; ++nT)
	{
		int nS;
		char S[2000];
		scanf("%d %s", &nS, S);
		
		int ans = 0;
		int cnt = 0;
		for (int i = 0; i <= nS; ++i)
		{
			if (cnt < i)
			{
				if (ans < i - cnt)
					ans = i - cnt;
			}
			cnt  += S[i]-'0';
		}
		printf("Case #%d: %d\n", nT, ans);
	}
}