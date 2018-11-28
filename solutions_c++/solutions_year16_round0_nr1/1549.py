#include <vector>
#include <string>
#include <iostream>
#include <algorithm>
#include <numeric>
#include <map>
#include <set>
#include <string.h>

typedef long long ll;
using namespace std;

void count(int c[], int x) {
	while (x > 0) {
		c[x%10]++;
		x /= 10;
	}
}

bool all_digits(int c[]) {
	for (int i = 0; i < 10; i++) {
		if (c[i] == 0)
			return false;
	}
	return true;
}

int solve(int N) {
	if (N == 0)
		return 0;
	int c[10] = {};
	int x = N;
	for (int r = 1;; r++) {
		count(c, x);
		if (all_digits(c))
			return x;
		x += N;
		if (x <= 0) {
			printf("!!!!!!!!!!\n");
		}
	}
}

int main()
{
	int T;
	scanf("%d", &T);
	for (int i = 0; i < T; i++) {
		int N;
		scanf("%d", &N);
		int ans = solve(N);
		printf("Case #%d: ", i+1);
		if (ans == 0)
			printf("INSOMNIA\n");
		else
			printf("%d\n", ans);
	}
}
