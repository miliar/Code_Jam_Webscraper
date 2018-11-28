#include <iostream>
#include <string>
#include <vector>
#include <set>
#include <algorithm>
#include <iomanip>
#include <queue>
#include "string.h"
#include "assert.h"
#include "math.h"

using namespace std;

void solve() {
	string str; getline(cin, str);
	int l = str.length();
	bool seen[1000];
	pair<char, int> a[1000];

	for (int i = 0; i < l; i++) {
		seen[i] = false;
		a[i].first = str[i];
		a[i].second = i;
	}
	sort(a, a + l);

	int lastPos = l - 1;
	for (int k = l - 1; k >= 0; k--) {
		int pos = a[k].second;
		if (pos > lastPos)
			continue;
		cout << a[k].first;
		seen[pos] = true;
		lastPos = pos;
	}

	for (int i = 0; i < l; i++) {
		if (!seen[i])
			cout << str[i];
	}
}

int main(int argc, char** argv) {
	int T;
	cin >> T; // number of test cases
	string s; getline(cin, s);
	for (int i = 0; i < T; i++) {
		cout << "Case #" << i + 1 << ": ";
		solve();
		cout << endl;
	}
}

	