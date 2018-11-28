#include <stdio.h>

using namespace std;

int main()
{
    int T;
    scanf("%d",&T);
    for(int k=1;k<=T;k++)
    {
        double c,f,x,t,r,tmp;
        r=2;tmp=0;
        scanf("%lf%lf%lf",&c,&f,&x);
        t=x/r;
        while(1)
        {
            tmp+=(c/r);
            if(t>(x/(f+r))+tmp) {t=(x/(f+r))+tmp;r+=f;}
            else break;
        }
        printf("Case #%d: %.7lf\n",k,t);
    }
    return 0;
}
