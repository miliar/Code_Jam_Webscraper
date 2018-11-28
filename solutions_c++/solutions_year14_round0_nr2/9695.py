#include <stdio.h>
double min;
double c,f,x;
void go(double time,double interval,double coin){
    if(time < min){
        if(x == coin){
            min = time;
            //sprintf("%lf\n",min);
        }else{
            if(c == coin){
                interval += f;
            }
            go(time + x/interval,interval,x);
            go(time + c/interval,interval,c);

        }
    }
}
int main(){
    freopen("B-small-attempt0.in","r",stdin);
    freopen("ouput.txt","w",stdout);
    int t;
    int temp = 0;
    scanf("%d",&t);
    while(t--){
        scanf("%lf",&c);
        scanf("%lf",&f);
        scanf("%lf",&x);
        min = x / 2.0;
        go(0.0,2.0,0.0);
        printf("Case #%d: %.7lf\n",++temp,min);
    }
    return 0;
}
