#include <iostream>
#include <cstdio>
#include <cstring>
using namespace std;

int main()
{
    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);
  //  freopen("test.txt","r",stdin);
    int T;scanf("%d",&T);
    for(int cas = 1; cas <= T;cas++){
        double C,F,X;
        scanf("%lf%lf%lf",&C,&F,&X);
        double per = 2,tim = 0;
        if(X <= C) tim = X / 2;
        else{
            double farm = C / per;
            tim += farm;
            while(true){
                double notbuy = (X - C) / per;
                double buy = X / (per + F);
                if(notbuy < buy){
                    tim += notbuy;
                    break;
                }
                else{
                    tim += C / (per + F);
                    per += F;
                }
            }
        }
        printf("Case #%d: ",cas);
        printf("%.7f\n",tim);
    }

    return 0;
}
