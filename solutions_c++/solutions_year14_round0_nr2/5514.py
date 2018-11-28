#include <stdio.h>

int main(){
    
    int T, i;
    double C, F, X, ans, count;

    scanf("%d", &T);

    for (i = 0; i < T; i++){
    
        scanf("%lf %lf %lf", &C, &F, &X);
        ans = 0;
        count = 2;
        
        while(1){
            if (X / count > X/(count + F) + C / count){
                ans += C / count;
                count += F;
            }else
                break;
        }
        ans += X / count;
        printf("case #%d: %.7lf\n", i + 1, ans);   

    }

}
