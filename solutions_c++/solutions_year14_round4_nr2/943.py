#include<bits/stdc++.h>
#define s(a) scanf("%d",&a)

using namespace std;
typedef long long int ll;
int t,n;
int inp[10004];
int sorted[10004];
int main()
{
	int tt,t;
	s(t);
	for(tt=1;tt<=t;tt++)
	{
		int i,j;
		s(n);
		for(i=0;i<n;i++)
		{
			s(inp[i]);
			sorted[i] = inp[i];
		}
		sort(sorted,sorted+n);
		int hi=n-1,lo=0,res=0;
		for(i=0;i<n;i++)
		{
			for(j=lo;j<=hi;j++)
				if(inp[j]==sorted[i])break;
			int left = (j-lo);
			int right = (hi-j);
			if(left<=right)
			{
				int temp;
				while(j>lo)
				{
					temp=inp[j];
					inp[j] = inp[j-1];
					inp[j-1]=temp;
					j--;
					res++;
				}
				lo++;
			}
			else
			{

				int temp;
				while(j<hi)
				{
					temp=inp[j];
					inp[j] = inp[j+1];
					inp[j+1]=temp;
					j++;
					res++;
				}
				hi--;
			}
		}
		printf("Case #%d: %d\n",tt,res);
	}
	return 0;
}
