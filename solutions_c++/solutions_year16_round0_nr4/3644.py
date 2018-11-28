#include "cstdio"
#include "iostream"

using namespace std;

int main(void) {

	int t;
	scanf("%d", &t);
	for(int test = 1;test<=t;test++) {
		int k, c, s;
		cin >> k >> c >> s;

		printf("Case #%d:", test);

		if(c == 1) {
			if(s == k) {
				for(int i=1;i<=k;i++)
					printf(" %d", i);
				printf("\n");
			}	else {
				printf(" IMPOSSIBLE\n");
			}	
		} else {
			if(k == 1) {
				printf(" 1\n");
			}
			else if(s >= k-1) {
				for(int i=0;i<k-1;i++)
					printf(" %d", i*k + i + 2);
				printf("\n");
			}	else {
				printf(" IMPOSSIBLE\n");
			}
		}
	}
	return 0;
}

