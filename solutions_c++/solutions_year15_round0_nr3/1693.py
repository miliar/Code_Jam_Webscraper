#include <bits/stdc++.h>
using namespace std;
const int MAXN = 10000 + 10;
const int op[5][5] = {
	{0, 0, 0, 0, 0},
	{0, 1, 2, 3, 4},
	{0, 2, -1, 4, -3},
	{0, 3, -4, -1, 2},
	{0, 4, 3, -2, -1}
};

int change(char c) {return c - 'i' + 2;}

int mul(int a, int b) {
	int sa(1), sb(1);
	if (a < 0) sa = -1;
	if (b < 0) sb = -1;
	int r = op[abs(a)][abs(b)];
	return r * sa * sb;
}

char buf[MAXN];
int A[MAXN], ps[MAXN];
int X, L, N;

int main() {
	int T; scanf("%d", &T);
	for (int cas = 1; cas <= T; ++ cas) {
		scanf("%d%d%s", &L, &X, buf);
		for (int i = 0; i < L * X; ++ i) {
			A[i] = change(buf[i % L]);
		}
		N = L * X; ps[N] = 1;
		for (int i = N - 1; i >= 0; -- i) {
			ps[i] = mul(A[i], ps[i + 1]);
		}
		int is = 1, js = 1, ks = 1;
		bool flag = false;
		for (int i = 0; i < N && !flag; ++ i) {
			is = mul(is, A[i]); js = 1;
			for (int j = i + 1; j < N && !flag; ++ j) {
				js = mul(js, A[j]); ks = ps[j + 1];
				if (is == 2 && js == 3 && ks == 4) {
					flag = true;
				}
			}
		}
		printf("Case #%d: %s\n", cas, flag ? "YES" : "NO");
	}
	return 0;
}
