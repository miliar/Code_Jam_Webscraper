#include <iostream>
#include <cstdlib>
#include <cstdio>
#include <algorithm>

using namespace std;

int T, S;
string x;

int main() {
	freopen("A.in", "r", stdin);
	freopen("A.out", "w", stdout);
	cin >> T;
	for (int z = 1; z <= T; z++) {
		cout << "Case #" << z << ": ";
		cin >> S >> x;
		int cur = x[0] - '0';
		int res = 0;
		for (int i = 1; i < x.length(); i++) {
			if (cur < i) {
				res += i - cur;
				cur = i;
			}
			cur += x[i] - '0';
		}
		cout << res << endl;
	}
}
