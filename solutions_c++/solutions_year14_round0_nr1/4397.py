#include<iostream>
#include<cstdio>
#include<cstring>
using namespace std;
int hash[20],n;
int main()
{
	freopen("A-small-attempt3.in","r",stdin);
	freopen("out.txt","w",stdout);
	int t;
	scanf("%d",&t);
	for(int ca=1;ca<=t;ca++)
	{
		int pos=-1,tmp;
		memset(hash,0,sizeof hash);
		scanf("%d",&n);
		bool flag=true;
		if(n>4 || n<1)
			flag=false;
		for(int i=0;i<4;i++)
		{
			for(int j=0;j<4;j++)
			{
				scanf("%d",&tmp);
				if(tmp>16 || tmp<1)
					flag=false;
				if(i==n-1 && flag)
					hash[tmp]=1;
			}
		}
		scanf("%d",&n);
		if(n>4 || n<1)
			flag=false;
		for(int i=0;i<4;i++)
		{
			for(int j=0;j<4;j++)
			{
				scanf("%d",&tmp);
				if(tmp>16 || tmp<1)
					flag=false;
				if(i==n-1 && flag)
				{
					if(hash[tmp])
					{
						if(pos==-1)
							pos=tmp;
						else
							flag=false;
					}
				}
			}
		}
		if(pos==-1)
			printf("Case #%d: Volunteer cheated!\n",ca);
		else
		{
			if(flag)
				printf("Case #%d: %d\n",ca,pos);
			else
				printf("Case #%d: Bad magician!\n",ca);
		}
	}
	return 0;
}
