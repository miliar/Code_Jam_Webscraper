#include <cstdio>
#define oo 100000

using namespace std;
double NR,time,prev,sol,C,F,X;
int t,T,i,n,OK;
int main()
{
    freopen("cookie.in","r",stdin);
    freopen("cookie.out", "w", stdout);
    scanf("%d", &T);
    for(t=1;t<=T;++t)
    {
        scanf("%lf%lf%lf", &C, &F, &X);
        NR=0;OK=1;prev=oo+1;n=0;time=X/2;
        while(OK)
        {
            NR+=(C/(2+n*F));
            n++;
            prev=time;
            time=NR+X/(2+n*F);
            if(prev<=time)
            {
                OK=0;
                sol=prev;
            }
        }
        printf("Case #%d: %.7lf\n", t, sol);
    }
    return 0;
}
