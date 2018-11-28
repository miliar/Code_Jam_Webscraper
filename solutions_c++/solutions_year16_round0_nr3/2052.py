#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <iostream>
#include <fstream>
#include <algorithm>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>

typedef long long LL;

std::vector<int> pr;
bool z[233333];

int check(int n) {
	for (int i = 0; i < (int)pr.size() && pr[i] < n; ++i)
		if (n % pr[i] == 0) return pr[i];
	return 0;
}

int main() {
	int N = 65536;
	for (int i = 2; i <= N; ++i) {
		if (!z[i]) pr.push_back(i);
		for (int j = 0; j < (int)pr.size() && i * pr[j] <= N; ++j) {
			z[i * pr[j]] = 1;
			if (i % pr[j]) break;
		}
	}
	int n = 32, m = 500;
	long long M = 1LL << (n - 2);
	printf("Case #1:\n");
	long long i = 0;
	for (int tot = 0; i < M && tot < m; ++i) {
		std::vector<int> a;
		a.push_back(1);
		for (long long K = i, j = 0; j < 30; K >>= 1, ++j)
			a.push_back(K & 1LL);
		a.push_back(1);
		std::reverse(a.begin(), a.end());
		std::vector<int> b;
		for (int j = 2; j <= 10; ++j) {
			int p = 0;
			for (int k = 0; k < (int)pr.size(); ++k) {
				int mod = 0;
				for (int q = 0; q < (int)a.size(); ++q)
					mod = (mod * j + a[q]) % pr[k];
				if (mod == 0) {
					p = pr[k];
					break;
				}
			}
			if (p) b.push_back(p);
			else break;
		}
		if (b.size() == 9) {
			for (int i = 0; i < (int)a.size(); ++i)
				printf("%d", a[i]);
			for (int i = 0; i < 9; ++i)
				printf(" %d", b[i]);
			printf("\n");
			++tot;
		}
	}
	return 0;
}
