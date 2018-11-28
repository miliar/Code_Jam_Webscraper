#include<cstdio>
using namespace std;
int main(){
    int T;
    scanf("%d",&T);
    double C,F,X;
    for(int p=1;p<=T;p++){
        scanf("%lf%lf%lf",&C,&F,&X);
        double up=2.0;
        double max=X/up;
        double time;
        int k=1;
        while(1){
            time=0.0;
            for(int i=0;i<k;i++){
                time+=C/(i*F+up);
            }
            double nup=up+k*F;
            time+=X/nup;
            if(time<max){
                max=time;
                k++;
            }
            else break;
        }
        printf("Case #%d: %.7lf\n",p,max);
    }
    return 0;
}
