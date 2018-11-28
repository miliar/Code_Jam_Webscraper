#include <iostream>
#include <cstdio>
#include <vector>
using namespace std;
#define EPS 1e-9
int main() {
    int t;
    double C,X,F;
    //freopen("cookie.c","r",stdin);
    //freopen("cookie.out","w",stdout);
    scanf("%d",&t);
    for(int ca=1; ca<=t; ca++) {
        cin>>C>>F>>X;
       double mn=2139999999.0;
       double ant=0.0,act;
       double tam=10.0*max(C,X);
       for(double i=2.0;i<=tam;i+=F){
         act=ant+(X/i);
         if(act<mn+EPS)
            mn=act;
            else
                break;
           ant+=(C/i);
        }
        printf("Case #%d: %.7f\n",ca,mn);
    }
    return 0;
}
