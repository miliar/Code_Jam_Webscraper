#include <iostream>
#include <iomanip>

using namespace std;

int main() {

	int T;
	cin >> T;

	for(int t = 0; t < T; t++) {
		double C, F, X, cpers;
		cpers = 2;
		cin >> C >> F >> X;
		// cout << C << " " << F << " " << X << endl;
		double time = 0;
		cout << setprecision(7) << fixed;
		// cout << "test " << (C/cpers+X/(cpers+F)) << " " << X/cpers << endl;
		while((C/cpers+X/(cpers+F)) < X/cpers) {
			time += C/cpers;
			cpers += F;
			// cout << cpers << " " << time << endl;
			// cout << "test " << (C/cpers+X/(cpers+F)) << " " << X/cpers << endl;

		} 
		time += X/cpers;
		cout << "Case #" << t+1 << ": " << time << endl;
		
	}
}