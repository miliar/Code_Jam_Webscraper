#include<stdio.h>
#include<stdlib.h>
int N;
double V,X;
double r[121], c[121];
double abs(double a){
    return a > 0 ? a : -a;
}
double max(double a, double b){
    return a > b ? a : b;
}
double min(double a, double b){
    return a < b ? a : b;
}
bool equal(double a, double b){
    double q = abs(a - b);
    if(q < 1e-10)return true;
    return false;
}
int main(){
    int T;
    scanf("%d",&T);
    for(int ca = 0; ca < T ; ca++){
        scanf("%d %lf %lf",&N,&V,&X);
        //printf("%d %lf %lf\n",N,V,X);
        for(int i=0;i<N;i++){
            scanf("%lf %lf",&r[i],&c[i]);
            //printf("%lf %lf\n",r[i],c[i]);
        }
        printf("Case #%d: ", ca + 1);
        if(N == 1){
            //if(equal(X, c[0])){
            if(X == c[0]){
                printf("%.9lf\n",V / r[0] );
            }else{
                printf("IMPOSSIBLE\n");
            }
            continue;
        }
        //if((c[0] - X) * (c[1] - X) > 0.0 && !equal((c[0] - X) * (c[1] - X), 0.0)){
        if((c[0] - X) * (c[1] - X) > 0.0){
            printf("IMPOSSIBLE\n");
            continue;
        }
        //if(equal(c[0],X) && equal(c[1],X)){
        if(c[0] == X && c[1] == X){
            printf("%.9lf\n",V / (r[0] + r[1]));
            continue;
        }
        if(c[0] == X || c[1] == X){
            if(c[0] == X){
                printf("%.9lf\n",V / r[0]);
            }else{
                printf("%.9lf\n",V / r[1]);
            
            }
            continue;
        }
        //double v0 = V * (c[1] - X) / (c[1] - c[0]);
        double v0 = V * (c[1] - X) / (c[1] - c[0]);
        //double v1 = V * (c[0] - X) / (c[0] - c[1]);
        double v1 = V * (c[0] - X) / (c[0] - c[1]);
        double m0 = v0 / r[0];
        double m1 = v1 / r[1];
        printf("%.9lf\n",max(m0,m1));
    }
    return 0;
}
