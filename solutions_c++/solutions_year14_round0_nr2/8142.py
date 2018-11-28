#include <cstdio>
#define eps 1e-9

using namespace std;

double X, C, F;

double binara (double st, double dr);
inline double ABS (double x) {return x>0?x:-x;}
int verifica (double);

int main()
{
    int i, t;
    freopen ("fis.in", "r", stdin);
    freopen ("fis.out", "w", stdout);
    scanf ("%d\n", &t);
    for (i=1; i<=t; i++)
    {
        double rez;
        scanf ("%lf %lf %lf\n", &C, &F, &X);
        rez = binara (0, 200000);
        printf ("Case #%d: ", i );
        printf ("%.7lf\n", rez);
    }
    return 0;
}

double binara (double st, double dr)
{
    double mij, p=dr;
    while (ABS(dr-st)>eps){
        mij = st + (dr - st)/2;
        if (verifica (mij)){
            p = mij;
            dr = mij-eps;
        } else
            st = mij + eps;
    }
    return p;
}

int verifica (double mij){
    double rate = 2.0;
    while (1){
        if (rate*mij >= X)
            return 1;
        if (mij < C/rate)
            return 0;
        mij -= C/rate;
        rate += F;
    }
    return 0;
}