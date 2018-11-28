#include <cstdio>
#include <cstring>
#include <string>
#include <map>
#include <set>
#include <utility>
#include <vector>
#include <algorithm>
#include <cstdint>
#include <cmath>
#include <iostream>
using namespace std;
const int maxn = 10001;
int n, x;
int s[maxn];
bool v[maxn];

void init() {
	scanf("%d%d", &n, &x);
	for (int i = 1; i <= n; i++) {
		scanf("%d", &s[i]);
	}
	sort(s + 1, s + 1 + n);
	return;
}

int calc() {
	int ans = 0;
	memset(v, false, sizeof(v));
	for (int i = 1; i <= n; i++) {
		if (v[i]) {
			continue;
		}
		v[i] = true;
		ans++;
		int rem = x - s[i];
		for (int j = n; j >= 1; j--) {
			if (s[j] > rem) {
				continue;
			}
			if (v[j]) {
				continue;
			}
			v[j] = true;
			break;
		}
	}
	return ans;
}

int main() {
	int tcase;
	scanf("%d", &tcase);
	for (int i = 1; i <= tcase; i++) {
		init();
		printf("Case #%d: %d\n", i, calc());
	}
	return 0;
}