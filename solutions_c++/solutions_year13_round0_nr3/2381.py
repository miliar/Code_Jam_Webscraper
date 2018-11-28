#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
using namespace std;
#define N 10000000
long long a, b;
int table[N + 1] = {0};
int ok(long long t)
{
	char tmp[100];
	sprintf(tmp, "%lld", t);
	int l = strlen(tmp);
	for (int i = 0; i < l / 2; ++i) {
		if (tmp[i] != tmp[l - i - 1]) {
			return 0;
		}
	}
	return 1;
}
void pre()
{
	for (long long i = 1; i <= N; ++i) {
		if (!ok(i)) {
			continue;
		}
		long long t = i * i;
		if (ok(t)) {
			table[i] = 1;
		}
	}
}
int solve()
{
	long long i;
	for (i = 1; i * i < a; ++i) ;
	int cnt = 0;
	for (; i * i <= b; ++i) {
		if (table[i]) {
			cnt++;
		}
	}
	return cnt;
}
int main()
{
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	int T;
	scanf("%d", &T);
	pre();
	for (int i = 1; i <= T; ++i) {
		scanf("%lld %lld", &a, &b);
		printf("Case #%d: %d\n", i, solve());
	}
	return 0;
}