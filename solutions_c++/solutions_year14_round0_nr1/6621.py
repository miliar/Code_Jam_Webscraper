#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<vector>
#include<map>
#include<queue>
#include<cstring>
#include<cmath>
using namespace std;


int main()
{
int T;
int a;
int m[17];
int tp[4];
freopen("magic.in","r",stdin);
freopen("magic.out","w",stdout);
scanf("%d",&T);
for(int t=1;t<=T;t++)
	{
	for(int i=0;i<17;i++)
		m[i]=0;
	scanf("%d",&a);
	for(int i=0;i<4;i++)
		{
		for(int j=0;j<4;j++)
			scanf("%d",&tp[j]);
		if(i+1==a)
			{
			for(int j=0;j<4;j++)
				{
				m[tp[j]]++;
				}
			}
		}
		scanf("%d",&a);
	for(int i=0;i<4;i++)
		{
		for(int j=0;j<4;j++)
			scanf("%d",&tp[j]);
		if(i+1==a)
			{
			for(int j=0;j<4;j++)
				{
				m[tp[j]]++;
				}
			}
		}
	int c=0;
	int ans=-1;
	for(int i=1;i<17;i++)
		{
		if(m[i]>1)
			{
			c++;
			ans=i;
			}
		}
	if(c==0)
		{
		printf("Case #%d: Volunteer cheated!\n",t);
		}
	else if(c!=1)
		{
		printf("Case #%d: Bad magician!\n",t);
		}
	else
		{
		printf("Case #%d: %d\n",t,ans);
		}
	}
return 0;
}
