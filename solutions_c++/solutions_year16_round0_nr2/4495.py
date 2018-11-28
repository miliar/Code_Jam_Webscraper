#include <stdio.h>
#include <string.h>
#pragma warning (disable:996)

void flip(char* list, int end){

	char tmp;
	int i, size = end + 1;

	for (i = 0; i< size/2; i++){
		tmp = list[i];
		list[i] = list[ (size-1)-i ];
		list[(size-1)- i] = tmp;
	}
	for (i = 0; i <= end; i++){
		if (list[i] == '-') list[i] = '+';
		else list[i] = '-';
	}

}

bool isTerminate(char* c){

	for (int i = 0; i < strlen(c); i++){
		if (c[i] == '-') return false;
	}

	return true;
}

int main(){

#ifndef _DEBUG_
	freopen("largeB.in", "r", stdin);
	freopen("largeBOut.out", "w", stdout);
#endif

	int tCase = 0, j=0;
	char pStack[200];

	scanf("%d", &tCase);

	for (int i = 1; i <= tCase; i++){

		int moves = 0;

		scanf("%s", pStack);
		printf("\nCase #%d: ", i);
		
		// ¼ÒÆÃ
		while (true){

			j = 0;
			if (isTerminate(pStack)){ printf("%d", moves); break; }

			if (pStack[0] == '+'){
				while (true){
					if (pStack[++j] == '-' || j == strlen(pStack)){
						flip(pStack, j - 1); moves++; break;
					}
				}
			} else {
				while (true){
					if (pStack[++j] == '+' || j == strlen(pStack)){
						flip(pStack, j - 1); moves++; break;
					}
				}
			}
		}
		
	}

	return 0;
}