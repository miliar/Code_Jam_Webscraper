#include<iostream>
#include<cstdio>
using namespace std;
int main()
{
	int t,a[5][5],b[5][5],c1,c2,x,f;
	scanf("%d",&t);
	int k=0;
	while(k<t)
	{
		k++;
		scanf("%d",&c1);
		for(int i=1;i<=4;i++)
			for(int j=1;j<=4;j++)
				scanf("%d",&a[i][j]);
		scanf("%d",&c2);
		for(int i=1;i<=4;i++)
			for(int j=1;j<=4;j++)
				scanf("%d",&b[i][j]);
		f=0;
		for(int j=1;j<=4;j++)
		{
			for(int i=1;i<=4;i++)
			{
				if(b[c2][i]-a[c1][j]==0)
				{
					x=a[c1][j];
					f++;
				}
			}
		}
		if(f==1)
			printf("Case #%d: %d\n",k,x);
		if(f==0)
			printf("Case #%d: Volunteer cheated!\n",k);
		if(f>1)
			printf("Case #%d: Bad magician!\n",k);
	}
	return 0;
}
