#include <iostream>
#include <algorithm>
#include <cmath>
#include <vector>

using namespace std;

int main() {
	int nTests, test;
	cin >> nTests;
	for (int test = 1; test <= nTests; ++test) {
		int nDiners;
		cin >> nDiners;
		vector<int> p(nDiners);
		int maxP = 0;
		for (int i = 0; i < nDiners; ++i) {
			cin >> p[i];
			maxP = max(maxP, p[i]);
		}
		int best = maxP;
		for (int normalMinutes = 1; normalMinutes <= maxP; ++normalMinutes) {
			int tmp = normalMinutes;
			for (int i = 0; i < nDiners; ++i) {
				tmp += (p[i] - 1) / normalMinutes;
			}
			best = min(best, tmp);
		}
		cout << "Case #" << test << ": " << best << endl;
	}
	return 0;
}
