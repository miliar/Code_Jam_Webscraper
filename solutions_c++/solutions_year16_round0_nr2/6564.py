#include "stdio.h"
#include "stdlib.h"
#include "string.h"


int n;

int t;

char str[105];

char mask[105];

int main() {
	freopen("B-large.in", "r", stdin);
	freopen("B_output.txt", "w", stdout);
	scanf("%d",&t);
	int i,j,k;
	for(i = 1; i <= t; i ++) {
		scanf("%s",str);
		int len = strlen(str);
		for(j = 0; j < len; j++) {
			mask[j] = '+';
		}
		mask[len] = 0;
		int ans = 0;
		while(strcmp(str,mask) != 0) {
			for(j = 1; j < len; j++) {
				if(str[j] != str[j-1]) {
					break;
				}
			}
		//	printf("==========%d============\n", j);
			for(k = 0; k < j; k++) {
				str[k] = (str[k] == '-') ? '+' : '-';
			}
	//		printf("==========%s============\n", str);
			ans ++;
		}
		printf("Case #%d: ",i);
		printf("%d\n",ans);
	}
	fclose(stdin);
	fclose(stdout);
	return 0;
}
