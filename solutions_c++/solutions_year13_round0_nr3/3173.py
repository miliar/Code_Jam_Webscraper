#include <iostream>
#include <string>
#include <cmath>
using namespace std;

int pol(string p) {
	int res = 1;
	int len = p.length();
	for (int i=0; i<len; ++i) {
		if (p[i] != p[len-1-i]) {
			res = 0;
			break;
		}
	}
	return res;
}

int main() {
	int t;
	int ans[5] = {1, 4, 9, 121, 484};
	cin >> t;
	for (int i=0; i<t; ++i) {
		int a, b, res = 0;
		cin >> a >> b;
		for (int j=0; j<6; ++j) {
			if (ans[j]>=a && ans[j]<=b) {
				++res;
			}
		}
		cout << "Case #" << i+1 << ": " << res << endl;
	}
}
