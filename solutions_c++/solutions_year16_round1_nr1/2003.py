#include<stdio.h>
#include<stdlib.h>
#include<string.h>

char str[4000];
char make[4000];
int length;
int cur = 1500;

int main(void) {
	int T;
	int N;
	int i, j, k;

	freopen("A-large.in", "r", stdin);
	freopen("out.txt", "w", stdout);

	scanf("%d", &T);

	for (i = 1; i <= T; i++) {
		cur = 1500;
		for (j = 0; j < 3000; j++) {
			str[j] = 0;
			make[j] = 0;
		}
		scanf("%s\n", str);
		length = strlen(str);

		make[cur] = str[0];
		
		for (j = 1; j < length; j++) {
			if (str[j] >= make[cur]) {
				make[--cur] = str[j];
			}
			else {
				make[cur + j] = str[j];
			}
		}
		make[cur + j] = 0;

		printf("Case #%d: %s\n", i, make + cur);
	}


}