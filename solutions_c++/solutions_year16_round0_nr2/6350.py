#include <cstdio>
#include <cstring>
#include <iostream>
#include <cstdlib>
using namespace std;

void solve(int test) {
	char s[1000];
	cin >> s;
	char cur = s[0];
	int res = 0;
	for (int k = 1; s[k]; ++k) {
		if (s[k] == cur) continue;
		cur = s[k];
		++res;
	}
	if (cur == '-') ++res;
	printf("Case #%d: %d\n", test, res);
}

int main() {
//	freopen("test.in", "r", stdin);
//	freopen("test.our", "w", stdout);
	int testNumber;
	cin >> testNumber;
	for (int test = 1; test <= testNumber; ++test) {
		solve(test);
	}
}