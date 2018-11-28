#include <cstdio>
#include <cstring>
#include <cstdlib>
using namespace std;

#define LL long long

int tr[5][5] = {
	{0, 0, 0, 0, 0},
	{0, 1, 2, 3, 4},
	{0, 2, -1, 4, -3},
	{0, 3, -4, -1, 2},
	{0, 4, 3, -2, -1}
};

int T;
int L;
LL X;
int first, last;
int pi;
char s[16384];
int a[16384];

int mul(int a, int b) {
	int ans = 1;
	if (a < 0) {
		ans *= -1;
		a *= -1;
	}
	if (b < 0) {
		ans *= -1;
		b *= -1;
	}
	return ans * tr[a][b];
}

int pow(int a, LL b) {
	if (b == 0) return 1;
	int t = pow(a, b / 2ll);
	t = mul(t, t);
	if (b % 2ll == 1ll) t = mul(t, a);
	return t;
}

int main() {
	scanf("%d", &T);
	for (int test = 1; test <= T; ++test) {
		printf("Case #%d: ", test);
		scanf("%d %lld", &L, &X);
		scanf("%s", s);
		for (int i = 0; i < L; ++i) {
			if (s[i] == 'i') a[i] = 2;
			if (s[i] == 'j') a[i] = 3;
			if (s[i] == 'k') a[i] = 4;
		}
		pi = 1;
		for (int i = 0; i < L; ++i)
			pi = mul(pi, a[i]);
		pi = pow(pi, X);
		first = -1;
		last = -1;
		int v = 1;
		for (int tn = 0; tn < 4; ++tn) {
			for (int i = 0; i < L; ++i) {
				v = mul(v, a[i]);
				if (v == 2) {
					first = tn * L + i + 1;
					break;
				}
			}
			if (v == 2) break;
		}
		v = 1;
		for (int tn = 0; tn < 4; ++tn) {
			for (int i = 0; i < L; ++i) {
				v = mul(a[L - i - 1], v);
				if (v == 4) {
					last = tn * L + i + 1;
					break;
				}
			}
			if (v == 4) break;
		}
		if (first > 0 && last > 0 && pi == -1 && (LL)first + (LL)last <= (X * (LL)L))
			printf("YES\n");
		else
			printf("NO\n");
	}
	return 0;
}