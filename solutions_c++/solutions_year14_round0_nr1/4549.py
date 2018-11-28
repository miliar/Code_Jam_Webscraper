#include<cstdio>
#include<iostream>
#include<cstring>
#include<string>
using namespace std;
bool exist[17];
int main()
{
	//freopen("a.in","r",stdin);
	//freopen("a.out","w",stdout);
	int T,x,y,a,b,num,Case=0;
	scanf("%d",&T);
	while(T--)
	{
		scanf("%d",&x);
		memset(exist,0,sizeof(exist));
		for(int i=1;i<=4;i++)
			for(int j=1;j<=4;j++)
			{
				scanf("%d",&a);
				if(i==x)exist[a]=1;
			}
		scanf("%d",&y);
		int ans=0;
		for(int i=1;i<=4;i++)
			for(int j=1;j<=4;j++)
			{
				scanf("%d",&b);
				if(i==y && exist[b]){num=b;ans++;}
			}
		if(ans>0)
		{
			if(ans==1)printf("Case #%d: %d\n",++Case,num);
			else printf("Case #%d: Bad magician!\n",++Case);
		}
		else printf("Case #%d: Volunteer cheated!\n",++Case);
	}
	return 0;
}
