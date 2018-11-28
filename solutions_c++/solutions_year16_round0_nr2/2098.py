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
	int T;
	string S;
	cin >> T;
	for (int i = 1; i <= T; i++) {
		cin >> S;
		int count = 0;
		bool up = true;
		for (int j = S.length() - 1; j >= 0; j--) {
			if (up && S[j] == '-') {
				count++;
				up = false;
			} else if (!up && S[j] == '+') {
				count++;
				up = true;
			}
		}
		cout << "Case #" << i << ": " << count << endl;
	}

	return 0;
}
