#include<cstdio>
using namespace std;
double min(double a, double b)
{
    if(a < b)
        return a;
    return b;
}
int main()
{  
    int lp;
    scanf("%d", &lp);
    for(int pr = 0; pr < lp; pr++)
    {
        double cs,kf,wyg,t,bcs;
        double wynik;
        scanf("%lf %lf %lf", &kf, &bcs, &wyg);
        t = 0.0;
        cs = 2.0;
        wynik = wyg/cs;
        while(t < wynik)
        {
            wynik = min(wynik, t + wyg/cs);
            t += kf/cs;
            cs += bcs;
        }
        printf("Case #%d: %.7lf\n",pr+1,wynik);
    }
}
