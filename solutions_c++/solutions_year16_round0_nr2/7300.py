#include <iostream>
#include <stdio.h>
using namespace std;

char a[1000];

int main() {
	int n, j;
	scanf("%d", &n);
	j = 1;
	while(n--) {
		scanf("%s", a);
		int len = 0;
		int i;
		for (i=0; a[i]!='\0'; i++) {
		}
		len = i;
		int out = 0;
		if (a[len-1] == '-') {
			out++;
		}
		for (i = len-2; i>=0; i--) {
			if (a[i] != a[i+1]) {
				out++;
			}
		}
		printf("Case #%d: %d\n", j, out);
		j++;
	}
	return 0;
}
