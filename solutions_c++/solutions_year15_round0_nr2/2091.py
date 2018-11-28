#include <iostream>
#include <cstdlib>
#include <cstdio>
#include <string>
#include <cstring>
#include <algorithm>

using namespace std;

int T, D, p[1005];

int main(int argc, char** argv) {
	freopen("b.in", "r", stdin);
	freopen("b.out", "w", stdout);
	scanf("%d", &T);
	
	for (int times = 1; times <= T; times ++) {
		printf("Case #%d: ", times);
		scanf("%d", &D);
		int max = 0;
		for (int i = 0; i < D; i ++) {
			scanf("%d", &p[i]);
			if (p[i] > max) max = p[i];
		}
		
		int ans = max + 1, now;
		for (int i = 1; i <= max; i++) {
			now = i;
			for (int j=0; j < D; j++) now += (p[j] - 1) / i;
			if (now < ans) ans = now;
		}
		printf("%d\n", ans);
	}
	return 0;
}

