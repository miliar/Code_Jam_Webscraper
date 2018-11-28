#include<iostream>
#include<cstdio>
#include<fstream>
using namespace std;
int main()
{
	freopen("input","r",stdin);
	freopen("output","w",stdout);
	int t,a[4][4],b[4][4],outpt[4],n1,n2;
	scanf("%d",&t);
	for(int i=0;i<t;i++)
	{
		scanf("%d",&n1);
		for(int j=0;j<4;j++)
			for(int k=0;k<4;k++)
				scanf("%d",&a[j][k]);
		scanf("%d",&n2);
		for(int j=0;j<4;j++)
			for(int k=0;k<4;k++)
				scanf("%d",&b[j][k]);
		int ele1,cnt=0;
		for(int j=0;j<4;j++)
		{
			ele1=a[n1-1][j];
			for(int k=0;k<4;k++)
			{
				if(ele1==b[n2-1][k])
				{
					outpt[cnt++]=ele1;
				}
			}
		}
		if(cnt==1)
			printf("Case #%d: %d\n",(i+1),outpt[0]);
		else if(cnt>0)
			printf("Case #%d: Bad magician!\n",(i+1));
		else
			printf("Case #%d: Volunteer cheated!\n",(i+1));
	}
	return 0;
}