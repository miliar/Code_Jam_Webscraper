#include <stdio.h>
int main(int argc, char *argv[]){
    int T;
    scanf("%d", &T);
    for(int c=1;c<=T;++c){
        double C, F, X;
        scanf("%lf%lf%lf", &C, &F, &X);
        double best_time = X/2; 
        double farm_time = 0;
        int i=0;
        while(C*F*i < X*F - 2*C){
            double total_time = farm_time + X/(2+i*F);
            if(total_time < best_time){
                best_time = total_time;
            }
            farm_time += C/(2+i*F);
            ++i;
        }
        printf("Case #%d: %0.7lf\n", c, best_time);
    }
	return 0;
}