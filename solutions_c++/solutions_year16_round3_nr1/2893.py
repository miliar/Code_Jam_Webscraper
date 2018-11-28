#include <stdio.h>
#include <iostream>
#include <math.h>
#include <string.h>

int main(){
	int T;
	int N;
	int P[26];
	int a, b, c;
	int remove1;
	int remove2;
	int check = 0;
	int checkRatio = 0;
	int total;
	int ascii;
	char print;
	
	scanf("%d", &T);
	for(a = 0; a < T; a++){
		scanf("%d", &N);
		for(b = 0; b < N; b++){
			scanf("%d", &P[b]);
		}
		if(N == 2){
			printf("Case #%d: ", a + 1);
			while(P[0] != P[1]){
				if(P[0] > P[1]){
					P[0]--;
					printf("A ");
				}else{
					P[1]--;
					printf("B ");
				}
			}
			while(P[0] != 0){
				P[0]--;
				P[1]--;
				printf("AB ");
			}
		}else{
			printf("Case #%d: ", a + 1);
			check = 0;
			while(check == 0){
				total = 0;
				for(b = 0; b < N; b++){
					total = total + P[b];
				}
				if(total == N){
					for(b = N - 1; b > 1; b--){
						ascii = b + 65;
						print = ascii;
						printf("%c ", print);
					}
					printf("AB");
					break;
				}
				remove1 = 0;
				for(b = 0; b < N; b++){
					if(P[b] > P[remove1]){
						remove1 = b;
						
					}
				}
				P[remove1]--;
				ascii = remove1 + 65;
				print = ascii;
				printf("%c", print);
				
				remove2 = 0;
				for(b = 0; b < N; b++){
					if(P[b] > P[remove2]){
						remove2 = b;
					}
				}
				
				checkRatio = 0;
				for(b = 0; b < N; b++){
					if((double)P[b]/(double)total - 2 > 0.5){
						checkRatio = 1;
						break;
					}
				}
				
				if(checkRatio == 0 && (P[remove2] - 1) >= 0){
					P[remove2]--;
					ascii = remove2 + 65;
					print = ascii;
					printf("%c", print);
				}
				check = 1;
				for(b = 0; b < N; b++){
					if(P[b] != 0){
						check = 0;
						break;
					}
				}
				printf(" ");
			}
		}
		printf("\n");
	}
	return 0;
}
