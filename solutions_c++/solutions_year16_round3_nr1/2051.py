#include <iostream>
#include <vector>
#include <map>
#include <string>
#include <cmath>
#include <cstdio>
#include <limits>
#include <algorithm>
#define _USE_MATH_DEFINES
#define vi vector<int>
using namespace std;
class Data {
public:
	int v, i;
	bool operator < (const Data& arg) const {
		return v > arg.v;
	}
};
int main () {
	freopen ("C:\\Vishwa\\Internet\\A-large.in", "r", stdin);
	freopen ("A-large.txt", "w", stdout);
	int T;
	cin >> T;
	for (int t = 1; t <= T; t++) {
		int n;
		cin >> n;
		int sum = 0;
		vector<Data> a (n);
		for (int i = 0; i < n; i++) {
			cin >> a[i].v;
			a[i].i = i;
			sum += a[i].v;
		}
		int runs = (sum + 1) >> 1;
		cout << "Case #" << t << ":";
		for (int i = 0; i < runs; i++) {
			sort(a.begin(), a.end());
			if (a[0].v == 0 || sum == 0)
				break;
			int i1 = a[0].i, i2 = -1;
			if (sum != 3) {
				if (a[0].v > a[1].v + 1 && a[0].v > 1) {
					i2 = a[0].i;
					a[0].v--;
					sum--;
				}
				else if (a[1].v > 0) {
					i2 = a[1].i;
					a[1].v--;
					sum--;
				}
			}
			a[0].v--;
			sum--;
			cout << " " << (char)(i1 + 'A');
			if (i2 >= 0)
				cout << (char)(i2 + 'A');
		}
		cout << endl;
	}
}