#include <cstdio>
#include <cstring>
#include <iostream>
using namespace std;

bool vis[10];
int dcnt;

void test(int n) {
//	cout << n << endl;
	while (n) {
		int x = n % 10;
		if (!vis[x]) {
			vis[x] = true;
			dcnt++;
		}
		n /= 10;
	}
}

int main() {
	int T;
	scanf("%d", &T);
	for (int tn = 1; tn <= T; tn++) {
		int n;
		scanf("%d", &n);
		if (n == 0) {
			printf("Case #%d: INSOMNIA\n", tn);
			continue;
		}
		memset(vis, 0, sizeof(vis));
		dcnt = 0;
		int step = 0;
		while (dcnt < 10) {
			step++;
			test(n * step);
		}
		printf("Case #%d: %d\n", tn, step * n);
	}
	return 0;
} 