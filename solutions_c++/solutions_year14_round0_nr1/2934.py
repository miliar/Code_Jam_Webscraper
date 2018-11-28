#include<cstdio>
#include<algorithm>
using namespace std;
int main()
{	int a[4][4],b[4][4],i,j,t,a1,b1,k;
	//memset(c,0,sizeof(c));
	scanf("%d",&t);
	for(i=1;i<=t;i++)
	{	int c[16];
		for(j=0;j<16;j++)	c[j]=0;
		scanf("%d\n",&a1);
		for(j=0;j<4;j++)
		{	for(k=0;k<4;k++)
			{	scanf("%d",&a[j][k]);
				if(j==a1-1)
				{	c[a[j][k]]++;
				}
			}

		}
		scanf("%d",&b1);
		for(j=0;j<4;j++)
		{	for(k=0;k<4;k++)
			{	scanf("%d",&b[j][k]);
				if(j==b1-1)
				{	c[b[j][k]]++;
				}
			}
		}
		int num=0,count=0;
		for(j=0;j<16;j++)
		{	if(c[j]==2)
			{	num=j;count++;
			}
		}
		if(count==1)
		{	printf("Case #%d: %d\n",i,num);}
		else if(count>1)
		{	printf("Case #%d: Bad magician!\n",i);	}
		else if(count==0)
		{	printf("Case #%d: Volunteer cheated!\n",i);	}
	}
		  
	return 0;
}
