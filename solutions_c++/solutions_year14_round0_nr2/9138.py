#include <stdio.h>
#include <iostream> 
using namespace std;

double solve(double v, double c, double f, double x){
	if(x <= c ) return x/v; 
	if(c*(v+f) < x*f) {
	    return c/v + solve(v+f,c,f,x);
	}
	else return x/v;
}
int main() {
    int T;
    double C,F,X;
    cin >> T;
    for(int i=0; i<T;++i) {
    	cin >> C >> F >> X;
	double result = solve (2,C,F,X);
	printf("Case #%d: %.7lf\n",i+1,result);
    }
    return 0;
}
