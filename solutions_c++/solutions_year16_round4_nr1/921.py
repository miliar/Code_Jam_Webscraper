#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstring>
#include <algorithm>
#include <vector>

using namespace std;
typedef long long ll;
int a[15][5000];
bool ff = true;
int b[5000];

void tran(int *a, int l1, int l2, int len) {
	bool flag = true;
	for (int i = 1; i <= len; i++) {
		if (a[l1 + i - 1] < a[l2 + i - 1])
			break;
		if (a[l1 + i - 1] > a[l2 + i - 1]) {
			flag = false;
			break;
		}
	}
	if (!flag) {
		for (int i = 1; i <= len; i++) {
			swap(a[l1 + i - 1] , a[l2 + i - 1]);
		}
	}
}

bool check(int a[], int len) {
	int b[5000];
	for (int i = 1; i <= len; i++)
		b[i] = a[i];
	while (1) {
		if (len == 1) return true;
		int j = 0;
		for (int i = 1; i < len; i+=2) {
			if (b[i] == b[i + 1])
				return false;
			j ++;
			if (b[i] + b[i + 1] == 4)
				b[j] = 3;
			else b[j] =min(b[i], b[i + 1]);
		}
		len = j;
	}
}

void dfs(int p , int r, int s, int now ) {
	if (ff)
		return;
	if (p == 0 && r == 0 && s == 0) {
		if (check(b, now - 1)) {
			ff = true;
			for (int i = 1; i <= now - 1; i++) {
				if (b[i] == 1) printf("P");
				if (b[i] == 2) printf("R");
				if (b[i] == 3) printf("S");
			}
			printf("\n");
		}
		return;
	}
	if (p) {
		b[now] = 1;
		dfs(p - 1, r, s, now + 1);
	}
	if (r) {
		b[now] = 2;
		dfs(p, r - 1, s, now + 1);
	}
	if (s) {
		b[now] = 3;
		dfs(p, r, s - 1, now + 1);
	}
}

int main() {
	int o, cas = 0;
	scanf("%d", &o);
	while (o--) {
		int n, p, r, s;
		scanf("%d%d%d%d", &n, &r, &p, &s);
		/*ff = false;
		printf("Case #%d: ", ++cas);
		dfs(p, r, s, 1);
		if (!ff) {
			printf("IMPOSSIBLE\n");
		}*/
		
		int pp = p, rr = r, ss = s;
		bool flag = true;
		while (1) {
			if (pp < 0 || rr < 0 || ss < 0) {
				flag = false;
				break;
			}
			if (pp + rr + ss == 1) break;
			int np = (pp + rr - ss) / 2 , ns = (pp + ss - rr) / 2, nr = (ss + rr - pp) / 2;
			pp = np;
			ss = ns;
			rr = nr;
		}
		printf("Case #%d: ", ++cas);
		if (flag == false) {
			printf("IMPOSSIBLE\n");
			continue;
		}
		a[0][0] = 1;
		if (pp) {
			a[0][1] = 1;
		} else if (rr) {
			a[0][1] = 2;
		} else if (ss) {
			a[0][1] = 3;
		}
		for (int i = 1; i <= n; i++) {
			a[i][0] = a[i - 1][0] * 2;
			int l = 0;
			for (int j = 1; j <= a[i - 1][0]; j++) {
				int x = a[i - 1][j];
				if (x == 1) {
					a[i][++l] = 1;
					a[i][++l] = 2;
				}else if (x == 2) {
					a[i][++l] = 2;
					a[i][++l] = 3;
				}else {
					a[i][++l] = 1;
					a[i][++l] = 3;
				}
			}
		}
		for (int i = 1; i < a[n][0]; i*=2) {
			for (int j = 1; j < a[n][0]; j += i * 2) {
				int l1 = j, l2 = j + i;
				tran(a[n], l1, l2, i);
			}
		}
		for (int i = 1; i <= a[n][0]; i++) {
			if (a[n][i] == 1) printf("P");
			if (a[n][i] == 2) printf("R");
			if (a[n][i] == 3) printf("S");
		}
		printf("\n");
		
	}
	return 0;
}