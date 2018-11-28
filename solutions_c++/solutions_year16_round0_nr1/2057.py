#include <cstdlib>
#include <cmath>
#include <fstream>
#include <iomanip>
#include <iostream>
#include <queue>
#include <unordered_map>
#include <vector>
#include <sstream>
#include <set>
#include <map>
using namespace std;

int main() {
#ifdef TESTING
	ifstream cin("input.txt");
	ofstream cout("output.txt");
#endif
	int T, N;
	cin >> T;
	for (int i = 1; i <= T; i++) {
		cin >> N;
		int seen = 0, loops = 0, current;
		while (seen != (1 << 10) - 1 && loops < 10000) {
			loops++;
			current = loops * N;
			// Check digits seen
			while (current > 0) {
				seen |= 1 << (current % 10);
				current /= 10;
			}
		}

		cout << "Case #" << i << ": ";
		if (loops == 10000)
			cout << "INSOMNIA" << endl;
		else
			cout << loops * N << endl;
	}

	return 0;
}
