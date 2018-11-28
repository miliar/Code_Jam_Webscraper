#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<algorithm>

main() {
	freopen("B-large.in", "r", stdin);
	freopen("out.txt", "w", stdout);
	int n, tcase = 1;
	char str[105];
	scanf("%d", &n);
	for(int i = 0; i < n; i++) {
		scanf("%s", str);
		int len = strlen(str);
		
		int count = 0;
		if(str[0] == '-') count = 1;
		for(int j = 1; j < len; j++) {
			if(str[j] == '-' && str[j - 1] == '+') count += 2;
		}
		printf("Case #%d: %d\n", tcase++, count);
	}
}
