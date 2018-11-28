#include <iostream>
#include <algorithm>
#include <cstdlib>
#include <cstdio>
#include <cstring>
#include <queue>
#include <cmath>
#include <stack>
#include <map>

#pragma comment(linker, "/STACK:1024000000");
#define EPS (1e-8)
#define LL long long
#define ULL unsigned long long int
#define _LL __int64
#define _INF 0x3f3f3f3f
#define Mod 1000000007
#define LM(a,b) (((ULL)(a))<<(b))
#define RM(a,b) (((ULL)(a))>>(b))

const double PI = acos(-1.0);

using namespace std;

int main()
{
    int T;

    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);

    scanf("%d",&T);

    int icase = 1;

    double sum,x,f,c,p;

    while(T--)
    {
        scanf("%lf %lf %lf",&c,&f,&x);

        printf("Case #%d: ",icase++);

        if(c >= x)
        {
            printf("%.7lf\n",x/2);
        }
        else
        {
            sum = 0 , p = 2;

            while(1)
            {
                sum += c/p;

                if((x-c)/p > x/(p+f))
                {
                    p += f;
                }
                else
                {
                    sum += (x-c)/p;
                    break;
                }
            }
            printf("%.7lf\n",sum);

        }

    }
    return 0;
}





