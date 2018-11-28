#include <iostream>
#include <string>
#include <vector>
#include <set>
#include <algorithm>
#include <iomanip>
#include "string.h"
#include "assert.h"
#include "math.h"

using namespace std;


bool rev_order(const pair<int, int> & a, const pair<int, int> & b) {
	return a.first > b.first;
}

void solve() {
	int N; cin >> N; // max shyness level
	int s[2000];
	for (int i = 0; i < N + 1; i++) {
		char c; cin >> c;
		s[i] = c - '0';
	}

	int sum = s[0];
	int extra = 0;
	for (int i = 1; i <= N; i++) {
		if (sum < i) {
			extra += (i - sum);
			sum = i;
		}
		sum += s[i];
	}
	
	cout << extra;
}


int main(int argc, char** argv) {
	int T;
	cin >> T; // number of test cases
#if 0
	char c;
	do {
		c = cin.get();
	} while (c != '\n');
#endif

	for (int i = 0; i < T; i++) {
		cout << "Case #" << i + 1 << ": ";
		solve();
		cout << endl;
	}
}

	