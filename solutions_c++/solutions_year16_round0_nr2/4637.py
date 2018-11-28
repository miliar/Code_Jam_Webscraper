#include <stdio.h>
#include <string.h>

char str[128];

bool check() {
	int len = strlen(str);
	for (int i = 0; i < len; ++i) {
		if (str[i] == '-') {
			return false;
		}
	}
	return true;
}
void flip(int x) {
	int low = 0;
	int high = x;
	while (low < high) {
		char tmp = str[low];
		str[low] = str[high];
		str[high] = tmp;
		++low;
		--high;
	}
	for (int i = 0; i <= x; ++i) {
		str[i] = (str[i] == '+' ? '-' : '+');
	}
}
int encode() {
	int res = 0;
	int len = strlen(str);
	for (int i = 0; i < len; ++i) {
		res = (res << 1 | (str[i] == '+' ? 1 : 0));
	}
	return res;
}

int solve() {
	int len = strlen(str);
	int res = 0;
	for (int i = len - 1; i >= 0; --i) {
		if (str[i] == '+') {
			continue;
		}
		if (str[0] == '-') {
			++res;
			flip(i);
		} else {
			int j = 0;
			while (j + 1 < i && str[j + 1] == '+') {
				++j;
			}
			res += 2;
			flip(j);
			flip(i);
		}
	}
	return res;
}


int main() {
	freopen("B-large.in", "r", stdin);
	freopen("B_output.txt", "w", stdout);
	int T;
	scanf("%d", &T);
	for (int cas = 1; cas <= T; ++cas) {
		printf("Case #%d: ", cas);
		scanf("%s", str);
		int ans = solve();
		printf("%d\n", ans);
	}
	return 0;
}
