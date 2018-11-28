#include <stdio.h>

int num[5][5];

int main()
{
	int T;
	scanf("%d",&T);
	for (int tt = 1; tt <= T; tt++)
	{
		bool flag[17] = {};
		
		int a;
		scanf("%d",&a);
		for (int i = 0; i < 16; i++)
		{
			int tmp;
			scanf("%d",&tmp);
			if (i >= a * 4 - 4 && i < a * 4) flag[tmp] = true;
		}

		int ans = -1;

		scanf("%d",&a);
		for (int i = 0; i < 16; i++)
		{
			int tmp;
			scanf("%d",&tmp);
			if (i >= a * 4 - 4 && i < a * 4)
			{
				if (flag[tmp])
				{
					if (ans == -1) ans = tmp;
					else ans = -2;
				}
			}
		}

		if (ans == -1) printf("Case #%d: Volunteer cheated!\n", tt);
		else if (ans == -2) printf("Case #%d: Bad magician!\n", tt);
		else printf("Case #%d: %d\n", tt, ans);
	}
}