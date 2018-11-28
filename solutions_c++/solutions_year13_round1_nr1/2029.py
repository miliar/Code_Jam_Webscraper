#include <stdio.h>
#include <math.h>

int main()
{
	freopen("A-small-attempt0.in", "r", stdin);
	freopen("s.out", "w", stdout);

	int T, cas;
	__int64 r, t;
	__int64 s;

	scanf("%d", &T);
	for (cas=1; cas<=T; cas++)
	{
		scanf("%I64d%I64d", &r, &t);
		s=0;
		if (2*r+1<=t)
		{
			__int64 tmp;
			double delta=sqrt( ((2*r-1)*(2*r-1)+8*t)/1.0 );
			tmp=(__int64)( ((1-2*r)+ delta)/4.0 );
			s=tmp;
			t-=2*tmp*tmp+(2*r-1)*tmp;
			r+=2*tmp;
		}
		printf("Case #%d: %I64d\n", cas, s);
	}
	return 0;
}