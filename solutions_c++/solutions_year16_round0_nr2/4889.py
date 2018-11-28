#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <algorithm>
#include <string.h>
#include <string>
#include <queue>
#include <vector>
#include <time.h>
#include <complex>
#include <map>
using namespace std;

const int MXL = 110;

int T, n, a[MXL];
char s[MXL];
inline void solve() {
	scanf("%d\n", &T);
	for(int ii = 1; ii <= T; ii++) {
		scanf("%s\n", s);
		// printf("%s\n", s);
		printf("Case #%d: ", ii); //
		n = strlen(s);
		for(int i = 0; i < n; i++) a[i] = (s[i] == '+') ? 1: 0; ///
		int noww = 1, cnt = 0;
		for(int i = n - 1; i >= 0; i--) {
			if(a[i] == noww) {
			}
			else {
				cnt++;
				noww ^= 1;
			}
		}
		printf("%d\n", cnt);
	}
}
int main() {
	freopen("B.in","r",stdin);freopen("B.out","w",stdout);
	solve();
	return 0;
}
