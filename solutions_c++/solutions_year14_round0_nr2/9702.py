#include <cstdio>
#include <cfloat>

using namespace std;

double C, F, X;
double mini;

double memo[10004][10004];

double min(double a, double b){
    if(a < b)
        return a;
    return b;
}
    
double f(double acum, double factor, double tiempo, int NC, int NF){
    if(tiempo > mini) { return DBL_MAX; }
    if(acum + C > X){
        double b = tiempo + (X - acum) / factor;
        mini = min(mini, b);
        return mini;
    } 
    /*if(factor > 50) {
        double b = tiempo +  (X / factor); 
        if(b < mini)
            mini = b;
        return mini;
    }*/
    
    if( memo[NC][NF] > mini ){
        f(0, factor+F, tiempo + (C / factor), 0, NF + 1);
        f(acum + C, factor, tiempo + (C / factor), NC + 1, NF);
        memo[NC][NF] = mini;
    }
}

void limpia(){
    for(int i = 0; i < 10000; i++)
        for(int j = 0; j < 10000; j++)
            memo[i][j] = 1000000.0f;
}

int main(){
    int T;
    scanf("%d", &T);
    for(int i = 0; i < T; i++){
        limpia();
        scanf("%lf  %lf %lf", &C, &F, &X);
        mini = X / 2.0f;
        //printf("Recibido %lf %lf %lf %lf\n", C, F, X, mini);
        double res = f(0, 2, 0, 0, 0);
        
        printf("Case #%d: %.7lf\n", i + 1, mini);
    }
    
    return 0;
}
