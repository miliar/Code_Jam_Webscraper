#include <cstdio>
#include <iostream>
#include <vector>
#include <string>
#include <set>
#include <map>
#include <queue>
#include <cstring>
#include <cstdlib>
#include <algorithm>

using namespace std;

struct BigNum {
	char str[101];
	BigNum() {
		str[0] = 0;
	}
	BigNum(int x) {
		sprintf(str, "%d", x);
	}
	BigNum(int len, int k) {
		for(int i = 0; i < len; ++i) {
			str[i] = i + 1 + '0';
		}
		for(int i = 0; i < len - 1; ++i) {
			str[i + len] = len - i - 1 + '0';
		}
		str[len * 2 - 1] = 0;
	}
	void input() {
		scanf("%s", str);
	}
	bool operator <=(const BigNum &a) const {
		if(strlen(str) < strlen(a.str)) {
			return true;
		} else if(strlen(str) > strlen(a.str)) {
			return false;
		} else {
			return strcmp(str, a.str) <= 0;
		}
	}
};
int solve() {
	BigNum a, b;
	a.input();
	b.input();
	int ans = 0;
	{
		BigNum c(4);
		if(a <= c && c <= b) {
			++ ans;
			//cout << c.str << endl;
		}
	}
	{
		BigNum c(484);
		if(a <= c && c <= b) {
			++ ans;
			//cout << c.str << endl;
		}
	}
	{
		BigNum c(9);
		if(a <= c && c <= b) {
			++ ans;
		}
	}
	for(int i = 1; i < 10; ++i) {
		BigNum c(i, 1);
		if(a <= c && c <= b) {
			++ ans;
			//cout << c.str << endl;
		}
	}
	cout << ans << endl;
	return 0;
}

int main() {

	int T;
	freopen("C-small-attempt0.in", "r", stdin);
	freopen("C.out", "w", stdout);
	cin >> T;
	for (int t = 1; t <= T; ++t) {
		cout << "Case #" << t << ": ";
		solve();
	}
}
