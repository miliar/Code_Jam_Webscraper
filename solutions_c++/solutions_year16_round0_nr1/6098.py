#include <iostream>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <cstring>
#include <vector>
#include <string>

using namespace std;

const int maxN = 110, maxLen = 1000000, oo = 23041997;

#define fo "A.txt"
#define foru(i, l, r) for (int i = l; i <= r; ++i)
#define ford(i, r, l) for (int i = r; i >= l; --i)
#define repu(i, r) for (int i = 0; i < r; ++i)
#define ll long long

int m, n, test, check[100];

int main() {
	cin >> test;
	freopen(fo, "w", stdout);
	int i = 0;
	while (test--) {
		cin >> n;
		++i;
		int num = 0;
		int m = n;
		cout << "Case #" << i << ": ";
		if (n) {
			while (num != 10) {
				int temp = m;
				while (temp) {
					if (check[temp % 10] != test + 1) check[temp % 10] = test + 1, num++;
					temp /= 10;
				}
				m += n;
			}
			cout << m - n << endl;
		}
		else cout << "INSOMNIA\n";
	}
}