#include <cstdio>
#include <cmath>
#include <algorithm>
using namespace std;

#define EPS 1e-6

double rate[100];
double temp[100];

int main()
{
	int t;
	scanf("%d",&t);

	for(int casenum=1; casenum<=t; casenum++)
	{
		int n;
		double v,x;
		scanf("%d %lf %lf",&n,&v,&x);
		for(int i=0; i<n; i++)
		{
			scanf("%lf %lf",rate+i,temp+i);
		}

		{
			double hvalid = false;
			double lvalid = false;
			for(int i=0; i<n; i++)
			{
				if(temp[i]-x>=-EPS)
				{
					hvalid = true;
				}
				if(temp[i]-x<=EPS)
					lvalid = true;
			}

			if(!hvalid || !lvalid)
			{
				printf("Case #%d: IMPOSSIBLE\n",casenum);
			}
			else
			{
				if(n>2)
					continue;
				if(n==1)
				{
					printf("Case #%d: %.8lf\n",casenum,v/rate[0]);
				}
				else if(fabs(temp[0]-temp[1])<EPS)
				{
					//get the one with higher flow rate
					double tm = v/(rate[0]+rate[1]);
					printf("Case #%d: %.8lf\n",casenum,tm);
				}
				else
				{
					double v1 = v*(x-temp[1])/(temp[0]-temp[1]);
					double v2 = v-v1;
					printf("Case #%d: %.8lf\n",casenum,max(v1/rate[0],v2/rate[1]));
				}
			}
		}
	}
}