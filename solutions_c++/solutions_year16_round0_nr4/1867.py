#include <stdio.h>
#include <string.h>
#include <iostream>

using namespace std;

typedef long long LL;

void solve(int k, int c, int s) {
	if (c == 1) {
		if (s < k) {
			puts(" IMPOSSIBLE");
		} else {
			for (int i = 1; i <= k; ++i) {
				printf(" %d", i);
			}
			puts("");
		}
		return;
	}

	if (s < (k+1)/2) {
		puts(" IMPOSSIBLE");
		return;
	}
	for (int i = 1; i <= k; i+=2) {
		LL before = i-1;
		for (int j=1;j<c;++j) {
			before *= k;
		}
		LL pos = (i==k)?i:(i+1);
		cout<<" "<<before+pos;
	}
	puts("");
}

int main() {
	int T;scanf("%d",&T);
	for (int t=1;t<=T;++t){
		int K,C,S;scanf("%d%d%d",&K,&C,&S);
		printf("Case #%d:", t);
		solve(K,C,S);
	}
	return 0;
}
