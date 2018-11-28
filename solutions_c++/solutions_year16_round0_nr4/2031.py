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
#include <gmpxx.h>
using namespace std;
typedef long long ll;

int main() {
#ifdef TESTING
	ifstream cin("input.txt");
	ofstream cout("output.txt");
#endif
	int T, K, C, S;
	cin >> T;
	for (int i = 1; i <= T; i++) {
		cin >> K >> C >> S;
		cout << "Case #" << i << ":";
		int students_needed = ceil((double)K / C);
		if (S < students_needed) {
			cout << " IMPOSSIBLE" << endl;
		} else {
			int group = 0;
			for (int j = 0; j < students_needed; j++) {
				int exp = C - 1;
				mpz_class sum, power;
				while (exp >= 0 && group < K) {
					mpz_ui_pow_ui(power.get_mpz_t(), K, exp);
					sum += power * group;
					exp--, group++;
				}
				cout << " " << sum + 1;
			}
			cout << endl;
		}
	}
	return 0;
}
