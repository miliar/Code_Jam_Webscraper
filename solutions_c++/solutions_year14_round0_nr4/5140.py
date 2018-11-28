#include<cstdlib>
#include<iostream>
using namespace std;
#include<cstdio>

long double a[1000],b[1000];
int compare (const void * x, const void * y)
{
	if( (*(long double*)x - *(long double*)y)>0)
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
			cin>>a[j];
		}
		for(int j=0;j<n;j++)
		{
			cin>>b[j];
		}
		qsort(a,n,sizeof(long double),compare);
		qsort(b,n,sizeof(long double),compare);
		int k=n-1;
		int countd=0;
		for(int j=n-1;j>=0;j--)
		{
			for(;k>=0;k--)
			{
				if(a[k]>b[j])
				{
					countd++;
					k--;
					break;
				}
			}
		}
		k=n-1;
		int counto=0;
		for(int j=n-1;j>=0;j--)
		{
			for(;k>=0;k--)
			{
				if(a[j]<b[k])
				{
					counto++;
					k--;
					break;
				}
			}
		}
		printf("Case #%d: %d %d\n",i,countd,n-counto);
	}
    return 0;
}
