#include <bits/stdc++.h>
using namespace std;

int n_test;
string a, b, x, y, optX, optY;

long long evaluate(string x, string y) {
	long long X, Y;
	stringstream ss;
	ss << x << " " << y;
	ss >> X >> Y;
	return abs(X - Y);
}

void complete(string a, string b, string x, string y, string &optX, string &optY, int i) {
	for (; i < a.length(); ++i) {
		if (a[i] == '?') x[i] = '0';
		if (b[i] == '?') y[i] = '9';
	}
	if (optX == "" || make_pair(evaluate(x, y), min(x, y)) < make_pair(evaluate(optX, optY), min(optX, optY))) {
		optX = x;
		optY = y;
	}
}

void solve(string a, string b, string &optX, string &optY) {
	x = a;
	y = b;
	for (int i = 0; i < a.length(); ++i) {
		if (a[i] == '?' && b[i] == '?') {
			x[i] = '1';
			y[i] = '0';
			complete(a, b, x, y, optX, optY, i + 1);
			x[i] = y[i] = '0';
		} else if (a[i] == '?') {
			x[i] = y[i] == '9' ? '9' : y[i] + 1;
			complete(a, b, x, y, optX, optY, i + 1);
			x[i] = y[i];
		} else if (b[i] == '?') {
			y[i] = x[i] == '0' ? '0' : x[i] - 1;
			complete(a, b, x, y, optX, optY, i + 1);
			y[i] = x[i];
		} else {
			complete(a, b, x, y, optX, optY, i + 1);
		}
	}
	complete(a, b, x, y, optX, optY, a.length());
}

int main() {
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);
	cin >> n_test;
	for (int test = 1; test <= n_test; ++test) {
		cin >> a >> b;
		optX = "";
		optY = "";
		solve(a, b, optX, optY);
		solve(b, a, optY, optX);
		cout << "Case #" << test << ": " << optX << " " << optY << endl;
	}

	return 0;
}
