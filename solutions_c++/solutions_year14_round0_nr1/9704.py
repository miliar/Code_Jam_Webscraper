#include <stdio.h>
#include <string.h>
#include <algorithm>
using namespace std;

int hash1[20],hash2[20];

int main()
{
	freopen("A-small-attempt1.in", "r", stdin);
	freopen("data.out", "w", stdout);
	int test;
	scanf("%d",&test);
	for(int item = 1; item <= test; item++)
	{
		memset(hash1,0,sizeof(hash1));
		memset(hash2,0,sizeof(hash2));

		int r1,r2,x;

		scanf("%d",&r1);
		for(int i = 1; i <= 4; i++)
		{
			if(i == r1)
			{
				for(int j = 1; j <= 4; j++)
				{
					scanf("%d",&x);
					hash1[x] = 1;
				}
			}
			else
			{
				for(int j = 1; j <= 4; j++)
					scanf("%d",&x);
			}
		}

		scanf("%d",&r2);
		for(int i = 1; i <= 4; i++)
		{
			if(i == r2)
			{
				for(int j = 1; j <= 4; j++)
				{
					scanf("%d",&x);
					hash2[x] = 1;
				}
			}
			else
			{
				for(int j = 1; j <= 4; j++)
					scanf("%d",&x);
			}
		}

		int ans = 0;
		int pos;

		for(int i = 1; i <= 16; i++)
		{
			if(hash1[i] && hash2[i])
			{
				pos = i;
				ans++;
			}
		}

		if(ans == 0)
			printf("Case #%d: Volunteer cheated!\n",item);
		else if(ans == 1)
			printf("Case #%d: %d\n",item,pos);
		else
			printf("Case #%d: Bad magician!\n",item);
	}
	return 0;
}
