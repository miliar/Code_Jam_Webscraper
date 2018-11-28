#include<iostream>
#include<stdio.h>
#include<string>
#include<cstdlib>
#include<string.h>
#include<math.h>
using namespace std;
#define eps 1e-6
int main(){
    int T;
    freopen("B-large.in","r",stdin);
    freopen("xxx.out","w",stdout);
    double c,f,x;
    scanf("%d",&T);
    for(int t=1;t<=T;t++) {
        scanf("%lf%lf%lf",&c,&f,&x);
        double ans=0.0;
        double ff=2.0;
        double a=x/ff;
        double b=c/ff+x/(f+ff);
        while(a>b){
            ans+=(double)c/ff;
            ff+=f;
            a=(double)x/ff;
            b=(double)c/ff+x/(f+ff);
        }
        ans+=x/ff;
        printf("Case #%d: %.7lf\n",t,ans);
    }
    return 0;
}
