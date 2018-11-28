#include <cstdio>
#include <algorithm>

using namespace std;

char s[110],temp[110];

inline int solve () {
	scanf ("%s", s);

	int n;
	for (n = 0;s[n] != 0;n ++) ;

	int ans = 0;
	for (int i = n-1;i >= 0;i --) {
		if (s[i] == '-') {
			if (s[0] == '+') {
				for (int j = 0;s[j] == '+';j ++) {
					s[j] = '-';
				}
				ans ++;
			}
			for (int j = 0;j <= i;j ++) {
				temp[i-j] = s[j];
			}
			for (int j = 0;j <= i;j ++) {
				if (temp[j] == '-') {
					s[j] = '+';
				} else {
					s[j] = '-';
				}
			}
			ans ++;
		}
	}
	return ans;
}

int main () {
	int t;
	scanf ("%d", &t);

	for (int i = 1;i <= t;i ++) {
		printf ("Case #%d: %d\n", i, solve ());
	}
}