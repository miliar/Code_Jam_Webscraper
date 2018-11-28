#include <fstream>
#include <iostream>
#include <set>
#include <iostream>
#include <iomanip>

using namespace std;

double getTime(double farmPrice, double farmGain, double target, int farmCount) {
	double currentTime = 0;
	double currentGain = 2;	

	for (int i = 0; i < farmCount; i++) {
		currentTime += farmPrice / currentGain;
		currentGain += farmGain;
	}

	return currentTime + target / currentGain;
}

int main() {
	ifstream in("input.txt");
	ofstream out("output.txt");

	int T;
	in >> T;	

	for (int t = 0; t < T; t++) {
		double farmPrice;
		double farmGain;
		double target;

		in >> farmPrice >> farmGain >> target;	
		// for (int i = 0; i < 5; i++) {
		// 	out << setprecision(9) << getTime(farmPrice, farmGain, target, i) << " ";
		// }

		double ans = getTime(farmPrice, farmGain, target, 0);
		int farmCount = 1;
		while (getTime(farmPrice, farmGain, target, farmCount) < ans) {
			ans = getTime(farmPrice, farmGain, target, farmCount);
			farmCount++;
		}
		out << "Case #" << t + 1 << ": " << setprecision(9) << ans;
		out << endl;
	}
	return 0;
}
