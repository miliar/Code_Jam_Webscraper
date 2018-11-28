#include <iostream>
#include <cstdio>
using namespace std;

int main() {
	int t;
	scanf("%d",&t);
	int k=1;
	while(t--)
	{
		int num1;
		scanf("%d",&num1);
		int a[17]={0};
		int arr[5][5];
		int i,j;
		for(i=1;i<=4;i++)
		{
			for(j=1;j<=4;j++)
			scanf("%d",&arr[i][j]);
		}
		for(j=1;j<=4;j++)
		{
			a[arr[num1][j]]=1;
		}
		int num2;
		scanf("%d",&num2);
		for(i=1;i<=4;i++)
		{
			for(j=1;j<=4;j++)
			scanf("%d",&arr[i][j]);
		}
		for(j=1;j<=4;j++)
		{
			a[arr[num2][j]]=a[arr[num2][j]]+1;
		}
		int count=0;
		int num=0;
		for(i=1;i<=16;i++)
		{
			if(a[i]==2)
			{
				count++;
				num=i;
			}
		}
		if(count==1)
		{
			printf("Case #%d: %d\n",k++,num);
		}
		else if(count>1)
		{
			printf("Case #%d: Bad magician!\n",k++);
		}
		else
		{
			printf("Case #%d: Volunteer cheated!\n",k++);
		}
		
		
	}
	return 0;
}