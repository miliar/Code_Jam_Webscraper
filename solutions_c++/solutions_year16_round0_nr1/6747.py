//https://code.google.com/codejam/contest/6254486/dashboard
#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <functional>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <limits>
#include <sstream>
#include <typeinfo>

using namespace std;

typedef long long ll;

ll solve(int N)
{
	if (N == 0)
		return 0;
	set<int> digits;
	for (ll n = N; ; n += N) {
		for (ll t = n; t > 0; t /= 10) {
			digits.insert((int)(t % 10));
		}
		bool exit = true;
		for (int i = 0; i < 10; i++) {
			if (digits.find(i) == digits.end()) {
				exit = false;
				break;
			}
		}
		if (exit) {
			return n;
		}
	}
	return 0;
}

int main() {
	int T;
	cin >> T;
	for (int t = 1; t <= T; t++) {
		int N;
		cin >> N;
		auto ans = solve(N);
		if (ans == 0)
			cout << "Case #" << t << ": " << "INSOMNIA" << endl;
		else
			cout << "Case #" << t << ": " << ans << endl;

	}
	return 0;
}
