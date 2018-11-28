 //FUCK

#include<stdio.h>

int num[5]={1,4,9,121,484};

int main()
{
	freopen("c.in","r",stdin);
	freopen("c.out","w",stdout);
	int t;
	scanf("%d",&t);
	for(int tt=0;tt<t;tt++)
	{
		int a,b;
		scanf("%d %d",&a,&b);

		int count=0;
		for(int i=0;i<5;i++)
		{
			if(num[i]>=a && num[i]<=b)
			{
				count++;
			}
		}
		printf("Case #%d: %d\n",tt+1,count);
	}
}
