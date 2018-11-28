#include<stdio.h>
#include<stdlib.h>
#include<string.h>

#define maxLength 2400

int main() {
	int test;
	scanf("%d\n", &test);
	for(int t=0; t<test; t++) {
		char str[maxLength];
		scanf("%s", str);
		int length = strlen(str);
		char ans[maxLength];
		int head = maxLength/2;
		int tail = maxLength/2;
		ans[head] = str[0];
		head -= 1;
		tail += 1;
		for(int i=1; i<length; i++) {
			if(str[i] >= ans[head+1]) {
				ans[head] = str[i];
				head -= 1;
			}
			else {
				ans[tail] = str[i];
				tail += 1;
			}
		}

		head += 1;
		printf("Case #%d: ", t+1);
		while(head < tail) {
			printf("%c", ans[head]);
			head += 1;
		}
		printf("\n");
	}
	return 0;
}
