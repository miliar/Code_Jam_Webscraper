#include <cstdio>
#include <iostream>
#include <bits/stdc++.h>
#define pc putchar
using namespace std;

double c,f,x;

/*double fun(double r)
{
	if(r>x)
        return 1.0;
	return min(x/r,(c/r+fun(r+f)));
}*/

int main()
{
    freopen("B-large.in", "r", stdin);
    freopen("outbig1.txt", "w", stdout);
    int t;
    scanf("%d", &t);
    for(int k=1; k<=t; k++)
    {
        scanf("%lf %lf %lf", &c, &f, &x);
        double ans = 0;
        double prod = 2;

        while(1)
        {

            double t1 = x/prod;
            double t2 = (c/prod)+(x/(f+prod));
            if(t2<t1)
            {
                ans+=(c/prod);
                prod+=f;
            }
            else
            {
                ans+=(x/prod);
                break;
            }

        }
        printf("Case #%d: ", k);
        printf("%.7lf\n", ans);
    }
	return 0;
}
