#include <cstdio>
#include <iostream>
#include <algorithm>
using namespace std;
int a[1010], n, b[1010];

int main() {
	int T; scanf("%d", &T);
	for(int kase = 1; kase <= T; ++kase) {
		scanf("%d\n", &n);
		for(int i = 0; i < n; ++i)  { scanf("%d", &a[i]); b[i] = a[i]; }
		int ans = 0;
		//puts("here");
		while(n > 0) {
			//printf("n = %d\n", n);
			int p = 0, m = a[0];
			for(int i = 0; i < n; ++i) {
				if(a[i] < m) {
					m = a[i]; p = i;
				}
			}
			if(abs(p - 0) == 0 || abs(p - (n-1)) == 0) {}
			else {
				ans += min(abs(p - 0), abs(p - (n-1)));
			}
			n--;
			for(int i = p; i < n; ++i) {
				a[i] = a[i+1];
			}
		}
		printf("Case #%d: %d\n", kase, ans);
	}
	return 0;
}