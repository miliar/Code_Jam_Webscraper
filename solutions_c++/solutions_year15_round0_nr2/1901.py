#include <iostream>
#include <cmath>
#include <algorithm>
#include <vector>
using namespace std;

int total;

int calc(vector<int> &p, int msize) {
	int special = 0;
	for (int i = 0; i < p.size(); ++i) {
		if (p[i] > msize) {
			special += ceil(double(p[i])/msize)-1;
		}
	}
	total = min(total, msize+special);
}

int main() {
	int t;
	cin >> t;
	for (int c = 1; c < t+1; ++c) {
		int d;
		cin >> d;
		vector<int> p(d);
		for (int i = 0; i < d; ++i) {
			cin >> p[i];
		}
		sort(p.begin(), p.end());
		total = 1000;
		for(int i = 1; i < 1000; ++i) {
			calc(p, i);
		}
		cout << "Case #" << c << ": " << total << endl;
	}
}