#include<stdio.h>
#include<string.h>
#include<stdlib.h>

int main(){
	FILE *f;
	FILE *fp;
	char S[101];
	int T, i, j, tmp;
	int len;
	int count;
	
	f = fopen("B-large.in", "r");
	fp = fopen("output3.txt", "w");
	
	fscanf(f, "%d", &T);
	
	//printf("%d\n", T);
	for(i = 1; i <= T; i++){
		count = 0;
		fscanf(f, "%s", S);
		len = strlen(S);
		//printf("len : %d\n", len);
		
		for(j = len-1; j >= 0; j --){
			if(S[j] == '-'){
				for(tmp = j; tmp >= 0; tmp --){
					if(S[tmp] == '-'){
						S[tmp] = '+';
					}else{
						S[tmp] = '-';
					}
				}
				//printf("%s\n", S);
				count ++;
			}			
		}
		
		fprintf(fp, "Case #%d: %d\n", i, count);
	}

}