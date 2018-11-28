#include<cstdio>
#include<iostream>
#include<cstring>
#include<vector>
#include<algorithm>
using namespace std;
int N;
double VF,CF;
double R[110],C[110];
const double eps=1e-8;
int sgn(double x)
{
    return x<-eps?-1:x>eps;
}
int main(){
    freopen("bin.in","r",stdin);
    freopen("outb.out","w",stdout);
    int T;scanf("%d",&T);int tt = 0;
     while(T--){tt++;
        scanf("%d%lf%lf",&N,&VF,&CF);
        for(int i=0;i<N;i++){
            scanf("%lf%lf",&R[i],&C[i]);
        }printf("Case #%d: ",tt);
        if(N == 1){
            if(sgn(CF - C[0]) == 0){
                printf("%.10f\n",VF / R[0]);
            }else printf("IMPOSSIBLE\n");
        }
        else if(N == 2){
            if(CF < min(C[0],C[1])-eps || CF > max(C[0],C[1]) + eps){
                printf("IMPOSSIBLE\n");
            }
            else{
                if(sgn(C[0] - C[1]) == 0){
                    printf("%.10f\n",VF / (R[0] + R[1]));
                }else{
                    double v1 = VF*(CF - C[0])/(C[1] - C[0]);
                    double v0 = VF*(CF - C[1])/(C[0] - C[1]);
                    printf("%.10f\n",max(v0/R[0],v1/R[1]) + eps);
                }
            }
        }
     }
    return 0;
}
