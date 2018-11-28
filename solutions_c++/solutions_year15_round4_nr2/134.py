#include <stdio.h>
#include <string.h>
#include <algorithm>
#include <cmath>

using namespace std;

typedef pair<double,double> pii;

const double eps = 1e-9;

pii pipe[111];

int main(void)
{
	int T = 0;
	int TK = 0;
	scanf("%d",&T);
	while(T--)
	{
		int N = 0;
		scanf("%d",&N);
		double V = 0.0;
		double X = 0.0;
		scanf("%lf %lf",&V,&X);

		for(int i = 0;i < N;i++) scanf("%lf %lf",&pipe[i].first,&pipe[i].second);
		sort(pipe,pipe+N);

		double ans = 1e200;
		for(int i = 0;i < N;i++)
		{
			if(fabs(pipe[i].second-X) < eps)
			{
				ans = min(ans, V/pipe[i].first);
			}
		}
		if(N > 1)
		{
			if(fabs(pipe[0].second - pipe[1].second) < eps && fabs(pipe[0].second-X) < eps)
			{
				ans = min(ans, V/(pipe[0].first + pipe[1].first));
			}
			else
			{
				double V0 = V*(X-pipe[1].second)/(pipe[0].second-pipe[1].second);
				if(V0 > eps)
				{
					double V1 = V-V0;
					if(V1 > eps)
					{
						ans = min(ans, max(V0/pipe[0].first, V1/pipe[1].first));
					}
				}
			}
		}
		printf("Case #%d: ",++TK);
		if(ans > 1e111) puts("IMPOSSIBLE");
		else printf("%.9f\n",ans);
	}
	return 0;
}
