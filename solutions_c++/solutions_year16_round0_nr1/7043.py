#include <bits/stdc++.h>
using namespace std;

int tt = 0;
int ns = 0;
int cas = 0;

void check(int n) {
	if (n == 0) {
		printf("Case #%d: INSOMNIA\n", ++cas);
		return;
	}

    int hash[10] = {0, 0, 0, 0, 0, 0, 0, 0, 0, 0};
    int sum = 0;
    int i = 1;

    for (; sum < 10; ++i) {
    	int t = n * i;
    	while(t > 0) {
    		if (hash[t % 10] == 0) {
    			++sum;
    			hash[t % 10] = 1;
    		}
    		t /= 10;
    	}
    }

    printf("Case #%d: %d\n", ++cas, (i - 1) * n);
    return;
}

int main() {
	scanf("%d", &tt);
	for(;tt > 0; --tt) {
		scanf("%d", &ns);
		check(ns);
	}
}