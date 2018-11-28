#include<iostream>
#include<cstdio>
using namespace std;

int main()
{
	int t,a,b,ar[4][4],arr[4],brr[4],cnt,num,i,j,k;
	scanf("%d",&t);
	for(k=1;k<=t;k++)
	{
		cnt=num=0;
		scanf("%d",&a);
		for(i=0;i<4;i++)
			for(j=0;j<4;j++)
				scanf("%d",&ar[i][j]);
		a--;
		for(i=0;i<4;i++)
			arr[i]=ar[a][i];
		
		scanf("%d",&b);
		
		for(i=0;i<4;i++)
			for(j=0;j<4;j++)
				scanf("%d",&ar[i][j]);
		b--;
		for(i=0;i<4;i++)
			brr[i]=ar[b][i];
		
		for(i=0;i<4;i++)
		{
			for(j=0;j<4;j++)
			{
				if(arr[i]==brr[j])
				{
					cnt++;
					num=arr[i];
				}
			}
		}
		printf("Case #%d: ",k);
		if(cnt==0)
		{
			printf("Volunteer cheated!\n");
		}
		else if(cnt==1)
		{
			printf("%d\n",num);
		}
		else
		{
			printf("Bad magician!\n");
		}
	}
	return 0;
}
		
		