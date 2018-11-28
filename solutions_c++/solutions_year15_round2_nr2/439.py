#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cfloat>
#include <cmath>
#include <algorithm>
#include <vector>
#include <map>
#include <set>

using namespace std;

#define FOR(i,a,b) for (int i = (a); i < (b); i++)
#define pb push_back
#define mp make_pair
int orCalc(int r, int c, int n) {
	int total = r * c;
	int machbar = (total+1) / 2 - 1;
	n -= machbar;
		
	int un = 0;
	if (4 >= n) {
		return 2 * n;
	}
	n -= 4;
	un += 2 * 4;
	int rp = 2 * (r / 2) + 2 * (c / 2) - 4;
	if (rp >= n) {
		return 3 * n + un;
	}
	n -= rp;
	un += 3 * rp;
	
	un += 4 * n;
	return un;
}
int main() {
	int tc;
	cin >> tc;
	for (int t = 0; t < tc; t++) {
		int r, c, n, norig;
		cin >> r >> c >> n;
		int total = r * c;
		norig = n;
		int machbar = (total+1) / 2;
		if (n <= machbar) {
			cout << "Case #" << t+1 << ": " << 0 << endl;
		} else {
			int un = 0;
			n -= machbar;
			if (r == 1 && c == 1) {
				cout << "Case #" << t+1 << ": " << 0 << endl;
			} else if (r == 1 || c == 1) {
				r = max(r, c);
				c = 1;
				if (r % 2 == 0) {
					n--;
					un += 1;
				}
				un += 2 * n;
				cout << "Case #" << t+1 << ": " << un << endl;
			} else {
				// corners:
				int ab =  0;
				if (r % 2 == 0 || c % 2 == 0) {
					if (n >= 2) {
						n -= 2;
						un += 4;
					} else {
						n -= 1;
						un += 2;
					}
					ab = 2;
				}
				// border
				int poss = 0;
				if (r % 2 == 0 && c % 2 == 0) {
					poss = (r + c) - 4;
				} else if (r % 2 == 0) {
					poss = (c / 2) + (c / 2 - 1) + r / 2 - 1 + r / 2 - 1;
				} else if (c % 2 == 0) {
					poss = (r / 2) + (r / 2 - 1) + c / 2 - 1 + c / 2 - 1;
				} else {
					poss = 2 * (c / 2) + 2 * (r / 2);
				}
			
				if (n <= poss) {
					un += 3 * n;
					n = 0;
				} else {
					n -= poss;
					un += 3 * poss;
				}
			
				// middle
				un += 4 * n;
				if (r % 2 == 1 && c % 2 == 1) un = min(un, orCalc(r, c, norig));
				cout << "Case #" << t+1 << ": " << un << endl;
			}
		}
	}
	return 0;
}
