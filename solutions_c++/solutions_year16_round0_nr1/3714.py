#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <cctype>
#include <cassert>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <queue>
#include <stack>
#include <list>
#include <map>
#include <set>
#include <algorithm>
#include <utility>

using namespace std;

void solveSingleCase() {
	int N;
	cin >> N;

	if (N == 0) {
		cout << " INSOMNIA" << endl;
		return;
	}

	set <int> seenDigits;
	for (int i=1; true; ++i) {
		long long number = N * (long long)i;
		long long temp = number;
		while (temp > 0) {
			seenDigits.insert(temp % 10);
			temp /= 10;
		}
		if (seenDigits.size() == 10) {
			cout << " " << number << endl;
			return;
		}
	}
}

int main() {
	int T;
	cin >> T;

	for (int i = 1; i <= T; ++i) {
		cout << "Case #" << i << ":";
		solveSingleCase();
	}
	
	return 0;
}
