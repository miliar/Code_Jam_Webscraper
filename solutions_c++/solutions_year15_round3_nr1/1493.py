#define _CRT_SECURE_NO_WARNINGS

#include <stdio.h>
#include <algorithm>
#include <fstream>
#include <vector>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <string>
#include <utility>
#include <iomanip>
#include <iostream>
#include <cmath>
#include <bitset>
#include <time.h>
#include <iterator>

using namespace std;

int main() {
	freopen("A-small-attempt0 (1).in", "r", stdin);
	freopen("output.txt", "w", stdout);

	int T;
	cin >> T;
	for (int t = 1; t <= T; t++) {
		int R, C, W;
		cin >> R >> C >> W;
		cout << "Case #" << t << ": " << (C + W - 1) / W * (R - 1) + (C + W - 1) / W + (W - 1) << endl;
	}
	return 0;
}