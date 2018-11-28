#include<iostream>
#include<cstdio>
#include<cstring>
using namespace std;
int T;
double C,F,X;
int main(){
    freopen("B-large.in","r",stdin);
    freopen("B-large.txt","w",stdout);
    cin>>T;
    for(int cas=1;cas<=T;++cas){
            scanf("%lf%lf%lf",&C,&F,&X);
            double delta=2.0;
            double t=0;
            double tot=0;
            if(X<C){
                printf("Case #%d: %lf\n",cas,(X/delta));
                continue;
            }
            int i;
            for(i=0;;i++){
                t+=C/delta;
                if(((double)i+1.0)*C*F>X*F-2.0*C){
                   t+=(X-C)/(2.0+(double)i*F);
                   break; 
                }
                delta+=F;
            }
            printf("Case #%d: %.7lf\n",cas,t);
    }
    return 0;
}
