#include<stdio.h>
#include<string.h>
#include<stdlib.h>
#include<vector>
using namespace std;
double C, F, X;
double solve(){
    double t = 0;
    double res = 1.0e40;
    double r;
    for (int i=0; ; i++){
        r = t + X / (2 + i * F);
        if (res < r)
            return res;
        else 
            res = r;
        t += C / (2 + i * F);
    }
}
int main(){
	int T;
	scanf("%d",&T);
	for(int t=1; t<=T; t++){
        scanf("%lf%lf%lf", &C, &F, &X);
		printf("Case #%d: %.7lf\n", t, solve());
	}

}
