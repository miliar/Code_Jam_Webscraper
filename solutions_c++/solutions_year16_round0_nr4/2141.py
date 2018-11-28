#include <cstdio>
#include <iostream>
using namespace std;
unsigned long long mi(int k, int c) {
	long long ans = 1;
	for (int i = 0 ; i < c; i++)
		ans = ans * (unsigned long long)k;
	return ans;
}
int main() {
	freopen("D-small-attempt1.in", "r", stdin);
	freopen("b.txt", "w", stdout);
	int T;
	scanf("%d", &T);
	int k, c, s;
	for (int t = 0; t < T; t++) {
		scanf("%d %d %d", &k, &c, &s);
		printf("Case #%d:", t + 1);
		if (k == 1) {
			printf(" 1\n");
		}
		else {
			for (unsigned long long i = 0 ; i < k; i++) {
				unsigned long long ans = i * (mi(k, c) - 1)/ (k - 1) + 1;
				cout << " " << ans;
			}
			cout << endl;
		}
	}
}