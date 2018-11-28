#include<stdio.h>

int main()
{
//	freopen("inptu", "r", stdin);
//	freopen("output.txt", "w", stdout);
	int i,input,a,j,k,t,g,tmp,ans;
	int arr[1100];
	int max;
	freopen("B-large.in", "r", stdin);
	freopen("output.txt", "w", stdout);

	//printf("Enter:");
	scanf("%d",&input);
	for(i=0; i<input; i++)
	{
		max=0;
		scanf("%d",&a);
		for(k=1; k<=a; k++)
		{
			scanf("%d",&arr[k]);
			if(max<arr[k])
				max=arr[k];
		}
		ans = max;
		for(j=1; j<=max; j++)
		{
			tmp=j;
			for(t=1; t<=a; t++)
			{
				if(j >= arr[t])
					continue;
				tmp+=arr[t]/j-1;
				if(arr[t]%j!=0)tmp++;

			}
			if(ans>tmp) ans=tmp;	
		}
		printf("Case #%d: %d\n",i+1,ans);
	}
	return 0;
}