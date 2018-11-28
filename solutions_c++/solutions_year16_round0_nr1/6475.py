#include "stdio.h"
#include "stdlib.h"
#include "string.h"


int n;

int t;

int mask = 0x3ff;

int main() {
//	freopen("A-large.in", "r", stdin);
//	freopen("A_output.txt", "w", stdout);
	scanf("%d",&t);
	int i;
	for(i = 1; i <= t; i ++) {
		int ans = 0;
		int nn = 0;
		int m = 0;
		scanf("%d",&n);
		if(n == 0) {
			printf("Case #%d: INSOMNIA\n", i);
			continue;
		}
		printf("Case #%d: ",i);
		while(ans != mask) {
			nn += n;
			m = nn;
			while(m) {
				ans |= (1 << (m%10));
				m /= 10;
			}
		}
		printf("%d\n",nn);
	}
	fclose(stdin);
	fclose(stdout);
	return 0;
}
