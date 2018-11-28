#include<iostream>
#include<stdio.h>
#include<stdlib.h>
#include<algorithm>
using namespace std;

int main()
{
	freopen("A-small-attempt1.in", "r", stdin);
	freopen("out.txt", "w", stdout);

	int T, m, a, ct, ans;
	scanf("%d", &T);
	for(int Case = 1; Case <= T; Case++)
	{
		ct = 0;
		bool hash[17] = {false};
		scanf("%d", &m);
		for(int i = 0; i < 4; i++)
		{
			for(int j = 0; j < 4; j++)
			{
				scanf("%d", &a);
				if(i + 1 == m)
				{
					hash[a] = true;
				}
			}
		}
		scanf("%d", &m);
		for(int i = 0; i < 4; i++)
		{
			for(int j = 0; j < 4; j++)
			{
				scanf("%d", &a);
				if(i + 1 == m)
				{
					if(hash[a] == true)
					{
						ans = a;
						ct++;
					}
				}
			}
		}
		printf("Case #%d: ", Case);
		if(ct == 1)
		{
			printf("%d\n", ans);
		}
		else if(ct == 0)
		{
			printf("Volunteer cheated!\n");
		}
		else
		{
			printf("Bad magician!\n");
		}
	}
	return 0;
}
