#include <cstdio>
#include <algorithm>
using namespace std;

int main(){
    int T;
    scanf("%d",&T);
    for(int ix=0;ix<T;ix++){
        printf("Case #%d: ",ix+1);
        double C,F,X;
        scanf("%lf%lf%lf",&C,&F,&X);
        double acc=0,mi=X/2,cps=2;
        while(acc < mi){
            acc+=C/cps;
            cps+=F;
            mi=min(mi,acc+X/cps);
        }
        printf("%.7f\n",mi);
    }
}
