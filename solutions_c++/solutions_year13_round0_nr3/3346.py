#include <cstdio>
#include <cmath>

int casei, cases, A, B;
char st[20];

bool palin(int num) {
	int len = 0;
	while (num > 0) {
		st[len++] = num % 10;
		num /= 10;
	}
	for (int i = ((len - 1) >> 1); i >= 0; --i)
		if (st[i] != st[len - i - 1]) return false;
	return true;
}

int main() {
	freopen("C-small-attempt0.in", "r", stdin);
	freopen("out.txt", "w", stdout);

	scanf("%d", &cases);
	for (casei = 1; casei <= cases; ++casei) {
		scanf("%d%d", &A, &B);
		int ans = 0;
		for (int i = A; i <= B; ++i) {
			int j = static_cast<int>(sqrt(i));
			if (j * j < i) ++j;
			if (j * j > i) --j;
			if (j * j != i) continue;
			if (palin(i) && palin(j)) ++ans;
		}
		printf("Case #%d: %d\n", casei, ans);
	}
	
	return 0;
}
