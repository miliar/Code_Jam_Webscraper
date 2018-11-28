#include<iostream>
using namespace std;

int f(int x, int d) {
	int result = 1;
	for (; x; x = (x - 1) >> 1, --d) {
		result += 1 << d;
	}
	return result;
}

int g(int x, int d) {
	int result = 1;
	for (; d >= 0; --d) {
		if (!x) {result += 1 << d;}
		else {x = (x - 1) >> 1;}
	}
	return result;
}

int main() {
	const int N = 1024 + 32;
	int T, lowest[N], highest[N], cas = 0;
	for (cin >> T; T; --T) {
		int n, m;
		cin >> n;
		m = 1 << n;
		for (int i = 0; i < m; ++i) {
			lowest[i] = f(i, n - 1);
		}
		for (int i = 0; i < m; ++i) {
			highest[i] = g(m - 1 - i, n - 1);
		}
		int x, y, p;
		cin >> p;
		for (int i = 0; i < m; ++i) {
			if (lowest[i] <= p) {x = i;}
			if (highest[i] <= p) {y = i;}
		}
		cout << "Case #" << ++cas << ": " << x << " " << y << endl;
	}
	return 0;
}
