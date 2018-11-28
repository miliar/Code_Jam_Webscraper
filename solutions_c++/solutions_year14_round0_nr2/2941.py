#include <cstdio>
#include <cstdlib>
double min(double a, double b){
	return a > b ? b : a;
}
int main(){
    int t;
    //freopen("in", "r", stdin);
    //freopen("out", "w", stdout);
    scanf("%d", &t);
    for(int ct = 1;ct <= t; ct++){
        double C, F, X, rate = 2.0, now = 0, ans = 1e10, time = 0;
		scanf("%lf%lf%lf", &C, &F, &X);
		int factory = 100001;
		for(int i = 0; i < factory; i++){
			ans = min(ans, time+ X / rate);
			time = time + C / rate;
			rate = rate + F;
		}
		printf("Case #%d: %.7lf\n", ct, ans);
    }
    return 0;
}
