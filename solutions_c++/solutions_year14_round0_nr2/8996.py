//
//  main.cpp
//  cj14_round0_b
//

#include <iostream>
#include <cstdio>
#include <cmath>

int main()
{
    int T, TN,n,i;
    double  c, f, x, t; 
    freopen("B-large.in","r",stdin);
    freopen("B-large.txt","w",stdout);
    scanf("%d", &TN);
    for (T = 0; T<TN; T++)
    {
	scanf("%lf %lf %lf", &c, &f, &x);
	x /= 2; f/= 2; c/=2;
	n = floor(x/c-1/f);
	if (n<0)
		n=0;
	t = x/(1+n*f);
	for (i=0; i<n; i++)
		t += c/(1+i*f);
        printf("Case #%d: %.7lf\n", T+1, t);
    }
    fclose(stdin);
    fclose(stdout);
    return 0;
}


