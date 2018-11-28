#include <iostream>

using namespace std;

const int N = 1005;

char str[N];

int main() {
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	int t;
	scanf("%d", &t);
	for (int cas = 1; cas <= t; cas++) {
		int sMax, n;
		scanf("%d", &sMax);
		scanf("%s", str);
		n = sMax+1;
		int frds = 0;
		int sum = 0;
		for (int i = 0; i < n; i++) {
			int t = str[i]-'0';
			if (t == 0) continue;
			if(sum+frds < i) {
				frds = i-sum;
			}
			sum += t;
		}
		printf("Case #%d: %d\n", cas, frds);
	}
	return 0;
}
