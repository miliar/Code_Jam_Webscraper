#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <algorithm>

using namespace std;

int main()
{
    freopen("in.in", "r", stdin);
    freopen("out.txt", "w", stdout);
    int task;
    scanf("%d", &task);
    for (int t = 1; t <= task; ++t)
    {
	printf("Case #%d: ", t);
	double C, F, X;
	scanf("%lf%lf%lf", &C, &F, &X);
	double ans = X / 2.0;
	double tmp = 0;
	for (int i = 0; ; ++i)
	{
	    tmp += C / (2 + i * F);
	    double mid = tmp + X / (2 + (i + 1) * F);
	    if (mid > ans) break;
	    else ans = mid;
	}
	printf("%.8lf\n", ans);
    }
    return 0;
}
