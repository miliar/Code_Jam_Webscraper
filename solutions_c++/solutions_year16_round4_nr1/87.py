#include<cstring>
#include<cstdio>
#include<algorithm>
using namespace std;
int cnt[7777], st[7777];
void dfs(int n, int c, int offset) {
	if(n == 0) {
		st[offset] = c;
		cnt[c]++;
	}else {
		dfs(n - 1, (c + 2) % 3, offset);
		dfs(n - 1, c, offset + (1 << (n - 1)));
	}
}
bool cmp(int j, int i) {
	for(int k(0); k < (1 << i - 1); k++) {
		if(st[j + k] > st[j + (1 << i - 1) + k]) {
			return true;
		}
	}
	return false;
}
void print(int n) {
	for(int i(0); i < (1 << n); i++) {
		char tmp = (st[i] == 0 ? 'R' : (st[i] == 1 ? 'P' : 'S'));
		st[i] = tmp;
	}
	for(int i(1); i <= n; i++) {
		for(int j(0); j < (1 << n); j += (1 << i)) {
			if(cmp(j, i)) {
				for(int k(0); k < (1 << i - 1); k++) {
					swap(st[j + k], st[j + (1 << i - 1) + k]);
				}
			}
		}
	}
	for(int i(0); i < (1 << n); i++) {
		printf("%c", st[i]);
	}
	printf("\n");
}
int main() {
	int tests;
	scanf("%d", &tests);
	for(int qq(1); qq <= tests; qq++) {
		printf("Case #%d: ", qq);
		int a, b, c, n;
		scanf("%d%d%d%d", &n, &a, &b, &c);
		cnt[0] = cnt[1] = cnt[2] = 0;
		dfs(n, 0, 0);
		//printf("%d %d %d %d\n", n, cnt[0], cnt[1], cnt[2]);
		if(cnt[0] == a && cnt[1] == b && cnt[2] == c) {
			print(n);
			continue;
		}
		cnt[0] = cnt[1] = cnt[2] = 0;
		dfs(n, 1, 0);
		if(cnt[0] == a && cnt[1] == b && cnt[2] == c) {
			print(n);
			continue;
		}
		cnt[0] = cnt[1] = cnt[2] = 0;
		dfs(n, 2, 0);
		if(cnt[0] == a && cnt[1] == b && cnt[2] == c) {
			print(n);
			continue;
		}
		printf("IMPOSSIBLE\n");
	}
}
