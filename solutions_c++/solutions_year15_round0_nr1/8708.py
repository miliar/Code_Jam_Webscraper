#include <stdio.h>

int main(void) {
	int t, smax;
	char s[1010];
	scanf("%d", &t);
	for(int i=0; i<t; ++i) {
		scanf("%d %s", &smax, s);
		int counter = 0, addition_counter = 0;
		for(int j=0; j<=smax; ++j) {
			if(j-counter > 0) {
				addition_counter += j - counter;
				counter += j - counter;
			}
			counter += s[j]-'0';
		}
		printf("Case #%d: %d\n", i+1, addition_counter);
	}
	return 0;
}
