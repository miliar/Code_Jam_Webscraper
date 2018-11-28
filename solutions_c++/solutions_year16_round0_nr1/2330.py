# include <cstdio>
# include <cstring>
# define NR 100100
# define REP (i, a, b) for (int i = (a); i <= (b); i ++)
bool Tag[15];
long long x;
inline bool DealDight (long long w)
{
	for ( ; w; Tag[w % 10] = true, w /= 10);
	REP (i, 0, 9) if (!Tag[i]) return false;
	return true;
}
inline void Solve ()
{
	scanf ("%d", &x);
	if (!x)
	{
		puts ("INSOMNIA");
		return;
	}
	memset (Tag, 0, sizeof (Tag));
	long long tmp = x;
	for( ; ; x += tmp)
		if (DealDight(x)) {printf ("%lld\n", x); return;}

}
int main ()
{
	freopen ( "FA.in", "r", stdin);
	freopen ( "FA.out", "w", stdout);
	int T; scanf ( "%d", &T);
	REP (Case , 1, T){
		printf ("Case #%d: ", Case);
		Solve ();
	}
	return 0;
}
