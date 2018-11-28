#include <bits/stdc++.h>
using namespace std;
int main() {
	int T, len, rep, n;
	scanf("%d", &T);
	for(int caso=1 ; caso<=T ; caso++) {
		scanf("%d %d %d", &len, &rep, &n);
		printf("Case #%d:", caso);
		for(int i=1 ; i<=n ; i++) printf(" %d", i);
		printf("\n");
	}
	return 0;
}