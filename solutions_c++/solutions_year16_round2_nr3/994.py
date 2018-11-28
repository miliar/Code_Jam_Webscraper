#include <climits>
#include <cmath>
#include <iostream>
#include <map>
#include <string>
#include <vector>
using namespace std;

int pow2[17];

void init() {
	for (int i = 0; i <= 16; i++)
		pow2[i] = 1 << i;
}

int main() {
	init();
	int cases;
	cin >> cases;
	for (int caseCounter = 1; caseCounter <= cases; caseCounter++) {
		int n;
		cin >> n;

		string topic[16][2];
		for (int i = 0; i < n; i++)
			cin >> topic[i][0] >> topic[i][1];

		int sol = 0;

		for (int mask = 0; mask < pow2[n]; mask++) {
			map<string, bool> firsts;
			map<string, bool> seconds;
			for (int i = 0; i < n; i++)
				if ((mask >> i) & 1) {
					firsts[topic[i][0]] = true;
					seconds[topic[i][1]] = true;
				}

			bool possible = true;
			int fakes = 0;
			for (int i = 0; i < n; i++)
				if (((mask >> i) & 1) == 0) {
					fakes++;
					if (!firsts[topic[i][0]]) {
						possible = false;
						break;
					}
					if (!seconds[topic[i][1]]) {
						possible = false;
						break;
					}
				}

			if (possible && fakes > sol)
				sol = fakes;
		}

		cout << "Case #" << caseCounter << ": " << sol << endl;

	}
	return 0;
}
