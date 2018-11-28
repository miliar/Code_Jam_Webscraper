#include<cstdio>
int main()
{
	int t,t0=0;
	scanf("%d",&t);
	int tab[17];
	for(t0=1;t0<=t;t0++)
	{
		printf("Case #%d: ",t0);
		int a,temp;
		for(int i=1;i<=16;i++)tab[i]=0;
		a=temp=0;
		scanf("%d",&a);
		for(int i=1;i<=4;i++)
		{
			for(int j=0;j<4;j++)
			{
				scanf("%d",&temp);
				if(i==a)tab[temp]++;
			}
		}
		scanf("%d",&a);
		for(int i=1;i<=4;i++)
		{
			for(int j=0;j<4;j++)
			{
				scanf("%d",&temp);
				if(i==a)tab[temp]++;
			}
		}
		int cnt=0,num;
		for(int i=1;i<=16;i++)
			if(tab[i]==2){cnt++;num=i;}
		if(cnt==0)printf("Volunteer cheated!\n");
		if(cnt==1)printf("%d\n",num);
		if(cnt>1) printf("Bad magician!\n");
		
	}
	return 0;
}
