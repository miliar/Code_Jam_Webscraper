#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#pragma warning(disable : 4996)

int main(){
	int T;
	int i, j, k;
	scanf("%d", &T);
	for (i = 1; i <= T; i++){
		char pancake[105];
		scanf("%s", pancake);
		int cnt = 0;
		for (j = 0; j < strlen(pancake); j++){
			for (k = 0; k < strlen(pancake)-1; k++){
				if (pancake[k] != pancake[k+1]){
					cnt++;
					while (k >= 0){
						if (pancake[k] == '-')
							pancake[k] = '+';
						else
							pancake[k] = '-';
						k--;
					}
					break;
				}
			}
			
		}
		if (pancake[strlen(pancake)-1]=='-')
			cnt++;
		printf("Case #%d: %d\n", i, cnt);
	}
	return 0;
}