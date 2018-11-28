#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

inline bool buy(const double& C, const double& F, const double& X, double P) {
	double nobuyt = X/P;
	double buyt (0.0);
	buyt += C/P;
	P += F;
	buyt += X/P;
	
	return buyt<nobuyt;
}

int main() {
	ios::sync_with_stdio(false);
	cout<<fixed;
	cout.precision(7);
	int T;
	cin>>T;
	for(int cases = 1; cases<=T; cases++) {
		double t(0.0);
		double P(2.0);
		double C, F, X;
		cin>>C>>F>>X;
		
		while(buy(C,F,X,P)) {
			t += C/P;
			P += F;
		}
		t += X/P;
		
		cout<<"Case #"<<cases<<": "<<t<<'\n';
	}	
}
