#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <vector>
#include <queue>
#include <map>
#include <algorithm>
#include <iostream>
#include <string>
using namespace std;

const double eps = (double)1e-9;
double R[105],C[105];

double fabs(double x){
    if(x<0) return -x;
    else    return x;
}

int main(){
    
    int T;
    scanf(" %d",&T);
    for(int t=0;t<T;t++){
        int N;
        double V,X;
        scanf(" %d %lf %lf",&N,&V,&X);
        for(int i=0;i<N;i++)
            scanf(" %lf %lf",&R[i],&C[i]);
        if(N==2 && C[0]==C[1]){
            N = 1;
            R[0] += R[1];
        }
        if(N==1){
            if(fabs(C[0]-X) > eps){
                printf("Case #%d: IMPOSSIBLE\n",t+1);
            }else{
                printf("Case #%d: %.6lf\n",t+1,V/R[0]);
            }
        }else{
            if((C[0]<X && C[1]<X) || (C[0]>X && C[1]>X)){
                printf("Case #%d: IMPOSSIBLE\n",t+1);
            }else{
                double VA = ((X-C[1])/(C[0]-C[1]))*V;
                double VB = ((X-C[0])/(C[1]-C[0]))*V;
                printf("Case #%d: %.6lf\n",t+1,max(VA/R[0],VB/R[1]));
            }
        }
    }


    return 0;
}
