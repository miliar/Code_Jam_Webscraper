#include <stdio.h>
#define f(i,n) for(int  i=0; i <n;i++)

#include <algorithm>
using namespace std;

int main()
{
	int t;
	scanf("%d",&t);
	f(i,t)
	{
		double n1[1000];
		double n2[1000];
		int n;
		scanf("%d",&n);
		f(j,n)
			scanf("%lf",n1+j);
		f(j,n)
			scanf("%lf",n2+j);
		sort(n1,n1+n);
		sort(n2,n2+n);
		int left = n;
		int ind1 = 0, ind2 =0;
		int w =0;
		int wfair = 0;
		int best = n-1;
		f(j,n)
		{
			if(n1[n-1-j]>n2[best])
			{
				wfair++;
			}
			else
			{
				best--;
			}
		}

		while(left>0)
		{
			if(n1[ind1]>n2[ind2])
			{
				w++;
				ind1++;
				ind2++;
			}
			else
			{
				ind1++;
			}

			left--;
		}

		printf("Case #%d: %d %d\n", i+1,w, wfair);
	}
}
