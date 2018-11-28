#include <iostream>
#include <cstdio>
#include <cstring>
#include <cmath>

using namespace std;

#define LL long long
#define eps 0.00000001

int HM[10000005];

int check_pal(LL nr)
{
	LL cnr = nr, rnr = 0;
	while (cnr)
	{
		rnr = rnr * 10 + (cnr % 10LL);
		cnr /= 10LL;
	}	
	if (nr == rnr) return 1;
	return 0;		
}

int main()
{
	freopen ("tests.in", "r", stdin);
	freopen ("tests.out", "w", stdout);	

	for (int i = 1; i <= 10000000; ++i)
	{
		HM[i] = HM[i-1];
		LL nr = i;
		LL snr = nr * nr;
		if (check_pal(nr) && check_pal(nr*nr)) //printf ("%lld %lld\n", nr, snr);
			++HM[i];
	}

	int T;
	scanf ("%d", &T);

	for (int t = 1; t <= T; ++t)
	{
		LL A, B;
		scanf ("%lld %lld", &A, &B);	
		double a = sqrt((double)A) + eps;
		LL la = (LL)a;
		double b = sqrt((double)B) + eps;
		LL lb = (LL)b;	

		if (la * la != A) ++la;		

		printf ("Case #%d: %d\n", t, HM[lb] - HM[la-1]);
	}

	return 0;
}
