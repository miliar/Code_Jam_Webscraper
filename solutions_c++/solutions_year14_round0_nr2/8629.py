#include<iostream>
#include<cmath>
#include<iomanip>
using namespace std;

int main() {
	int t, a;
	double C, F, X, res;
	
	cin >> t;
	for(int TCASE = 0; TCASE < t; TCASE++) {
		cin >> C >> F >> X;
		a = (int)floor((X*F - 2*C) / (C*F) );
		if(a < 0)
			a = 0;
		
		res = 0;
		for(int i=0;i<a;i++)
			res += C / (2 + i*F);
		res += X / (2 + a*F);
		
		cout << fixed << setprecision(7) << "Case #" << TCASE + 1 << ": " << res << '\n';
	}
	
	return 0;
}
