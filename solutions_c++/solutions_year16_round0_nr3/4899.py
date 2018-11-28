#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <cstdio>
#include <vector>
#include <algorithm>

using namespace std;

vector <int> ans;

int n = 16;
int j = 50;

long long get(long long a, int base) {
	long long j = 1;
	long long c = 0;
	for (int i = 0; i < n; i++) {
		if ((1 << i) & a) {
			c += j;
		}
		j *= base;
	}
	return c;
}

int check(long long num) {
	for (long long j = 3; j * j <= num; j++) {
		if (num % j)
			continue;
		return j;
	}
	return -1;
}

void print(long long a) {
	for (int i = n - 1; i >= 0; i--)
		if ((1 << i) & a)
			cout << 1;
		else
			cout << 0;
}

int main() {
	freopen("small.out", "w", stdout);

	cout << "Case #1:\n";

	int cur = 0;
	for (long long i = (1ll << (n - 1)) + 1; i < (1ll << (n)); i += 2) {
		ans.clear();
		for (int j = 2; j <= 10; j++) {
			long long u = get(i, j);
			long long f = check(u);
			if (f != -1) {
				ans.push_back(f);
			}
		}
		if (ans.size() == 9) {
			print(i);
			cout << ' ';
			for (int j = 0; j < ans.size(); j++)
				cout << ans[j] << ' ';
			cout << '\n';
			cur++;
			if (cur == j)
				break;
		}
	}

	return 0;
}