#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <vector>
#include <set>
#include <queue>
#include <stack>
#include <map>
#include <string>
#include <algorithm>
#include <assert.h>
#include <math.h>

using namespace std;

#define mp make_pair
#define pb push_back
#define all(a) a.begin(), a.end()
const int N = 1e6 + 10;
int z[N];

bool used[10];
int calc(int n) {
	for (int i = 0; i < 10; i++)
		used[i] = false;

	int cnt = 0;
	for (int i = 1; i <= 400; i++) {
		int x = i * n;
		while (x) {
			if (!used[x % 10]) {
				used[x % 10] = true;
				cnt++;
			}
			x /= 10;
		}
		if (cnt == 10) {
			return i * n;
		}
	}
	return -1;
}

int main() {
#ifdef _DEBUG
	freopen("A-large.in", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif // _DEBUG
	for (int i = 1; i < N; i++) {
		z[i] = calc(i);
	}
	int t;
	scanf("%d", &t);
	for (int i = 0; i < t; i++) {
		int n;
		scanf("%d", &n);
		printf("Case #%d: ", i + 1);
		if (n == 0) {
			printf("INSOMNIA\n");
		}
		else {
			printf("%d\n", z[n]);
		}
	}
	return 0;
}