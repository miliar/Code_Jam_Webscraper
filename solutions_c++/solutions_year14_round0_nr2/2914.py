#include <cstdio>

using namespace std;

int main()
{
    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);
    int a,b,c,i,j,k;
    double C,F,X;
    scanf("%d",&a);
    for(k=1;k<=a;k++){
        printf("Case #%d: ",k);
        double time=0.0,cur=2.0;
        scanf("%lf%lf%lf",&C,&F,&X);
        if(X<=C){
            time=X/cur;
            printf("%.7f\n",time);
        }
        else{
            while(1){
                time+=C/cur;
                if(((X-C)/cur) > X/(cur+F)){
                    cur+=F;
                }
                else{
                    time+=(X-C)/cur;
                    break;
                }
            }
            printf("%.7f\n",time);
        }
    }
}
