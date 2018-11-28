#include <cstdio>
#include <cstring>
using namespace std;

double EPS = 1e-7;

int main()
{
    freopen("B-small-attempt0.in","r",stdin);
    freopen("B_output.txt","w",stdout);
    int T;
    double C,F,X;
    scanf("%d",&T);
    for (int cases=1;cases<=T;cases++)
    {
        scanf("%lf%lf%lf",&C,&F,&X);
        double now = 0;
        double farms = 0;
        double result = 0;
        while (now<X)
        {
            double t1 = (X - now)/(2.0 + F*farms);
            double t2 = (now>=C)?((X-now+C)/(2.0+F*(farms+1.0))):((C-now)/(2.0+F*farms)+X/(2.0+F*(farms+1.0)));
            if (t1-EPS<t2)
            {
                result += t1;
                now = X;
            }else{
                if (now>=C)
                {
                    now -= C;
                    farms++;
                }else{
                    result += (C-now)/(2.0+F*farms);
                    now = 0;
                    farms++;
                }
            }
        }
        printf("Case #%d: %.7lf\n",cases,result);
    }
    return 0;
}
