#include<cstdio>
char input[1002];
void test()
{
	int smax;
	scanf("%d %s",&smax,input);
	int peo=0;
	int ans=0;
	for(int i=0;i<=smax;i++)
	{
		int x=input[i]-'0';
		if(x>0)
		{
			if(peo>=i)
				peo+=x;
			else
			{
				ans+=i-peo;
				peo=i+x;
			}
		}
	}	
	printf("%d\n",ans);
}


int main()
{
	int t;
	scanf("%d",&t);
	for(int i=0;i<t;i++)
	{
		printf("Case #%d: ",i+1);
		test();
	}
}
