#include<iostream>
#include<cstdio>
#include<cstring>
#include<algorithm>
#include<vector>
#include<cmath>
#define LL long long int
#define LIM 1001
using namespace std;
int arr[LIM],k;
int check(int num)
{
	int n,i,j;
	n=log10(num)+1;
	int dig[n];
	i=0;
	while(num>0)
	{
		dig[i++]=num%10;
		num/=10;	
	}
	for(i=0,j=n-1;i<=j;i++,j--)
	{
		if(dig[i]==dig[j])
			continue;
		else
			return 0;
	}
	return 1;
}
void precompute()
{
	int i,val,temp;
	k=0;	
	for(i=1;i<=31;i++)
	{
		if(check(i))
		{
			temp=i*i;			
			val=check(temp);
			if(val==1)
				arr[k++]=temp;

		}
	}

}
int main()
{
	int t,i,low,high,ans,a,b;
	precompute();
	scanf("%d",&t);
	i=1;
	while(i<=t)
	{
		scanf("%d %d",&a,&b);	
		low=lower_bound(arr,arr+k,a)-arr;
		high=upper_bound(arr,arr+k,b)-arr;
		ans=high-low;
		printf("Case #%d: %d\n",i,ans);
		i++;
	}
	return 0;
}
