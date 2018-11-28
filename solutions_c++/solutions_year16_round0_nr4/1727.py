#include <bits/stdc++.h>
using namespace std;

int A[110];

int main() {
	int t;
	scanf("%d", &t);
	for(int tc=1; tc<=t; tc++) {
		int k, c, s;
		scanf("%d %d %d", &k, &c, &s);
		printf("Case #%d: ", tc);
		if(k == s) {
			for(int i=1; i<=s; i++)
				printf("%d ", i);
			printf("\n");
		}
	}
}