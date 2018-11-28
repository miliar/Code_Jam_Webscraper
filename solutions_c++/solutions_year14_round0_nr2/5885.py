#include <iostream>
using namespace std;

void output(int num, double result){
	cout.precision(7);
	cout << "Case #" << num << ": " << fixed << result << '\n';
}

double helper(double C, double base, double F, double x){
	if(x <= C){
		return x/base;
	}else if(C*base <= F*(x-C)){
		return C/base + helper(C, base+F, F, x);
	}else{
		return x/base;
	}
}

/*
 * C: cost of a farm
 * F: rate of a farm
 * X: target
 */
double calc(double C, double F, double X){
	return helper(C, 2.0, F, X);
}

int main(){
	int T;
	double C, F, X;
	double result;
	cin >> T;
	for(int i = 0; i < T; ++i){
		cin >> C >> F >> X;
		result = calc(C, F, X);
		output(i+1, result);
	}
}