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
int T, n;
bool flag[12];
inline void solve() {
	scanf("%d", &T);
	for(int ii = 1; ii <= T; ii++) {
		scanf("%d", &n);
		printf("Case #%d: ", ii);
		if(n == 0) {printf("INSOMNIA\n"); continue;}
		for(int i = 0; i <= 9; i++) flag[i] = 0;
		int noww = n;
		while(1) {
			int tmp = noww;
			while(tmp) {
				flag[tmp % 10] = 1;
				tmp /= 10;
			}
			bool ok = 0;
			for(int i = 0; i < 10; i++) if(!flag[i]) {ok = 1; break;}
			if(!ok) break;
			noww += n;
		}
		printf("%d\n", noww);
	}
}
int main() {
	freopen("A.in","r",stdin);freopen("A.out","w",stdout);
	solve();
	return 0;
}
