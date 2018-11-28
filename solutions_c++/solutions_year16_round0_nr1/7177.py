#include<stdio.h>
#include<stdlib.h>
#include<algorithm>
main() {
	freopen("A-large.in", "r", stdin);
	freopen("out.txt", "w", stdout);
	int n;
	scanf("%d", &n);
	int num;
	int tcase = 1;
	bool chk[10];
	for(int i = 0; i < n; i++) {
		scanf("%d", &num);
		int original = num;
		if(num == 0) {
			printf("Case #%d: INSOMNIA\n", tcase++);
			continue;
		}
		for(int j = 0; j <= 9; j++) chk[j] = false;
		
		char str[50];
		for(;;) {
			sprintf(str, "%d", num);
			for(int j = 0; str[j] != '\0'; j++) {
				chk[str[j] - '0'] = true;
			}
			bool flag = true;
			for(int j = 0; j <= 9; j++)
				if(chk[j] == false) flag = false;
			if(flag) { 
			 	printf("Case #%d: %d\n", tcase++, num); 
				break; 
			}
			num += original;
		}
	}
}
