#include <iostream>
#include <fstream>
#include <map>
#include <stack>
#include <queue>
#include <deque>
#include <set>
#include <cmath>
#include <vector>
#include <algorithm>
#include <string>
#include <time.h>
#include <memory.h>
#include <sstream>

using namespace std;

void fill(int n, bool *d) {
	while (n > 0) {
		d[n % 10] = true;
		n /= 10;
	}
}

bool all(bool *d) {
	for (int i = 0; i < 10; i++) {
		if (!d[i]) {
			return false;
		}
	}
	return true;
}

int lastN(int n) {
	bool d[10];
	memset(d, false, sizeof(d));
	int original = n;
	n = 0;
	do {
		n += original;
		fill(n, d);
	} while (!all(d));
	return n;
}


int main() {
	ios_base::sync_with_stdio(false);

	ifstream cin("input.txt");
	ofstream cout("output.txt");

	int tests;
	cin >> tests;
	for (int t = 1; t <= tests; t++) {
		int n;
		cin >> n;
		cout << "Case #" << t << ": ";
		if (n != 0) {
			cout << lastN(n);
		}
		else {
			cout << "INSOMNIA";
		}
		cout << endl;
	}
	

	//system("pause");
	return 0;
}