#include <cstdio>
#include <algorithm>

bool used[10005];
int sizes[10005];

int f() {
	int n, c;
	scanf("%d %d", &n, &c);
	for (int i = 0; i < n; i++) {
		scanf("%d", &sizes[i]);
		used[i] = false;
	}
	std::sort(sizes, sizes+n);
	std::reverse(sizes, sizes+n);
	int ans = 0;
	for(int i = 0; i < n; i++) {
		if (used[i])continue;
		used[i] = true;
		for (int j = 0; j <n; j++) {
			if (used[j] || sizes[i] + sizes[j] > c) continue;
			used[j] = true;
			break;
		}
		ans += 1;
	}
	return ans;
}

int main() {
	int t;
	scanf("%d", &t);
	for (int i = 0; i < t; i++) {
		printf("Case #%d: %d\n", i+1, f());
	}
}