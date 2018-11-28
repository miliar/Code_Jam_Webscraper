#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <cmath>
#include <memory.h>
#include <vector>
#include <queue>
#include <deque>
#include <string>
#include <stack>
#include <ctime>
#include <set>
#include <map>
#include <list>
#include <memory.h>

using namespace std;

void solve() {
	int n, m, x;
	bool a[10];
	for (int i = 0; i < 10; ++i) {
		a[i] = false;
	}
	cin >> n;
	if (n == 0) {
		cout << "INSOMNIA" << endl;
		return;
	}
	m = n;
	while (true) {
		x = m;
		while (x > 0) {
			a[x % 10] = true;
			x /= 10;
		}
		bool f = true;
		for (int i = 0; i < 10; ++i) {
			if (!a[i]) {
				f = false;
			}
		}
		if (f) {
			cout << m << endl;
			return;
		}
		m += n;
	}
}

int main() {
	freopen("input.txt", "r", stdin); freopen("output.txt", "w", stdout);
	
	int n;
	cin >> n;
	for (int i = 0; i < n; ++i) {
		cout << "Case #" << i + 1 << ": ";
		solve();
	}
	
	return 0;
}

