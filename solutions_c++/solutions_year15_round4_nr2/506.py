#include <cstdio>
#include <cmath>
#include <algorithm>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include "auxiliary.h"
#define longd long double


using namespace std;

//longd abs(longd x) {if (x<0) return -x; return x;}
int n,m,testnum,ans;
struct item
{
    longd r,c,t;
}a[11111];

longd v,x;

bool cmp(item u, item v) {return u.c<v.c;}



int main(int argc, char* argv[])
{
    freopen("/Users/Dora/Desktop/ex/ex/x.in","r",stdin);
    freopen("/Users/Dora/Desktop/ex/ex/x.out","w",stdout);
    scanf("%d",&testnum);
    for (int test=1; test<=testnum; ++test)
    {
        scanf("%d %Lf %Lf",&n,&v,&x);
        longd speed=0;
        for (int i=0; i<n; ++i)
        {
            scanf("%Lf %Lf",&a[i].r,&a[i].c);
            speed+=a[i].r;
        }
        longd time=v/speed,sp;
        bool flag=false;
        for (int i=0; i<n; ++i) a[i].t=time;
        longd now=ac();
        if (now!=x)
        {
            sp=speed;
            for (int i=n-1; a[i].c>x; --i)
            {
                sp-=a[i].r;
                time=v/sp;
                for (int j=0; j<i; ++j) a[j].t=time;
                a[i].t=0;
                if (ac()>x) continue;
                else
                {
                    flag=true;
                    a[i].t=((fun_sum()-a[i].r*a[i].t*a[i].c)-x*(fun_tmp()-a[i].r*a[i].t))/a[i].r/(x-a[i].c);
                    time=0;
                    for (int j=0; j<=i; ++j) if (a[j].t>time) time =a[j].t;
                    break;
                }
            }
        }
        else {flag=true;}
        
        if (flag) printf("Case #%d: %.20Lf\n",test,time);
        else printf("Case #%d: %s\n",test,"IMPOSSIBLE");
    }
}