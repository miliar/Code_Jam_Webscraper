#include <iostream>
#include <algorithm>
#include <iomanip>
using namespace std;

double C,F,X;
double bestT,curR,curT;
	
int main() {
	int T; 
	cin >> T;
	for(int Z = 1; Z <= T; Z++) {
		cin >> C >> F >> X;
		curR = 2.0;
		curT = 0;
		double best = X;
		while(curT+(X/curR) < best) {
			best = curT+(X/curR);
			curT += (C/curR);
			curR += F;
		}
		cout << "Case #" << Z << ": " << fixed << setprecision(7) << best << endl;
	}
}