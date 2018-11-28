#include <iostream>
#include <algorithm>
#include <vector>
#include <queue>
#include <cstdio>
using namespace std;
#pragma warning(disable:4996)
int n, m;
int main() {
	int t;
	freopen("out.txt", "w", stdout);
	freopen("in.txt", "r", stdin);
	scanf("%d", &t);
	for (int i = 1; i <= t; i++) {
		int n;
		scanf("%d", &n);
		vector<bool> visit(10, 0);
		int c = 0;
		printf("Case #%d: ", i);
		for (int j = 1; j<=10000000; j++) {
			int k = n*j;
			while (k > 0) {
				if (!visit[k % 10]) {
					visit[k % 10] = 1;
					c++;
				}
				k /= 10;
			}
			if (c >= 10) {
				printf("%d\n", n*j);
				break;
			}
		}
		if (c < 10)
			printf("INSOMNIA\n");
	}
	return 0;
}