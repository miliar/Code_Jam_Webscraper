#include <iostream>
//#include <string>
#include <vector>
//#include <queue>
//#include <stack>

using namespace std;

int main() {
	unsigned t;
	cin >> t;
	for (unsigned thisCase = 1; thisCase <= t; thisCase++) {
		unsigned n;
		cin >> n;
		vector<long long> plateTime;
		plateTime.resize(n);
		for (unsigned i = 0; i < n; i++) {
			cin >> plateTime[i];
		}
		cout << "Case #" << thisCase << ": ";
		// method 1
		long long mushroomsEaten = 0;
		for (unsigned i = 0; i < (n-1); i++) {
			if (plateTime[i] > plateTime[i+1]) {
				mushroomsEaten += plateTime[i] - plateTime[i+1];
			}
		}
		cout << mushroomsEaten << " ";
		// method 2
		long long maxDiff = 0;
		mushroomsEaten = 0;
		for (unsigned i = 0; i < (n-1); i++) {
			long long diff = plateTime[i] - plateTime[i+1];
			if (diff > 0 && diff > maxDiff) {
				maxDiff = diff;
			}
		}
		for (unsigned i = 0; i < (n-1); i++) {
			if (plateTime[i] - maxDiff < 0) {
				mushroomsEaten += plateTime[i];
			} else {
				mushroomsEaten += maxDiff;
			}
		}
		cout << mushroomsEaten << "\n";
	}
	return 0;
}