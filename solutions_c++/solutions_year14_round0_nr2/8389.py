#include <iostream>
#include <cmath>

using namespace std;

int main() {
	double C, F, X;
	double cost;
	int T;
	int farmCount;
	double maxFarmCount;
	cin >> T;
	for (int i = 0; i < T; i++) {
		cin >> C >> F >> X;
		maxFarmCount = (X / C - 1) - 2/F;
		farmCount = (maxFarmCount < 0)? 0 : (int)ceil(maxFarmCount);
		// Calculate the time
		cost = 0;
		for (int j = 0; j < farmCount; j++) {
			cost += C / (2 + j*F);
		}
		cost += X / (2 + farmCount*F);
		cout << "Case #" << i+1 << ": ";
		cout.precision(7);
		cout << fixed << cost << endl;
	}
	return 0;
}


