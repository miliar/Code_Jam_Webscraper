

#include <stdio.h>
#include <algorithm>

using namespace std;


int T;

int main() {
    
    scanf("%d",&T);
    
    for (int case_number=1;case_number<=T;case_number++){
        
        int N;
        long double V,X;
        
        long double R[105];
        long double C[105];
        
        scanf("%d %Lf %Lf",&N,&V,&X);
        
        for (int i=0;i<N;i++) scanf("%Lf %Lf",&R[i],&C[i]);
        
        //int r1=R[0]*10000;
        //int r2=R[1]*10000;
        
    
        if (N==2){
        
        int c1=C[0]*10000;
        int c2=C[1]*10000;
            if (c1!=c2){
        
        int T=X*10000;
            
            
        
        if (min(c1,c2)>T||T>max(c1,c2)) {
            printf("Case #%d: IMPOSSIBLE\n",case_number);
            continue;
        }
        
        long double f= (X-C[1])/(C[0]-C[1]);
        
        long double answer = (V*f)/R[0];
        
        if ((V*(1-f))/R[1]>answer) answer=(V*(1-f))/R[1];
        
                printf("Case #%d: %.7Lf\n",case_number,answer); } else {
                    
                    N=1;
                    R[0]=R[0]+R[1];
                }
        }
        
        
        if (N==1){
            
            int c1=C[0]*10000;
            
            int T=X*10000;
            
            if (T!=c1) {
                printf("Case #%d: IMPOSSIBLE\n",case_number);
                continue;
            }
            
            printf("Case #%d: %.7Lf\n",case_number,V/R[0]);
            
            
            
        }
        
    }

    return 0;
}
