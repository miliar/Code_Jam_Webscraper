#include<iostream>
#include<cstdio>
#include<cstring>
using namespace std;
int test,a[16],x,y;
int main()
{
	scanf("%d",&test);
	for (int t=1;t<=test;t++)
	{
		memset(a,0,sizeof a);
		scanf("%d",&x);
		x--;
		for (int i=0;i<4;i++)
			for (int j=0;j<4;j++)
			{
				scanf("%d",&y);
				if (i==x) a[--y]++;
			}
		scanf("%d",&x);
		x--;
		for (int i=0;i<4;i++)
			for (int j=0;j<4;j++)
			{
				scanf("%d",&y);
				if (i==x) a[--y]++;
			}
		int ans=-1;
		for (int i=0;i<16;i++)
			if (a[i]==2)
			{
				if (ans==-1) ans=i+1;
				else ans=17;
			}
		printf("Case #%d: ",t);
		if (ans==-1) 
			puts("Volunteer cheated!");
		else
		if (ans==17)
			puts("Bad magician!");
		else
			printf("%d\n",ans);
	}
	return 0;
}