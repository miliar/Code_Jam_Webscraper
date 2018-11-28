#include <iostream>
#include <iomanip>

using namespace std;

int main() {
	int T;
	cin >> T;
	double noFarm, withFarm, C, F, X, time, perSec;
	for (int i = 0; i < T; i++) {
		cin >> C >> F >> X;
		time = 0.0;
		perSec = 2.0;
		noFarm = X/perSec;
		withFarm = C/perSec + X/(perSec+F);
		while (withFarm < noFarm) { 
			time += C/perSec;
			perSec += F;	
			noFarm = X/perSec;
			withFarm = C/perSec + X/(perSec+F);
		}
		time += noFarm;
		cout.precision(7);
		cout << fixed << "Case #" << i+1 << ": " << time << endl;
	}
	return 0;
}
