/*
 * Counting Sheep.cpp
 *
 *  Created on: Apr 9, 2016
 *      Author: Mostafa
 */
#include<bits/stdc++.h>

using namespace std;
typedef pair<int, int> ii;
typedef vector<ii> vii;
typedef vector<int> vi;
typedef long long ll;

int di[] = { 0, 0, 0, -1, 1 }, dj[] = { 0, 1, -1, 0, 0 };

int gcd(int a, int b) {
	return b == 0 ? a : gcd(b, a % b);
}

int lcm(int a, int b) {
	return a * (b / gcd(a, b));
}

int main() {
//#ifndef ONLINE_JUDGE
	freopen("A-large.in", "rt", stdin);
//#endif
	ios::sync_with_stdio(false);
	freopen("output.txt", "wt", stdout);

	int t;
	cin >> t;
	for (int tst = 1; tst <= t; tst++) {
		ll n;
		cin >> n;
		int cnt = 0, d[10], l = 0;
		ll m = n;
		if (n == 0) {
			cout << "Case #" << tst << ": INSOMNIA" << endl;
			continue;
		}
		memset(d, 0, sizeof d);
		while (cnt != 10) {
			m = n * l++;
			while (m) {
				int k = m % 10;
				m /= 10;
				if (d[k] == 0)
					cnt++;
				d[k]++;
			}
		}
		cout << "Case #" << tst << ": " << n * --l << endl;
	}
	return 0;
}
