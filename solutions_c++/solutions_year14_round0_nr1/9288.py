#include<iostream>
#include<cstdio>
#include<cmath>
#include<algorithm>
using namespace std;
#define mod 1000000007
int a[5][5],b[5][5];
int main()
{
	/*freopen("d:\\A-small-attempt0.in","r",stdin);
	freopen("d:\\open.txt","w",stdout);*/
	int n;
	scanf("%d",&n);
	for(int i=1;i<=n;i++)
	{
		int fir,sec;
		scanf("%d",&fir);
		for(int j=0;j<4;j++)
		{
			for(int k=0;k<4;k++)
			{
				scanf("%d",&a[j][k]);
			}
		}
		scanf("%d",&sec);
		for(int j=0;j<4;j++)
		{
			for(int k=0;k<4;k++)
			{
				scanf("%d",&b[j][k]);
			}
		}
		int sum=0,tem;
		for(int j=0;j<4;j++)
		{
			for(int k=0;k<4;k++)
			{
				if(a[fir-1][j]==b[sec-1][k]) { tem=a[fir-1][j];sum++;break;}
			}
		}
		printf("Case #%d: ",i);
		if(sum==0)printf("Volunteer cheated!\n");
		else if(sum==1) printf("%d\n",tem);
		else if(sum>1) printf("Bad magician!\n");
	}
	return 0;
}
