#include <cstdio>
#define MAXN 11000
inline long long min(long long a, long long b) {
	return a < b ? a : b;
}
inline int min(int a, int b) {
	return a < b ? a : b;
}
const int multiply[8][8] = {
	{0, 1, 2, 3, 4, 5, 6, 7},
	{1, 4, 3, 6, 5, 0, 7, 2},
	{2, 7, 4, 1, 6, 3, 0, 5},
	{3, 2, 5, 4, 7, 6, 1, 0},
	{4, 5, 6, 7, 0, 1, 2, 3},
	{5, 0, 7, 2, 1, 4, 3, 6},
	{6, 3, 0, 5, 2, 7, 4, 1},
	{7, 6, 1, 0, 3, 2, 5, 4}
};
int convert(char ch) {
	if(ch == '1') return 0;
	if(ch == 'i') return 1;
	if(ch == 'j') return 2;
	return 3;
}
int pow(int x, int y) {
	if(y == 0) {
		return convert('1');
	}
	if(y&1) {
		return multiply[pow(multiply[x][x], y/2)][x];
	}
	return pow(multiply[x][x], y/2);
}
long long n, m;
int alone;
int a[MAXN+5];
bool exist() {
	int I = 0, J = 0, K = 0, operat = 1;
	for(long long i = 1; i <= min(m, 10ll); i++) {
		for(long long j = 1; j <= n; j++) {
			switch (operat) {
				case 1:
					I = multiply[I][a[j]];
					if(I == 1) operat++;
					break;
				case 2:
					J = multiply[J][a[j]];
					if(J == 2) operat++;
					break;
				default:
					for(int k = j; k <= n; k++) {
						K = multiply[K][a[k]];
					}
					K = multiply[K][pow(alone, m-i)];
					return K == 3;
			}
		}
	}
	return false;
}

int main() {
	int T; scanf("%d", &T); char ch;
	for(int t = 1; t <= T; t++) {
		alone = 0;
		scanf("%I64d%I64d", &n, &m);scanf("%c", &ch);
		for(int i = 1; i <= n; i++) {
			scanf("%c", &ch);
			a[i] = convert(ch);
			alone = multiply[alone][a[i]];
		}
		if(exist()) {
			printf("Case #%d: YES\n", t);
		} else {
			printf("Case #%d: NO\n", t);
		}
	}
	return 0;
}
