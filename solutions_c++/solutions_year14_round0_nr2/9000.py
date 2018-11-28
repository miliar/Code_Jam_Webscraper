#include <iostream>
#include <iomanip>
using namespace std;

double solve(double C,double F, double X){
	double r=2.;
	double t=0.;
	double best=X/r;
	while(t<best){
		t+=C/r;
		r+=F;
		best=min(best,t+X/r);
	}
	return best;
}

int main(){
	int T;
	cin >> T;
	for(int t=0;t<T;t++){
		cout << "Case #" << t+1 << ": ";
		double C,F,X;
		cin >> C >> F >> X;
		cout << fixed << setprecision(7) << solve(C,F,X) << "\n";
	}
	
	return 0;
}
