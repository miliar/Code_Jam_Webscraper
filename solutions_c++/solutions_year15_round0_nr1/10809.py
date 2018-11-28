# include <stdio.h>
# define MAX 7

int main()
{
	int n; // no. of test cases
	scanf("%d",&n);
	int Smax,garb;
	int count=0;
	for(int i=1;i<=n;i++)
	{
		scanf("%d",&Smax);
		if(Smax==0)
			{printf("Case #%d: 0\n",i);
			scanf("%d",&garb);
			continue;
			}
		int arr[MAX];
		int num;
		scanf("%d",&num);
		for(int j=Smax;j>=0;j--)
		{
			arr[j]=(num%10);
			num=num/10;
			
		}

		count=arr[0];
		int required,ans=0;
		for(int j=1;j<=Smax;j++)
		{
			required=0;
			if(j>count)
			{
				required=(j-count);
				ans+=required;
			}
			count+=arr[j]+required;
		}
		printf("Case #%d: %d\n",i,ans);
	}
return 0;
}