#include <stdio.h>
#include <string.h>
#include <algorithm>

using namespace std;

const double eps = 1e-7;

double c,f,x;
//
//double product(int n)
//{
//    return 2.0 + f * n;
//}
//
//double cost(int n)
//{
//    if(n == 0)
//        return 0.0;
//    else
//        return cost(n - 1) + c / product(n - 1);
//}

int main()
{
    freopen("in.ads","r",stdin);
    freopen("out.ads","w",stdout);
    int T,ncase = 0;
    scanf("%d",&T);
    while(T--)
    {
        scanf("%lf%lf%lf",&c,&f,&x);
        double product = 2.0;
        double cost = 0.0;
        double t = x / product;
        for(int i=1;;i++)
        {
            cost += c / product;
            product += f;
            double tt = cost + x / product;
            if(tt > t - eps)
            {
                break;
            }
            else
            {
                t = tt;
            }
        }
        printf("Case #%d: %.7f\n",++ncase,t);
    }
    return 0;
}
