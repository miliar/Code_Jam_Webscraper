#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<math.h>
#include<string>
#include<algorithm>
#include<set>
#include<map>
#include<queue>
using namespace std;

int p[1005];
int n;

int func(int d) {
	int res = d;
	for (int i = 0; i < n; i++) {
		res += p[i] / d + (p[i] % d != 0) - 1;
	}
	return res;
}

int main() {
	freopen("B.in", "r", stdin);
	freopen("B.out", "w", stdout);
	int TT;
	scanf("%d", &TT);
	for (int T = 0; T < TT; T++) {
		printf("Case #%d: ", T + 1);
		scanf("%d", &n);
		for (int i = 0; i < n; i++) {
			scanf("%d", &p[i]);
		}
		sort(p, p + n);
		int res = p[n-1];
		for (int i = 1; i < p[n - 1]; i++)
		{
			res = min(res, func(i));
		}
		printf("%d\n", res);
	}
	return 0;
}