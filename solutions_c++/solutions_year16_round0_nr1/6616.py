#include <stdio.h>

long long n, oldn;
bool done[10];

bool update(long long x) {
	int i;
	while (x) {
		done[x%10]=true;
		x/=10;
	}
	for (i=0; i<10; ++i) 
		if (!done[i]) return false;	
	return true;
}

void work() {
	int i;
	for (i = 0; i < 10; ++i) done[i] = false;
	oldn = n;
	for (i = 1; i <= 100000; ++i) {
		if (update(n)) {
			printf("%lld\n", n);
			return;
		}
		n += oldn;
	}
	printf("INSOMNIA\n");
}

int main() {
	int i, t, T;
	scanf("%d",&T);
	for (t=1; t<=T; ++t) {
		scanf("%lld",&n);
		printf("Case #%d: ", t);
		if (n) {
			work();
		} else {
			printf("INSOMNIA\n");
		}
	}
	return 0;
}
