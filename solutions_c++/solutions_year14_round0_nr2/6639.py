#include <iostream>
#include <cstdio>
#include <cstring>
#include <string>
using namespace std;

double c,f,x,curTime,curRate,curScore;
int main(){
    //freopen("test.in","r",stdin);
    //freopen("test.out","w",stdout);
    int t;scanf("%d",&t);
    for (int it=1;it<=t;it++){
        printf("Case #%d: ",it);
        scanf("%lf%lf%lf",&c,&f,&x);
        curRate = 2.0;
        curScore = 0.0;
        curTime = 0;
        while (curScore < x){
            double t1 = (x-curScore) / curRate;
            double t2 = (c-curScore) / curRate + x / (curRate + f);
            if (t2 <= t1){
                curTime = curTime + (c-curScore) / curRate;
                curRate = curRate + f;
                curScore = 0;
            }else{
                curTime = curTime + (x-curScore) / curRate;
                curScore = x;
            }
        }
        printf("%.7lf\n",curTime);
    }
    return 0;
}
