#include <cstdio>

using namespace std;


int main(void){
    
    freopen("B-large.in", "r", stdin);
    freopen("out.txt", "w", stdout);
    
    int cas, c=0;
    double income, C, F, X, answer;
    
    scanf("%d", &cas);
    while( cas-- ){
        
        income = 2.0;
        answer = 0.0;
        scanf("%lf %lf %lf", &C, &F, &X);
        
        while(1){
            double build = C/income + X/(income+F);
            double not_build = X/income;
            if( build > not_build ) break;
            
            answer += C/income;
            income += F;
        }
        answer += X/income;
        printf("Case #%d: %.9lf\n", ++c, answer);
    }
    
    return 0;
}
