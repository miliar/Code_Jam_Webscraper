#include <iostream>
#include <fstream>
#include <vector>
#include <stdlib.h>
#include <string.h>

const int N = 20002;

using namespace std;

char s[N];

int main() {

	char c;
	int k;
	const char* sv[] = {"ZERO", "TWO", "FOUR", "ONE", "THREE", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"};
	int nv[] = {0, 2, 4, 1, 3, 5, 6, 7, 8, 9};
	char cv[] = {'Z', 'W', 'U', 'O', 'R', 'F', 'X', 'S', 'T', 'I'};
	int alf[26];	
	int nr[10];
	
	//string s1, s2;
	int tst;
	scanf("%d", &tst);

	//printf ("%c %c %c %c\n", sv[0][3], sv[3][2], sv[5][2], sv[8][4]);//o e v t
	for (int t = 0; t < tst; t++) {
		
		scanf("%s", s);
		int n = strlen(s);
		
		memset (alf, 0, sizeof(alf));
		memset (nr, 0, sizeof(nr));
		for (int i = 0; i < n; i++) {
			alf[s[i] - 'A']++; 	
		}	
		
		/*
		for (int i = 0; i < 26; i++) {
			if (alf[i])
				printf("%c %d %d\n", i+'A', i, alf[i]);	
		}
		*/	
	
		for (int i = 0; i < 10; i++) {
			c = cv[i] - 'A';
			k = alf[c];
			//printf("%c %d %d\n", cv[i], k, c);
			if (k) {
				nr[nv[i]] = k;
				for (int j = 0; j < strlen(sv[i]); j++) {
					alf[sv[i][j] - 'A'] -= k;				
				}		
			}
		}

		printf("Case #%d: ", t+1);
		for (int i = 0; i < 10; i++) {
			k = nr[i];
			for (int j = 0; j < k; j++)
				printf("%d", i);		
		}
		printf("\n");
	}
	
	return 0;
}
