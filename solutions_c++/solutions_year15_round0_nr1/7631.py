#include<stdio.h>
int main()
{
	int i,tmp,t,smax,standing,ans;
	char arr[10022];
	scanf("%d",&t);
	tmp=t;
	while(t--)
	{
		scanf("%d%s",&smax,arr);
		ans=0;
		standing=arr[0]-'0';
		for(i=1;i<=smax;i++)
		{
			if(standing>=i)
			{
				standing+=arr[i]-'0';
			}
			else if(arr[i]-'0'>0)
			{
				ans+=i-standing;
				standing+=i-standing+(arr[i]-'0');
			}
		}
		printf("Case #%d: %d\n",tmp-t,ans);
	}
	return 0;
}
