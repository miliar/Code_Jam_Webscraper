#include<bits/stdc++.h>
using namespace std;
#define ll long long
int main()
{
	int i,j,k,t,n,m,count;
	scanf("%d",&t);
	for(k=1;k<=t;k++)
	{
		scanf("%d",&n);
		if(n==0){
			printf("Case #%d: INSOMNIA\n",k);
		}
		else{
				int nums[10]={0},temp;
				for(i=1;i<=100;i++)
				{
					temp=n*i;
					while(temp>0)
					{
						nums[temp%10]=1;
						temp/=10;
					}
					for(j=0;j<=9;j++)
					{
						if(nums[j]==0)
						{
							break;
						}
					}
					if(j==10)
						break;
				}
				printf("Case #%d: %d\n",k,n*i);
		}
	}
	return 0;
}
