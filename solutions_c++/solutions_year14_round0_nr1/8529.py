#include<cstdio>

int t, ans, ans1, ans2, used[23], used1[23], q, a[23][23];

int main()
{	
	freopen("a.in", "r", stdin);
	freopen("a.out", "w", stdout);
	scanf("%d", &t);
	for (int i = 0; i < t; i++)
	{
		scanf("%d", &ans1);
		ans1--;
		q = 0;
		for (int j = 0; j < 4; j++)
			for (int k = 0; k < 4; k++)
			{	
				scanf("%d", &a[j][k]);
				used[a[j][k]] = j;
			}
		scanf("%d", &ans2);
		ans2--;
		for (int j = 0; j < 4; j++)
			for (int k = 0; k < 4; k++)
			{	
				scanf("%d", &a[j][k]);
				used1[a[j][k]] = j;
			}
		for (int j = 1; j < 17; j++)
			if (used[j] == ans1 && used1[j] == ans2)
			{
				q++;
				ans = j;
			}	
	   	if (q == 0)
	   		printf("Case #%d: Volunteer cheated!\n", i + 1);
	   	else if (q > 1)
	   		printf("Case #%d: Bad magician!\n", i + 1);
	   	else
	   		printf("Case #%d: %d\n", i + 1, ans);
	 }
	 return 0;
}
