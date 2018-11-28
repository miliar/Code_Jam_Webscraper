#include <iostream>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <algorithm>
#include <vector>

using namespace std;

bool ispal(long long x) {
	if (x < 10) return true;


	long long xuoi = x, nguoc = 0;
	while (x > 0) {
		nguoc = nguoc * 10 + x % 10;
		x /= 10;
	}

	return nguoc == xuoi;
}

vector<long long> a;

int main() {
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);

	a.clear();
	for (int i = 1; i <= 10000000; ++i) if (ispal(i)) {
		long long n = ((long long)i) * i;
		if (ispal(n)) a.push_back(n);
	}

	int ntest;
	cin >> ntest;

	long long x, y;
	for (int test = 1; test <= ntest; ++test) {
		cin >> x >> y;

		int cnt = 0;
		for (int i = 0; i < a.size(); ++i) {
			if (x <= a[i] && a[i] <= y) ++cnt;
		}

		cout << "Case #" << test << ": " << cnt << endl;
	}

	return 0;
}
