#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <algorithm>
#include <map>
#include <string>
using namespace std;

#define N 105

int n;
char str[N];

int solve(string s) {
	int fi = 1;
	for (int i = 0; i < n; i++) {
		if (s[i] == '-') {
			fi = 0;
			break;
		}
	}
	if (fi) {
		return 0;
	}
	int r = n - 1;
	int res = 0;
	while (r >= 0) {
		int l = 0;
		while (r >= 0 && s[r] == '+') {
			r--;
		}
		int flag = 0;
		while (l <=r && s[l] == '+') {
			flag = 1;
			s[l] = '-';
			l += 1;
		}
		res += flag;

		reverse(s.begin(), s.begin() + r + 1);
		r -= l + flag;
		for (int i = r; i >= 0; i--) {
			if (s[i] == '+') {
				s[i] = '-';
			} else {
				s[i] = '+';
			}
		}
		res += 1;
		int fin = 1;
		for (int i = r; i >= 0; i--) {
			if (s[i] == '-') {
				fin = 0;
				break;
			}
		}
		if (fin) break;
	}
	return res;
}

int main() {
	int ncas;
	scanf("%d", &ncas);
	for (int cas = 1; cas <= ncas; cas++) {
		scanf("%s", str);
		n = strlen(str);
		printf("Case #%d: %d\n", cas, solve(str));
	}
	return 0;
}