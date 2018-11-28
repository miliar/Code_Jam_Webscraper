#include <iostream>
#include <cstdio>
#include <algorithm>

using namespace std;

#define MAX_D 1000
#define INF 1000000000

int d;
int p[MAX_D];

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int tests;
	cin >> tests;
	for (int test = 1; test <= tests; ++test) {
		cin >> d;
		for (int i = 0; i < d; ++i) {
			cin >> p[i];
		}
		int bestSum = INF;
		int maxP = *max_element(p, p+d);
		for (int limit = 1; limit <= maxP; ++limit) {
			int sum = limit;
			for (int i = 0; i < d; ++i) {
				sum += p[i] / limit + (p[i] % limit ? 1 : 0) - 1;
			}
			bestSum = min(bestSum, sum);
		}
		cout << "Case #" << test << ": " << bestSum << endl;
	}
	return 0;
}
