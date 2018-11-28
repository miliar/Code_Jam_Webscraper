#include <iostream>
#include <sstream>
#include <cmath>
#include <algorithm>
#include <string>
#include <string.h>
#include <cstdio>
#include <vector>
#include <map>
#include <set>
#include <cstring>
#include <queue>
#include <bitset>
#include <queue>
#include <unordered_map>


using namespace std;


int n, j;
int c[33];
long long dd[11];
long long cc[11][33];


int powm(int x, int a, int p) {
	if (a == 0) {
		return 1;
	} else {
		if (a % 2 == 0) {
			int st = powm(x, a / 2, p);
			return (1LL * st * st) % p;
		} else {
			return (1LL * powm(x, a - 1, p) * x) % p;
		}
	}
}


int delitel(long long a, int k) {
	for (int i = 2; i <= 1000000; i++) {
		if ((a % i + powm(k, n - 1, i)) % i == 0) {
			return i;
		}
	}
	return 0;
}


void get(int i) {
	if (i == n) {
		bool b = 1;
		vector<int> v;
		for (int k = 2; k <= 10; k++) {
			int a = delitel(dd[k], k);
			if (!a) {
				b = 0;
				break;
			}
			v.push_back(a);
		}	
		if (b) {
			for (int k = 0; k < n; k++) {
				cout << c[k];
			}
			cout << ' ';
			for (int k = 2; k <= 10; k++) {
				cout << v[k - 2] << ' ';
			}
			cout << endl;
			j--;	
			if (j == 0) {
				exit(0);
			}
		}
		return;
	}	
	if (i == 0 || i == n - 1) {
		c[i] = 1;
		if (i == n - 1) {
			for (int k = 2; k <= 10; k++) {
				dd[k] += cc[k][n - i - 1];
			}
		}
		get(i + 1);
		if (i == n - 1) {
			for (int k = 2; k <= 10; k++) {
				dd[k] -= cc[k][n - i - 1];
			}
		}
		return;
	}
	get(i + 1);
	c[i] = 1;
	for (int k = 2; k <= 10; k++) {
		dd[k] += cc[k][n - i - 1];
	}
	get(i + 1);
	for (int k = 2; k <= 10; k++) {
		dd[k] -= cc[k][n - i - 1];
	}
	c[i] = 0;
}


int main() {
	//freopen("output.txt", "w", stdout);
	freopen("output.txt", "w", stdout);
	int t;
	cin >> t;
	cin >> n >> j;
	for (int i = 2; i <= 10; i++) {
		cc[i][0] = 1;
		for (int jj = 1; jj <= n; jj++) {
			cc[i][jj] = cc[i][jj - 1] * i;
		}
	}
	cout << "Case #1:" << endl;
	get(0);
    return 0;
}
