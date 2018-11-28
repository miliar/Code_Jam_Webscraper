#include <iostream>
#include <cstdio>
#include <cassert>
using namespace std;

/* run this program using the console pauser or add your own getch, system("pause") or input loop */

int main()
{
	freopen("A-small-attempt0.in","r",stdin);
	freopen("data.out","w",stdout);
	int T;
	int a1[4][4];
	int a2[4][4];
	int r1,r2;
	int count,number,outnumber;
	scanf("%d",&T);
	for(int i=0;i<T;i++)
	{
		scanf("%d",&r1);
		for(int j=0;j<4;j++)
		{
			scanf("%d%d%d%d",a1[j],a1[j]+1,a1[j]+2,a1[j]+3);
	//		printf("%d%d%d%d\n",a1[j][0],a1[j][1],a1[j][2],a1[j][3]);
		}
		scanf("%d",&r2);
		for(int j=0;j<4;j++)
		{
			scanf("%d%d%d%d",a2[j],a2[j]+1,a2[j]+2,a2[j]+3);
		}
		count=0;
		for(int j=0;j<4;j++)
		{
			number=a1[r1-1][j];
			for(int k=0;k<4;k++)
			{
				if(number==a2[r2-1][k])
				{
					count++;
					outnumber=number;
					break;
				}	
			}
		}
		if(count==0)
		{
			printf("Case #%d: Volunteer cheated!\n",i+1);
		}
		else if(count==1)
		{
			printf("Case #%d: %d\n",i+1,outnumber);
		}
		else
		{
			printf("Case #%d: Bad magician!\n",i+1);
		}
	}

	return 0;
}


