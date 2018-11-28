#include <stdio.h>
#include <string.h>
#pragma warning (disable:996)

int main(){

#ifndef _DEBUG_
	freopen("bigA.in", "r", stdin);
	freopen("bigA.out", "w", stdout);
#endif

	int tCase, tryCount = 0;
	long long number, currentNum;
	char buf[10000];

	scanf("%d", &tCase);

	for (int i = 1; i <= tCase; i++){
		
		char digits[11] = { 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '\0' };
		printf("\nCase #%d: ", i);

		scanf("%lld", &number);
		sprintf(buf, "%lld", number);

		if (number == 0){
			printf("INSOMNIA");
			continue;
		}

		while (strcmp(digits, "1111111111")){
			for (int j = 0; j < strlen(buf); j++){
				if (0 <= buf[j] - '0' && buf[j] - '0' <= 9){
					digits[buf[j] - '0'] = '1';
				}
			}

			tryCount++;
			currentNum = (tryCount+1) * number;
			sprintf(buf, "%lld", currentNum);
		}

		printf("%lld", (tryCount*number));
		tryCount = 0;
	}

	getchar();
	
	return 0;
}