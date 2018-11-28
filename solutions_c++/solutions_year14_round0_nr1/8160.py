#include<cstdio>
#include<cstdlib>
int T, x, y, a[4], b[4];
int d;
int map[17];
int main()
{
	scanf("%d", &T);
	for(int t = 1; t <= T; ++t)
	{
		for(int i = 1; i <= 16; ++i)
			map[i] = 0;
		scanf("%d", &x);
		for(int i = 1; i <= 4; ++i)
		{
			if(i == x)
				for(int j = 0; j < 4; ++j)
					scanf("%d", &a[j]);
			else
				for(int j = 0; j < 4; ++j)
					scanf("%d", &d);
		}
		scanf("%d", &y);
		for(int i = 1; i <= 4; ++i)
		{
			if(i == y)
				for(int j = 0; j < 4; ++j)
					scanf("%d", &b[j]);
			else
				for(int j = 0; j < 4; ++j)
					scanf("%d", &d);
		}
		for(int i = 0; i < 4; ++i)
		{
			map[a[i]]++;
			map[b[i]]++;
		}
		int card = 0;
		for(int i = 1; i <= 16; ++i)
		{
			if(map[i] == 2)
				if(card == 0)
					card = i;
				else
				{
					card = -1;
					break;
				}
		}
		printf("Case #%d: ", t);
		if(card == -1)
			printf("Bad magician!\n");
		else if(card == 0)
			printf("Volunteer cheated!\n");
		else
			printf("%d\n", card);
	}
}