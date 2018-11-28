#include <iostream>
#include <vector>
#include <fstream>
#include <algorithm>
#include <string>

using namespace std;

int main() {
	ifstream cin("input.txt");
	ofstream cout("output.txt");
	int t;
	cin >> t;
	for (int k = 0; k < t; ++k) {
		int ans = INT_MAX;
		int d;
		cin >> d;
		vector <int> p(d);
		int mx = INT_MIN;
		for (int i = 0; i < d; ++i) {
			cin >> p[i];
			mx = max(mx, p[i]);
		}
		for (int i = 1; i <= mx; ++i) {
			int count = i;
			for (int j = 0; j < d; ++j)
				if (p[j] > i)
					count += (p[j] + i - 1) / i - 1;
			ans = min(ans, count);
		}
		cout << "Case #" << k + 1 << ": " << ans << endl;
	}
}