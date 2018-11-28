#include <cstdio>
#include <algorithm>
#include <cmath>
#include <cstdlib>
using namespace std;

const int Maxn=105;
const long double Eps=1e-5;

long double r[Maxn], c[Maxn];

int main()
{
	int T, n;
	long double v, x;
	scanf("%d", &T);
	for (int tt=1; tt<=T; ++tt)
	{
		scanf("%d%Lf%Lf", &n, &v, &x);
		for (int i=0; i<n; ++i) scanf("%Lf%Lf", r+i, c+i);
		printf("Case #%d: ", tt);
		if (n==1)
		{
			if (fabs(x-c[0])<Eps) printf("%.8Lf\n", v/r[0]);
			else puts("IMPOSSIBLE");
		}else
		{
			if (fabs(c[0]-c[1])<Eps)
			{
				if (fabs(x-c[0])<Eps) printf("%.9Lf\n", v/(r[0]+r[1]));
				else puts("IMPOSSIBLE");
				continue;
			}
			long double t0=v*(x-c[1])/(r[0]*(c[0]-c[1]));
			long double t1=v*(x-c[0])/(r[1]*(c[1]-c[0]));
			if (c[0]<=x && x<=c[1] || c[0]>=x && x>=c[1]) printf("%.9Lf\n", max(t0, t1));
			else puts("IMPOSSIBLE");
		}
	}
	return 0;
}

