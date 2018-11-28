#include <cstdio>
#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;
int test,i,n,j,k,x,sum;
double arr[1005],brr[1005],node[1005],pen[1005];
void SORT();
int main()
{
	freopen("D-large.in","r",stdin);
	freopen("output.txt","w",stdout);
    scanf("%d",&test);
	for(i=1;i<=test;i++)
    {
		x = 0;
		sum=0;
		scanf("%d",&n);
		for(j=0;j<n;j++)
		{
			scanf("%lf",&node[j]);
			arr[j] = node[j];
		}
		for(j=0;j<n;j++)
		{
			scanf("%lf",&pen[j]);
			brr[j] = pen[j];
		}
		SORT();
		for(j=0;j<n;j++)
        {
			for(k=0;k<n;k++)
			{
				if(node[k] > pen[j])
				{
					node[k] = 0;
					pen[j] = 0;
					x++;
					break;
				}
			}
		}
		for(j=0;j<n;j++)
		{
			for(k=0;k<n;k++)
			{
				if(brr[k] > arr[j])
				{
					sum++;	brr[k] = 0;
					arr[j] = 0;
					break;
				}
			}
		}
		printf("Case #%d: %d %d\n",i,x,n-sum);
	}
	return 0;
}
void SORT()
{
        sort(arr,arr+n);
		sort(brr,brr+n);
		sort(node,node+n);
		sort(pen,pen+n);
}
