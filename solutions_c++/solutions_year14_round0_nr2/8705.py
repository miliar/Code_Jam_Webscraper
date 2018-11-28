#include <iostream>

using namespace std;



int main() {
	int T;
	cin >> T;
	
	cout.setf(ios::fixed);
	cout.precision(7);
	
	for (int t = 1; t <= T; ++t) {
		double C, F, X;
		cin >> C >> F >> X;
		
		double R = 2;
		double s = 0;
		
		while(X/R > (C/R + X/(R+F))) {
			s += C/R;
			R += F;
		}
		s += X/R;
		
		cout << "Case #" << t << ": " << s << endl; 
	}
}
