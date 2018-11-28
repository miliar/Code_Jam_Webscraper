#include<stdio.h>
int arr[10005];
int main(void)
{
	
freopen("C:\\Users\\user\\Desktop\\A-large.in","r",stdin);
freopen("C:\\Users\\user\\Desktop\\out1.txt","w",stdout);

	int t;
	scanf("%d",&t);
	for(int i=1;i<=t;i++)
	{
		int n,ans1=0,ans2=0,max=0;
		scanf("%d",&n);
		for(int j=0;j<n;j++)
		scanf("%d",&arr[j]);
		for(int j=0;j<n-1;j++)
		{
			if(arr[j]>arr[j+1])
			{
				ans1=ans1+arr[j]-arr[j+1];
				if((arr[j]-arr[j+1])>max)
				max=arr[j]-arr[j+1];
			}
		}
		for(int j=0;j<n-1;j++)
		{
				if(arr[j]<max)
				ans2=ans2+arr[j];
				else
				ans2=ans2+max;
			
		}
		printf("Case #%d: %d %d\n",i,ans1,ans2);
	}
	return 0;
}