#include <iostream>

using namespace std;

double cookies(double c, double s, double f, double x){

	double directTime = x / s;
	double farmTime = c / s;

	if ( directTime < farmTime +  x / (s+f)){
		return directTime;
	} else {
		return farmTime + cookies(c, s+f, f, x);
	}
}

int main(int argc, char const *argv[]){
	int nCase;
	cin >> nCase;
	for ( int k = 0; k < nCase; ++k ){
		double c, f, x;
		cin >> c >> f >> x;
		double s = 2.;
		double ans = cookies(c, s, f, x);
		printf("Case #%d: %.7f\n", k+1, ans);
	}
	return 0;
}