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
	freopen("B-large.in", "r", stdin);
	freopen("output.txt", "w", stdout);

	int T;
	cin >> T;
	for (int t = 0; t < T; t++) {
		int N;
		cin >> N;
		vector<int> a(N + 10, 0);
		for (int i = 0; i < N; i++)
			cin >> a[i];
		long long ans = 1e18;
		for (int i = 1; i <= 1000; i++) {
			long long sum = 0;
			for (int j = 0; j < N; j++) {
				sum += (a[j] - 1) / i;
			}
			sum += i;
			ans = min(ans, sum);
		}
		cout << "Case #" << t + 1 << ": " << ans << endl;
	}
	return 0;
}