#include<stdio.h>
#include<math.h>
#include<iostream>
#include<string.h>

int main(){
	int T;
	int n;
	int i;
	char S[1010];
	char lastWord[1010];
	int length;
	int len2;
	int a, b;
	int g, h;
	
	scanf("%d", &T);
	for(i = 0; i < T; i++){
		scanf("%s", S);
		length = strlen(S);
		for(a = 0; a < 1010; a++){
			lastWord[a] = '\0';
		}
		for(a = 0; a < length; a++){
			if(a == 0){
				lastWord[0] = S[0];
				continue;
			}
			if(S[a] >= lastWord[0]){
				len2 = strlen(lastWord);
				for(b = len2 - 1; b >= 0; b--){
					lastWord[b + 1] = lastWord[b];
				}
				lastWord[0] = S[a];
			}else{
				lastWord[a] = S[a];
			}
		}
		printf("Case #%d: ", (i + 1));
		puts(lastWord);
	}
}
