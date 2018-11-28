#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <string.h>
#include <ctype.h>
#include <iostream>
#include <vector>
#include <stack>
#include <queue>
#include <set>
#include <map>
#include <string>
#include <algorithm>
#include <iostream>
using namespace std;

const int N = 1e6;
#define MP make_pair
#define lli long long int

bool used[20];

lli solve(lli v) {
	memset(used, 0, 20 * sizeof(bool));
	int cnt = 0;
	for (lli i = 1; i <= 10000000; ++i) {
		lli n = v*i;
		while (n) {
			int k = n % 10;
			if (!used[k]) {
				used[k] = 1;
				++cnt;
			}
			n /= 10;
		}
		if (cnt == 10) return v * i;
	}
	return -1;
}

int main() {

	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	/*
	for (int i = 1; i <= 100000; ++i)
		cout << i << ' ' << solve(i) << endl;
	return 0;*/
	int T;
	cin >> T;
	for (int qq = 0; qq < T; ++qq) {
		cout << "Case #" << qq + 1 << ": ";
		lli t;
		cin >> t;
		lli res = solve(t);
		if (res == -1) cout << "INSOMNIA";
		else cout << res;
		cout << endl;
	}
}