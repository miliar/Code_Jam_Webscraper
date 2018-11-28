#include <cstdio>
#include <iostream>
#include <cmath>
using namespace std;

void solve(){
     double c,f,x;
     scanf("%lf %lf %lf",&c,&f,&x);
     double ret = x/2.0;
     double mul = 0;
     double tmp;
     for (int i=1;i<=1000000;++i){
         tmp = mul+c/(2.0+(i-1)*f)+x/(2.0+i*f);
         ret = min(ret,tmp);
         mul = mul+c/(2.0+(i-1)*f);
     }
     printf("%.7lf\n",ret);
}
int main(){
    int ntest;
    scanf("%d",&ntest);
    for (int test=1;test<=ntest;++test){
        printf("Case #%d: ",test);
        solve();
    }
    return 0;
}
