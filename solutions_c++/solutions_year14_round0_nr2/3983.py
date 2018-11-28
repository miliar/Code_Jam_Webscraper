#include<iostream>
#include<cstring>
#include<cstdio>
using namespace std;

double fun(double n, double X, double C, double F)
{
    double K = C/2.0;
    return ( X + n*C + F*K*n*(n+1)/2.0 ) / (2.0 + F*n);
}

int main()
{
    freopen("B.in","r",stdin);
    freopen("B.out","w",stdout);
    int T;
    double C,F,X,K,sol,temp,n,cont;
    cin>>T;
    for(int i=1;i<=T;i++)
    {
        cin>>C>>F>>X;
        cont = 1.0;
        sol = X/2.0;
        double sec = 0.0, act = 0.0, rate = 2.0;

		while (true)
		{

			double tC = C/rate, tX = (X - act)/rate;

			if (tX < tC)
			{
				sec += tX;
				break;
			}

			sec += tC;
			act += C;

			double nR = rate + F;
			if ((X-act)/rate > X/nR)
			{
				act  = 0.0;
				rate = nR;
			}
		}
        printf("Case #%d: %.7lf\n",i,sec);
    }

    return 0;
}

