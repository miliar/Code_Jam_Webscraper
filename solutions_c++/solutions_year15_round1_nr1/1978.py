#include <iostream>
#include <cstdlib>
#include <cstdio>
#include <vector>
#include <algorithm>

using namespace std;

int solve(vector<int> v) {
	int n = v.size();
	int r = 0;
	int s = 0;
	int diff = 0;
	int minr = 0;
	for (int i = 1; i < n; i++) {
		if (v[i] < v[i - 1]) {
			diff = -v[i] + v[i - 1];
			r += diff;	
			if (diff > minr) {
				minr = diff;
			}
		}
	}
	for (int i = 0; i < n - 1; i++) {
		if (v[i] < minr) {
			s += v[i];
		} else {
			s += minr;
		}
	//	cout << "s " << s << endl;
	}
	cout << r << " " << s;
	return 0;
}

int main() {
	int nt;
	cin >> nt;
	int n;
	for (int i = 0; i < nt; i++) {
		cin >> n;
		vector<int> v(n);
		for (int j = 0; j < n; j++) {
			cin >> v[j];
		}
		cout << "Case #" << i + 1 << ": ";
		solve(v);
		cout << endl;
	}
	return 0;
}
