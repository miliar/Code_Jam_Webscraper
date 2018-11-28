#include <iostream>
#include <cstdio>
using namespace std;

int main()
{
    //freopen("b2.in","r",stdin);
    //freopen("b2.out","w",stdout);
    int cas;
    double c,f,x;
    scanf("%d",&cas);
    int tt=0;
    while(cas--){
        tt++;
        scanf("%lf%lf%lf",&c,&f,&x);

        printf("Case #%d: ",tt);

        double ans=x/2.0;
        double rate=2.0;
        double last=ans;
        //int now=-1;
        for(int i=0;i<=200000;i++)
        {
            double tmp=last-x/rate+c/rate;
            rate=rate+f;
            tmp=tmp+x/rate;
            last=tmp;
            if(tmp<ans)
                ans=tmp;
        }
        printf("%.8f\n",ans);
    }
    return 0;
}
