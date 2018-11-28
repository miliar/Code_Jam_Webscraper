#include<cstdio>
#include<vector>
#include<algorithm>

using namespace std;

int main()
{
	int t,f,s,p=1,x;
	scanf("%d",&t);
	while(t--)
	{
		int hash[20]={};
		scanf("%d",&f);
		for(int i=1;i<=4;i++)
		{
			for(int j=1;j<=4;j++)
			{
				scanf("%d",&x);
				if(i==f)
					hash[x]++;
			}
		}
		scanf("%d",&s);
		for(int i=1;i<=4;i++)
		{
			for(int j=1;j<=4;j++)
			{
				scanf("%d",&x);
				if(i==s)
					hash[x]++;
			}
		}
		int c=0,n=0;
		for(int i=1;i<=16;i++)
		{
			if(hash[i]==2)
			{
				c++;
				n=i;
			}
		}
		printf("Case #%d: ",p++);
		if(c==1)
			printf("%d\n",n);
		else if(c>1)
			printf("Bad magician!\n");
		else if(c==0)
			printf("Volunteer cheated!\n");
	}
	return 0;
}
