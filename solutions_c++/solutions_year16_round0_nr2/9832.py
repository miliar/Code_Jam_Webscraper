#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <vector>
#include <set>
#include <map>
#include <string>
#include <cstring>
#include <queue>
#include <cmath>
#include <algorithm>
#include <utility>
#include <climits>

using namespace std;

string pancakes;

int heuristic() {
	int plus[101], minus[101];
	plus[0] = 0; minus[0] = 0;
	for (int i = 0; i < pancakes.size(); i++) {
		if (pancakes[i] == '+') {
			plus[i+1] = plus[i];
			minus[i+1] = plus[i] + 1;
		} else {
			plus[i+1] = minus[i] + 1;
			minus[i+1] = minus[i];
		}
	}
	return plus[pancakes.size()];
}

void run_case(int tc) {
    cin >> pancakes;
	cout << "Case #" << tc << ": " << heuristic() << endl;
}

int main() {
	int num = 0;
	cin >> num;
	for (int i = 1; i <= num; ++i) {
		run_case(i);
	}
	return 0;
}