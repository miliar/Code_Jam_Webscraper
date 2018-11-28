#include <bits/stdc++.h>

using namespace std;

int main()
{
	//freopen ("input.txt","r",stdin);
	
	int t,n,i,k=1,num,count,end,j,maxnum;
	scanf("%d",&t);
	while(k<=t)
	{
		int arr[2501]={0};
		maxnum=0;
		scanf("%d",&n);
		end=2*n*n-n;
		for(i=1 ; i<=end ; i++)
		{
			//for(j=1 ; j<=n ; j++)
			//{
				scanf("%d",&num);
				arr[num]++;
				if(maxnum<num)
					maxnum=num;
			//}
		}
	
		
		printf("Case #%d: ",k);
		count=0;
		for(i=1 ; i<=maxnum ; i++)
		{
			if(arr[i] && arr[i]%2)
			{
				printf("%d ",i);
				count++;
			}
			if(count==n)
					break;
		}
		printf("\n");
		k++;

	}
	return 0;
}
