#include <stdio.h>
int main(){
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int n, i;
    double c, f, x;
    scanf("%d", &n);
    for(i=1 ; i<=n ; i++){
        double ak, dap=0, hap=0, st=2, sum=0, min=0x7fffffff;
        scanf("%lf %lf %lf", &c, &f, &x);
        min=(double)x/(double)st;
        while(sum+c<=x){
            ak=c/st;
            sum+=c;
            dap+=ak;
            st+=f;
            if(min>dap+(double)x/(double)st){
                min=dap+(double)x/(double)st;
            }
        }
        printf("Case #%d: %.7lf\n",i, min);
    }
    return 0;
}
