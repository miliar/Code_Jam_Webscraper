#include <cstdio>
#include <cstring>
int main()
{
	int T;
	scanf("%d", &T);
	int tt = 1;
	while(T--)
	{
		int v1, v2;
		int num[17];
		int tmp;
		memset(num, 0, sizeof(num));
		scanf("%d", &v1);
		for(int i = 1 ; i <= 4 ; i++)
		{
			for(int j = 1 ; j <= 4 ; j++)
			{
				if(i == v1)
				{
					scanf("%d", &tmp);
					num[tmp]++;
				}
				else scanf("%*d");
			}
		}
		scanf("%d", &v2);
		for(int i = 1 ; i <= 4 ; i++)
		{
			for(int j = 1 ; j <= 4 ; j++)
			{
				if(i == v2)
				{
					scanf("%d", &tmp);
					num[tmp]++;
				}
				else scanf("%*d");
			}
		}
		int ans = -1;
		for(int i = 1 ; i <= 16 ; i++)
		{
			if(num[i] == 2)
			{
				if(ans != -1)
				{
					ans = 0;
					break;
				}
				ans = i;
			}
		}
		if(ans == 0) printf("Case #%d: Bad magician!\n", tt);
		else if(ans == -1) printf("Case #%d: Volunteer cheated!\n", tt);
		else printf("Case #%d: %d\n", tt, ans);
		tt++;
	}
}
