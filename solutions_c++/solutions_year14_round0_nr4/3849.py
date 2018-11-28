#include<cstdlib>
#include<iostream>
using namespace std;
#include<cstdio>
long double arr[1000];
long double brr[1000];
int compare (const void * a, const void * b)
{
	if( (*(long double*)a - *(long double*)b)>0)
  return 0;
  else
  return 1;
}
int main()
{

	int t,n;
	scanf("%d",&t);
	for(int i=1;i<=t;i++)
	{
		scanf("%d",&n);
		for(int j=0;j<n;j++)
		{
			cin>>arr[j];		
		}
		for(int j=0;j<n;j++)
		{
			cin>>brr[j];		
		}
		qsort(arr,n,sizeof(long double),compare);
		qsort(brr,n,sizeof(long double),compare);
		int k=n-1;
		int count_d=0;
		for(int j=n-1;j>=0;j--)
		{
			for(;k>=0;k--)
			{
				if(arr[k]>brr[j])
				{
					//printf("first %d %d\n",k,j);
					count_d++;
					k--;
					break;
				}
			}
		}
		k=n-1;
		int count_o=0;
		for(int j=n-1;j>=0;j--)
		{
			for(;k>=0;k--)
			{
				if(arr[j]<brr[k])
				{
					//printf("second %d %d\n",j,k);
					count_o++;
					k--;
					break;
				}
			}
		}
		count_o=n-count_o;
		printf("Case #%d: %d %d\n",i,count_d,count_o);
	}
return 0;
}
