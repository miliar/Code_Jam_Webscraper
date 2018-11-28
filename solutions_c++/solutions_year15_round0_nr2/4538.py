#include "common.hpp"

using namespace std;

int main() {
	forEachTestCase([]() {
		int d; cin >> d;
		vector<int> p(d);
		for (auto& pi : p) cin >> pi;

		int min = numeric_limits<int>::max();
		for (int eatingMinutes = 1; eatingMinutes < 10; eatingMinutes++) {
			int specialMinutes = 0;
			for (auto pi : p) {
				specialMinutes += (pi - 1) / eatingMinutes;
			}
			if (specialMinutes + eatingMinutes < min) {
				min = specialMinutes + eatingMinutes;
			}
		}

		return min;

		// int D, P = 1024;
		// cin >> D;

		// vector<int> pancakeDistribution(P);
		// for (int i = 0; i < D; i++) {
		// 	int x;
		// 	cin >> x;
		// 	pancakeDistribution[x]++;
		// }



		// int min = P, argmin = 1;
		// for (int eatingMinutes = 1; eatingMinutes < 10; eatingMinutes++) {
		// 	for (int pancakes = 0; pancakes < pancakeDistribution.size(); pancakes++) {
		// 		int diners = pancakeDistribution[pancakes];
		// 		if (diners == 0) continue;
		// 		if (pancakes <= eatingMinutes) continue;
		// 		int pancakeSum = diners * pancakes;
		// 		int neededSpecialMinutes += (pancakes * diners) / eatingMinutes - 1;

		// 		if (pancakeDistribution[j] == 0) continue;
		// 		switch (pancakeDistribution)
		// 	}
		// }

		// return min;

		// 	int x = sum % i == 0 ? sum / i - 1 + i : sum / i + i;
		// 	if (x < min) {
		// 		min = x;
		// 		argmin = i;
		// 	}
		// }

		// return 5 / 2;
		// return min;
	});
}









