#include<stdio.h>
#include<iostream>
int main()
{
	int arr[5]={1,4,9,121,484},t;
	scanf("%d",&t);
	for(int i=1;i<=t;i++)
	{
		int a,b,count=0;
		scanf("%d %d",&a,&b);
		for(int j=0;j<5;j++)
		{
			if((arr[j]>=a)&&(arr[j]<=b))
			{
				count++;
			}
		}
		printf("Case #%d: %d\n",i,count);		
	}	
	return 0;
}
