#include <stdio.h>
#define eps 1e-8

long long r, t, ret;
long long lf, rt, mid;

double tt, tmp, s;

int main()
{
	int T, cas, i;
	scanf("%d", &T);
	for (cas = 1; cas <= T; cas++)
	{
		scanf("%I64d%lf", &r, &tt);
		lf = 1; rt = 1e12;
		//tt = 1.0 * t;
		while (lf <= rt)
		{
			mid = (lf + rt) / 2;
			s = (2.0 * r + 1) + (2.0 * r + 4.0 * (mid - 1) + 1);
			tmp = 1.0 * s * mid / 2;
			//printf("s = %f tmp = %f, mid = %I64d\n", s, tmp, mid);
			//printf("tt  = %f\n", tt);
			if (tmp - tt > eps)
				rt = mid - 1;
			else
				lf = mid + 1;
		}
		ret = rt;
		printf("Case #%d: %I64d\n", cas, ret);
	}
	return 0;
}
