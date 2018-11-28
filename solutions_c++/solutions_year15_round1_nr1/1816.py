#include <iostream>
#include <algorithm>
#include <cstdio>
#include <vector>
#include <cstring>
#include <string>
#include <map>
#include <set>
#include <queue>
using namespace std;

const int maxn = 1024;
int a[maxn], n;
int T;

int gao1() {
	int ret = 0;
	for (int i = 1; i < n; i++) {
		if (a[i] < a[i - 1]) ret += a[i - 1] - a[i];
	}
	return ret;
}

int gao2() {
	int m = 0;
	for (int i = 1; i < n; i++){
		m = max(m, a[i - 1] - a[i]);
	}
	int ret = 0;
	for (int i = 1; i < n; i++){
		if (a[i - 1] <= a[i]) {
			ret += min(a[i - 1], m);
		}
		else {
			ret += min(a[i - 1], m);
		}
	}
	return ret;
}

int main() {
	cin >> T;
	for (int C = 1; C <= T; C++) {
		cin >> n;
		for (int i = 0; i < n; i++)
			cin >> a[i];
		cout << "Case #" << C << ": " << gao1() << " " << gao2() << endl;
	}
	return 0;
}