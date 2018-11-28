#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <cmath>

using namespace std;

int t, ans;
string s;
char a, b;

int main() {
	freopen("B-large.in", "r", stdin); freopen("output.out", "w", stdout);
	cin >> t;

	for (int i = 1; i <= t; ++i) {
		cin >> s;
		ans = 0;
		a = '-';
		b = '+';
		for (int j = s.size() - 1; j >=0; --j) {
			if (s[j] == a) {
				++ans;
				swap(a, b);
			}
		}
		cout << "Case #" << i << ": " << ans << endl;
	}

    return 0;
}