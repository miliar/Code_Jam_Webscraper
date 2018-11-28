#include <stdio.h>
#include <string.h>

int T;

char S[1001];

char RESULT[1001];
//printf("%d : S(%s)\n", result, str);
int main(){
	freopen("sample.in", "r", stdin);
	FILE * pFile;
  
	pFile = fopen ("sample.out","w");


	scanf("%d", &T);
	printf("T = %d\n", T);
	for(int t=1; t<=T; t++){
		printf("Test %d start --------------\n", t);
		scanf("%s", &S);
		printf("S = %s \n", S);
		int len = strlen(S);
		printf("len = %d \n", len);
		for(int i=0; i< 1001; i++){					
			RESULT[i]= 0;
		}

		int currentPos = 0;

		RESULT[currentPos] = S[currentPos];
		currentPos = 1;
		for(; currentPos < len; currentPos++){
			if(S[currentPos] >= RESULT[0]){
				for(int i=currentPos; i>=0 ; i--){					
					RESULT[i+1] = RESULT[i];
				}
				RESULT[0] = S[currentPos];
			} else {
				RESULT[currentPos] = S[currentPos];
			}
		}

		printf("Case #%d: %s\n", t , RESULT);
		if(t == T){
			printf("Case #%d: %s", t , RESULT);
		fprintf (pFile, "Case #%d: %s", t , RESULT);
		}
		else {
			printf("Case #%d: %s\n", t , RESULT);
		fprintf (pFile, "Case #%d: %s\n", t , RESULT);
		}
	}	

	fclose(stdin);
	fclose (pFile);
	return true;
}
