#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <time.h>

using namespace std;
const int N = 1e6 + 5;
bool used[10];
int z[N];

int calc(int n) {
	if (z[n] != -2) return z[n];
	memset(used, 0, sizeof used);
	int cnt = 0;
	for (int i = 1; i < 100; i++) {
		int x = n * i;
		while (x > 0) {
			cnt += !used[x % 10];
			used[x % 10] = true;
			x /= 10;
		}
		if (cnt == 10) return n * i;
	}
	return -1;
}
int main(){
#ifdef _DEBUG
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif
	for (int i = 0; i < N; i++) {
		z[i] = -2;
	}

	int t;
	scanf("%d", &t);
	for (int i = 0; i < t; i++) {
		int n;
		scanf("%d", &n);
		if (calc(n) == -1) {
			printf("Case #%d: INSOMNIA\n", i + 1);
		}
		else {
			printf("Case #%d: %d\n", i + 1, calc(n));
		}
	}
	return 0;
}