#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cstring>
#include <vector>
#define LL __uint128_t
#define LD long double
int N, J;
using namespace std;
LL trans(LL x, LL base) {
	LL ans = 1;
	for (int i = 1; i < (N - 1); i++) {
		ans = ans * base + (x & 1);
		x /= 2;
	}
	ans = ans * base + 1;
	return ans;
}
LL prime(LL x) {
	for (LL i = 2; i * i <= x && i <= 1048576; i++)
		if (x % i == 0)
			return i;
	return 0;
}
vector<LL> ans;
int cnt;
void output(LL x) {
	int s[50];
	s[0] = 1;
	for (int i = 1; i < (N - 1); i++) {
		s[i] = x & 1;
		x /= 2;
	}
	s[N - 1] = 1;
    for (int i = 0; i < N; i++)
		printf("%d", s[i]);
}
void Output10(LL x) {
	cout << " ";
	int s[50];
	s[0] = 0;
	int i, j;
	for (i = 0; x; i++) {
		s[i] = x % 10;
		x /= 10;
	}
	for (j = i - 1; j >= 0; j--)
		printf("%d", s[j]);

}
void check(LL x) {
	ans.clear();
	for (LL i = 2; i <= 10; i++) {
		LL tran = trans(x, i);
		LL factor = prime(tran);
		if (factor == 0)
			return;
		else
			ans.push_back(factor);
	}
	output(x);
	for (int j = 0; j < 9; j++)
		Output10(ans[j]);
	printf("\n");
	cnt++;
}

int main() {
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	int cas, cases;
	scanf("%d", &cas);
	for (cases = 1; cases <= cas; cases ++) {
		printf("Case #%d:\n", cases);
		scanf("%d%d", &N, &J);
		LL lim = 1;
		lim <<= N - 2;
		for (LL i = 0; i < lim; i++) {
			check(i);
			if (cnt == J)
				break;
		}
	}
}
