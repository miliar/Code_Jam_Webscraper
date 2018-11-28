#include <cstdio>
#include <iostream>
#include <algorithm>
#include <vector>
#include <set>

using namespace std;

typedef pair<int, int> ii;


double C, F, X;
double prec = 1e-8;
double dp(double rate){
	double tg = X/rate;
	double th = C/rate;

	if(tg < th+X/(rate+F)) return tg;
	else return min(tg, th+dp(rate+F));
}
int main(){
	int t; scanf("%d", &t);
	for(int cas=1;cas<=t;cas++){
		scanf("%lf %lf %lf", &C, &F, &X); //C = house cost, F = house production, X = goal
		double tim = dp(2.0);
		printf("Case #%d: %.8f\n", cas, tim);
	}

}