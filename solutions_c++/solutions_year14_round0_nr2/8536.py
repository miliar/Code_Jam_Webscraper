#include <iostream>
#include <cstdio>

using namespace std;


double solve(double R, double C, double F, double X) {
	double a = X/R;
	double b = C/R + X / (R+F);
	if (b < a) {
		return C/R + solve(R+F, C, F, X);
	} else {
		return a;
	}

}

int main() {
	int T;
	cin>>T;
	for (int t=1;t<=T;++t) {
		double C, F, X;
		cin>>C>>F>>X;

		double ans = solve(2, C, F, X);

		printf("Case #%d: %.9lf\n", t, ans);
	}
}
