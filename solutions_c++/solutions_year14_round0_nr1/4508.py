#include <cstdio>

using namespace std;

int cases, m, istwo, num, a1;
int nums[25];

int main()
{
	scanf("%d", &cases);
	for(int q=1; q<=cases; q++)
	{
		istwo=0;
		for(int i=1; i<=16; i++)
			nums[i]=0;
		scanf("%d", &a1);
		for(int i=1; i<=4; i++)
		{
			for(int j=1; j<=4; j++)
			{
				scanf("%d", &m);
				if(i==a1)
					nums[m]++;
			}
		}
		scanf("%d", &a1);
		for(int i=1; i<=4; i++)
		{
			for(int j=1; j<=4; j++)
			{
				scanf("%d", &m);
				if(i==a1)
					nums[m]++;
			}
		}
		for(int i=1; i<=16; i++)
		{
			if(nums[i]==2)
			{
				istwo++;
				num=i;
			}
		}	
		printf("Case #%d: ", q);
		if(istwo>1)
		{
			printf("Bad magician!\n");
		}	
		if(istwo==1)
		{
			printf("%d\n", num);
		}
		if(istwo==0)
		{
			printf("Volunteer cheated!\n");
		}
	}
}
