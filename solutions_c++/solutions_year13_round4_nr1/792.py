# include <stdio.h>


long long o[1010], e[1010], p[1010], q[1010] ;
long long N ;
long long MOD = 1000002013LL ;
long long _M = 500001007LL ;


long long calc(long long x)
{
	if (x == 0) return 0 ;
	if (x == 1) return N ;
	long long a = MOD-((x*x-x)%MOD), b = N*x%MOD ;
	a = (a*_M)%MOD ;
	return (a+b)%MOD ;
	
}


int main ()
{
	int T, nCase = 1 ;
	long long i, j, t, n ;
	long long tot, sum ;
	freopen ("A-large.in", "r", stdin) ;
	freopen ("A-large.txt", "w", stdout) ;
	
	scanf ("%d", &T) ;
	while (T--)
	{
		scanf ("%I64d%I64d", &N, &n) ;
		tot = 0 ;
		for (i = 0 ; i < n ; i++)
			scanf ("%I64d%I64d%I64d", &o[i], &e[i], &p[i]), q[i] = p[i], tot = (tot + calc(e[i]-o[i])*p[i])%MOD ;
		for (i = 0 ; i < n ; i++)
			for (j = 0 ; j < i ; j++)
				if (o[i] < o[j])
					t = o[i], o[i] = o[j], o[j] = t,
					t = p[i], p[i] = p[j], p[j] = t ;
		for (i = 0 ; i < n ; i++)
			for (j = 0 ; j < i ; j++)
				if (e[i] < e[j])
					t = e[i], e[i] = e[j], e[j] = t,
					t = q[i], q[i] = q[j], q[j] = t ;
		sum = 0 ;
		for (i = 0 ; i < n ; i++)
		{
			for (j = n-1 ; j >= 0 ; j--)
			{
				if (o[j] <= e[i])
				{
					if (p[j] >= q[i])
					{
						sum = (sum+calc(e[i]-o[j])*q[i])%MOD ;
						p[j] -= q[i] ;
						break ;
					}
					else
					{
						sum = (sum+calc(e[i]-o[j])*p[j])%MOD ;
						q[i]-=p[j], p[j] = 0 ;
					}
				}
			}
		}
		tot = (tot+MOD-sum)%MOD ;
		printf ("Case #%d: %I64d\n", nCase++, tot) ;
	}
	return 0 ;
}
