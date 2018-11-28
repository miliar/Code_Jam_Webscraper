#include <iostream>
#include <cstring>
#include <cmath>
#include <algorithm>
#include <cstdlib>
#include <cstdio>
#define N 100000
#define INF 0x7ffffff
#define eqs 1e-7
using namespace std;
double a,b;
int main()
{
    freopen("B-small-attempt1.in","r",stdin);
    freopen("B-small-attempt1.out","w",stdout);
    int t,T = 1;
    scanf("%d",&t);
    while(t--)
    {
        double c,f,x;
        scanf("%lf %lf %lf",&c,&f,&x);
        double Min = INF;
        double s = 0;
        double z = 2;
        while(true)
        {
            a = s+ x/z;
            if(Min>a||fabs(Min-a)<=eqs)
            {
                Min = a;
            }else
            {
                break;
            }
            s+=c/z;
            z+=f;
        }
        printf("Case #%d: %.7lf\n",T++,Min);
    }
    return 0;
}
