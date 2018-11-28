#include <bits/stdc++.h>

using namespace std;

typedef long long ll;
typedef pair<int, int> ii;
typedef vector<int> vi;
typedef vector<ii> vii;

int T, K, C, S;

int main() {
	int t = 1, i;
	scanf("%d", &T);
	while (T--) {
		scanf("%d %d %d", &K, &C, &S);
		printf("Case #%d:", t++);
		for (i=1; i<=S; i++) {
			printf(" %d", i);
		}
		printf("\n");
	}
	return 0;
}