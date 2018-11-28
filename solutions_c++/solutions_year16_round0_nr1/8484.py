#include<bits/stdc++.h>
using namespace std;

bool x[11];
int ans = 0;

inline void ch(long long  t) {
	while(t) {
		if(x[t%10] == 0) ++ans;
		x[t%10] = 1;
		t /= 10;
	}
}

int t, n;
long long j;

int main(int argc, char **argv) {
	scanf("%d", &t);
	for(int T = 1, n; T<=t ; ++T) {
		scanf("%d", &n);
		printf("Case #%d: ", T);
		memset(x, 0, sizeof x);
		if(n == 0) {
			puts("INSOMNIA");
			continue;
		}
		ans = 0;
		for(j=n ; ans<10 ; j+=n) {
			ch(j);
		}
		printf("%lld\n", j-n);
	}
	return 0;
}
