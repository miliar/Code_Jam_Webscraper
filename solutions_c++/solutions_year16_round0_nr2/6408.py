#include<stdio.h>
#include<stdlib.h>
#include<string.h>

#define maxPancake 105

int main() {
	int testCase;
	scanf("%d\n", &testCase);
	for(int t=0; t<testCase; t++) {
		char pancake[maxPancake];
		memset(pancake, 0, sizeof(char)*maxPancake);
		scanf("%s\n", pancake);
		int length = strlen(pancake);
		int tailPtr = length-1;
		int ans = 0;
		while(tailPtr >= 0 && pancake[tailPtr]=='+')
			tailPtr -= 1;
		while(tailPtr >= 0) {
			if(pancake[0] == '+') {
				pancake[0] = '-';
				ans += 1;
				int flipN = 1;
				while(flipN < length && pancake[flipN]=='+') {
					pancake[flipN] = '-';
					flipN += 1;
				}
			}
			else {
				ans += 1;
				for(int i=0; i<=tailPtr; i++) {
					if(pancake[i] == '+')
						pancake[i] = '-';
					else
						pancake[i] = '+';
				}
				char tmp[maxPancake];
				for(int i=0; i<=tailPtr; i++)
					tmp[i] = pancake[tailPtr-i];
				for(int i=0; i<=tailPtr; i++)
					pancake[i] = tmp[i];
				while(tailPtr >= 0 && pancake[tailPtr]=='+')
					tailPtr -= 1;
			
			}
		}
		printf("Case #%d: %d\n", t+1, ans);
	}
	return 0;
}
