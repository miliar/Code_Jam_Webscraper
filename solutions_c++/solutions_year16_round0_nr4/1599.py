#include<iostream>
#include<algorithm>
#include<vector>
using namespace std;

int main() {
	int t;
	freopen("D-small-attempt1.in", "r", stdin);
	freopen("out.out", "w", stdout);
	scanf("%d", &t);
	int cas = 1;
	while (t--) {
		printf("Case #%d: ", cas++);
		int k, c, s;
		scanf("%d%d%d", &k, &c, &s);
		for (int i = 1;i <= k;++i)
			printf("%d ", i);
		puts("");
	}
}