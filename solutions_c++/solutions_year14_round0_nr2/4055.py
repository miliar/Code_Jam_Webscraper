#include <iostream>
#include <string>

using namespace std;

int main(int argc, char *argv[])
{
	int T, Cases = 0;
	long double X, CF, F, C, t0, tc, prev;
	scanf("%d\n", &T);
    do
    {
		scanf("%lf%lf%lf", &C, &F, &X);
		CF = 2;
		t0 = X/CF;
		tc = C/CF;
		if( t0 <= tc)
		{
			printf("Case #%d: %.7lf\n", ++Cases, t0);
			continue;
		}
		do
		{
			CF += F;
			prev = t0;
			t0 = tc + (X/CF);
			tc += (C/CF);
		}while (prev > t0);
		printf("Case #%d: %.7lf\n", ++Cases, prev);

	}while(--T); 
}