#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <cstdio>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
	freopen("D-small.in", "r", stdin);
	freopen("gold.out", "w", stdout);

	int t;
	cin >> t;
	for (int i = 1; i <= t; i++) {
		int x, y, z;
		cin >> x >> y >> z;
		cout << "Case #" << i << ": ";
		for (int j = 1; j <= z; j++) {
			cout << j << ' ';
		}
		cout << '\n';
	}

	return 0;
}