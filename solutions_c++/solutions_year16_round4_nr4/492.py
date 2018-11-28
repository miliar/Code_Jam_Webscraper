#include <iostream>
#include <algorithm>
#include <string>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <stack>
#include <sstream>
#include <cmath>
#include <cstdio>
#include <cstring>
#include <cstdlib>

using namespace std;

int deter(int mask, int N, string orig) {
	int ret = 0;
	for (int i = 0; i < N; i++)
		if ((1 << i) & mask)
			ret += orig[i] != '1';
		else {
			if (orig[i] == '1')
				return -1;
		}
	return ret;
}

bool knows(int mask, int index, int j, int n) {
	int smallmask = 0;
	int sh = n * index;
	for (int i = 0; i < n; i++) {
		int bit = (mask & (1 << (sh + i)));
		if (bit)
			smallmask |= 1 << i;
	}
	return smallmask & (1 << j);
}

bool valid(int mask, int n) {
	int per[40];
	for (int i = 0; i < n; i++)
		per[i] = i;

	do {
		int DP[40][106];
		memset(DP, 0, sizeof(DP));
		DP[0][0] = 1;

		for (int i = 0; i < n; i++) {
			for (int k = 0; k < (1 << n); k++)
				if (DP[i][k]) {
					bool flag = false;
					for (int j = 0; j < n; j++)
						if (!(k & (1 << j)) && knows(mask, per[i], j, n)) {
							flag = true;
							DP[i + 1][(1 << j) | k] = 1;
						}
					if (!flag)
						return false;
				}
		}
	} while (next_permutation(per, per + n));

	return true;
}

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int t;
	cin >> t;

	for (int test = 1; test <= t; test++) {
		cout << "Case #" << test << ": ";
		int n;
		cin >> n;
		string s = "";
		for (int i = 0; i < n; i++) {
			string cur;
			cin >> cur;
			s += cur;
		}
		int N = n * n;

		int ans = N;
		for (int i = 0; i < (1 << N); i++) {
			int price = deter(i, N, s);
			if (price == -1)
				continue;
			if (valid(i, n) && price < ans)
				ans = price;				
		}

		cout << ans << endl;
	}

	return 0;
}