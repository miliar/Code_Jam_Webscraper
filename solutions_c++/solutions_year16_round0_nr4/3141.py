#include <bits/stdc++.h>

using namespace std;

int main(){
	
	freopen("D-small-attempt0.in", "r", stdin);
	freopen("test.out", "w", stdout);

	int test, n, c, k, s;

	scanf("%d\n", &test);
	
	for (int i = 0; i < test; i++){
		scanf("%d %d %d", &k, &c, &s);
		printf("Case #%d: ", i+1);
		for (int j = 1; j <= k; j++){
			printf("%d ", j);
		}
		printf("\n");
	}
}