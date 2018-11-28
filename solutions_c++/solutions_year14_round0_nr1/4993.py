#include <iostream>
#include<cstdio>
using namespace std;
int arr[4][4];
int r[4],c[4];
int eq()
{ return (r[0]==c[0])+(r[1]==c[1])+(r[2]==c[2])+(r[3]==c[3]);}
int main() {
	int t,i,j,test,k,R1,R2;
	scanf("%d",&t);
	for(test=1;test<=t;test++)
	{
		scanf("%d",&R1);
		for(i=0;i<4;i++)
		{
			for(j=0;j<4;j++)
			scanf("%d",&arr[i][j]);
		}
		for(i=0;i<4;i++)r[i]=arr[R1-1][i];
		scanf("%d",&R2);
		for(i=0;i<4;i++)
		{
			for(j=0;j<4;j++)
			scanf("%d",&arr[i][j]);
		}
		for(i=0;i<4;i++)c[i]=arr[R2-1][i];
		if(eq()>1)
		{
			printf("Case #%d: Bad magician!\n",test);
		}
		else if(!eq())
		{
			printf("Case #%d: Volunteer cheated!\n",test);
		}
		else
		{
			for(i=0;i<4;i++)
			{
				if(r[i]==c[i])
				k=r[i];
			}
			printf("Case #%d: %d\n",test,k);
		}
	}


	return 0;
}
