#include<cstdio>
inline double min(double a, double b){
    return a<b?a:b;
}

void alg(int casenum){
    double c, f, x;
    printf("CASE #%d: ", casenum);
    scanf("%lf%lf%lf", &c, &f, &x);
    double base = 0, best = x/2, bases = 0;
    while(true){
        base+=c/(2+bases*f);
        bases++;
        if(best>base+x/(2+bases*f)){
            best = base+x/(2+bases*f);
        } else{
            break;
        }
    }
    printf("%.7lf\n", best);
}

int main(){
    int n;
    scanf("%d", &n);
    for(int i=1; i<=n; i++){
        alg(i);
    }
    return 0;
}
