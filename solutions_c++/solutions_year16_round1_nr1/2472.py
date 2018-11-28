#include <bitset>
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
	cin >> T;
	for (int caso = 1; caso <= T; caso++) {
		string S, R;
		cin >> S;
		R.push_back(S[0]);
		for (int i = 1; i < S.length(); i++) {
			if (S[i] >= R[0])
				R = string(1, S[i]) + R;
			else
				R.push_back(S[i]);
		}
		cout << "Case #" << caso << ": " << R << endl;
	}
	return 0;
}
