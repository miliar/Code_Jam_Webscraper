#include<cstdio>

int main()
{
	int t,s,j,n,i,k,flag,h;
	int a[17]={0};
	scanf("%d",&t);
	for(k=1;k<=t;k++)
	{
		flag=0;
		scanf("%d",&s);
		for(i=0;i<4;i++)
			for(j=0;j<4;j++)
			{
				scanf("%d",&n);
				if(i+1==s)
				{
					++a[n];
				}
			}
		scanf("%d",&s);
		for(i=0;i<4;i++)
			for(j=0;j<4;j++)
			{
				scanf("%d",&n);
				if(i+1==s)
				{
					++a[n];
				}
			}
		for(i=1;i<=16;i++)
		{
			if(a[i]==2)
			{
				if(flag==0)
				{				
					flag=1;
					h=i;
				}
				else
					flag=2;
			}
		}
		if(flag==0)
			printf("Case #%d: Volunteer cheated!\n",k);
		if(flag==2)
			printf("Case #%d: Bad magician!\n",k);
		if(flag==1)
			printf("Case #%d: %d\n",k,h);
		for(i=0;i<=16;i++)
			a[i]=0;
	}
	return 0;
}
