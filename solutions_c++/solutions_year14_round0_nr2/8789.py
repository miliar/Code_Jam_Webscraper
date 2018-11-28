#include <iostream>
#include <cstdio>

using namespace std;

double cookie_min(double R, double C, double F, double X) {
	double rate = 0;
	
	while (true) {
		if (X/R <= C/R + X/(R+F)) {
			rate += X/R;
			break;
		} else {
			rate += C/R;
			R += F;
		}
	}
	
	//if (X/R <= C/R + X/(R+F)) return X/R;
	//else return C/R + cookie_min(R+F, C, F, X);
	return rate;
}

int main(int argc, char** argv) {

	int T;
	
	cin >> T;
	
	for (int k = 0; k < T; k++) {
		
		double C, F, X;
		cin >> C >> F >> X;
		
		cout << "Case #" << (k+1) << ": ";
		printf("%.7lf", cookie_min(2, C, F, X));
		cout << endl;
		
	}

}