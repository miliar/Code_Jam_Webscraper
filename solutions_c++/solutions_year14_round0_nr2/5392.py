#include <iostream>
using namespace std;
const double epos = 1e-6;
int main(void)
{
    double c,f,x,v,t1,t2,t,mins;
    int tc,st,i,oo = 0;
    scanf("%d",&tc);
    for(i=1;i<=tc;i++){
                       printf("Case #%d: ",i);
                       scanf("%lf%lf%lf",&c,&f,&x);
                       v = 2.0;
                       t = 0;
                       oo = 0;
                       mins = x/v;
                       while(1){
                                t1 = t+x/v;
                                t2 = t + c/v + x/(v+f);
                                if(t2-t1>epos)break;
                                if(t2<mins)mins = t2;
                                t = t + c/v;
                                v = v+f;
                                ++oo;
                                if(oo > 5000000)break;
                                }
                       printf("%.7lf\n",mins);
                       }
    return 0;
}
    
