#include <bits/stdc++.h>
using namespace std;

const int MAX_H = 2500;

int main() {
	int _;
	cin >> _;
	for(int __ = 0; __ < _;) {
		cout << "Case #" << ++__ << ": ";
		int n;
		cin >> n;
		int a[2600];
		for(int h = 1; h <= MAX_H; h++) a[h] = 0;
		for(int i = 0; i < 2*n - 1; i++) {
			for(int j = 0; j < n; j++) {
				int h;
				cin >> h;
				a[h]++;
			}
		}
		for(int h = 1; h <= MAX_H; h++) {
			if(a[h] & 1) cout << h << " ";
		}
		cout << "\n";
	
	}	
	return 0;
}
