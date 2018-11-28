#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <iostream>
#include <fstream>
#include <sstream>
#include <iomanip>
#include <utility>
#include <string>
#include <vector>
#include <stack>
#include <queue>
#include <set>
#include <map>
#include <algorithm>
#include <functional>

using namespace std;

#define uchar unsigned char
#define ushort unsigned short
#define ull unsigned ll
#define ll long long
#define ull unsigned ll

#define E 2.718281828
#define PI 3.14159265358979323846264338328

int n;
char ab0[4][5];
char ab[4][4];

bool flag;
int opt;

bool fw[4], fm[4];
int w[4], m[4];
bool mo[4];

bool machine(int l) {
	if (l == n) {
		for (int i = 0; i < n; i++)
			mo[i] = false;
		for (int i = 0; i < n; i++) {
			bool has = false;
			for (int j = 0; j < n; j++)
				if (!mo[j] && (ab[w[i]][m[j]] == '1')) {
					mo[j] = true;
					has = true;
					break;
				}
			if (!has)
				return false;
		}
		return true;
	}
	for (int i = 0; i < n; i++)
		if (!fm[i]) {
			fm[i] = true;
			m[l] = i;
			if (!machine(l + 1))
				return false;
			fm[i] = false;
		}
	return true;
}

bool worker(int l) {
	if (l == n)
		return machine(0);
	for (int i = 0; i < n; i++)
		if (!fw[i]) {
			fw[i] = true;
			w[l] = i;
			if (!worker(l + 1))
				return false;
			fw[i] = false;
		}
	return true;
}

bool good() {
	for (int i = 0; i < n; i++)
		fw[i] = fm[i] = false;
	return worker(0);
}

void solve() {
	cin >> n;
	for (int i = 0; i < n; i++)
		cin >> ab0[i];
	flag = false;
	int n2 = n * n;
	for (int comb = 0; comb < (1 << n2); comb++) {
		int coin = 0;
		for (int i = 0; i < n; i++)
			for (int j = 0; j < n; j++) {
				ab[i][j] = ab0[i][j];
				if (comb & (1 << (i * n + j))) {
					if (ab[i][j] == '0')
						coin++;
					ab[i][j] = '1';
				}
			}
		if (good()) {
			if (!flag) {
				opt = coin;
				flag = true;
			} else
				opt = min(opt, coin);
		}
		}
	cout << opt << endl;
}


int main() {
	ios::sync_with_stdio(false);
	int t;
	cin >> t;
	for (int i = 1; i <= t; i++) {
		cout << "Case #" << i << ": ";
		solve();
	}
	return 0;
}