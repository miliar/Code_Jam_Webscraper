#include<iostream>
#include<cstdio>
#include<algorithm>
using namespace std;
int main()
{
	int T,i,t,j,a[5][5],b[5][5],r1,r2,count,l;
	scanf("%d",&T);
	for(t=1;t<=T;t++)
	{
		count=0;
		scanf("%d",&r1);
		for(i=1;i<=4;i++)
			for(j=1;j<=4;j++)
				scanf("%d",&a[i][j]);
		scanf("%d",&r2);
		for(i=1;i<=4;i++)
			for(j=1;j<=4;j++)
				scanf("%d",&b[i][j]);
		for(i=1;i<=4;i++)
			for(j=1;j<=4;j++)
				if(a[r1][i]==b[r2][j])
				{
					count++;
					l=a[r1][i];
				}
		if(count==1)
			printf("Case #%d: %d\n",t,l);
		if(count==0)
			printf("Case #%d: Volunteer cheated!\n",t);
		if(count>1)	
			printf("Case #%d: Bad magician!\n",t);		
	}
	return 0;
}