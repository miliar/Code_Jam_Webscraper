#define _CRT_SECURE_NO_WARNINGS

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
#include <limits.h>

using namespace std;

int main() {
	//ios_base::sync_with_stdio(false);

	ifstream cin("input.txt");
	ofstream cout("output.txt");


	int tests;
	cin >> tests;
	for (int test = 1; test <= tests; test++) {
		int n, k;
		cin >> n >> k;
		vector<double> p(n);
		for (int i = 0; i < n; i++) {
			cin >> p[i];
		}
		double ans = 0;
		for (int mask = 0; mask < (1 << n); mask++) {
			int ones = 0;
			vector<int> d(n, 0);
			int cur = mask;
			int pos = 0;
			while (cur > 0) {
				d[pos++] = cur % 2;
				ones += cur % 2;
				cur /= 2;
			}
			if (ones == k) {
				vector<int> ids;
				for (int i = 0; i < n; i++) {
					if (d[i] == 1) {
						ids.push_back(i);
					}
				}
				double tieProb = 0;
				for (int vote = 0; vote < (1 << k); vote++) {
					double prob = 1;
					int cur = vote;
					int zeros = 0;
					for (int pos = 0; pos < k; pos++) {
						if (cur % 2 == 0) {
							zeros++;
							prob *= (1 - p[ids[pos]]);
						} else {
							prob *= p[ids[pos]];
						}
						cur /= 2;
					}
					if (zeros == k / 2) {
						tieProb += prob;
					}
				}
				if (tieProb > ans) {
					ans = tieProb;
				}
			}
		}
		cout << "Case #" << test << ": ";
		cout.precision(8);
		cout << fixed << ans << endl;
	}

	//system("pause");
	return 0;
}