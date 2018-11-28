#include <stdio.h>
#include <string.h>

int T;

char S[101];

int result;
void arrage(char* str, int len);
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
		result = 0;
		int len = strlen(S);

		arrage(S, len);		

		printf("Case #%d: %d\n", t , result);
		fprintf (pFile, "Case #%d: %d\n", t , result);
	}	

	fclose(stdin);
	fclose (pFile);
	return true;
}

void arrage(char* str, int len){
	printf("%d : S(%s)\n", result, str);
	if(len == 1){
		if(str[len-1] == '-'){
			result++;
		}
		return;
	}

	int nextpos = 1;
	for(int i=len; i>0; i--){
		if(str[i-1] == '-'){
			nextpos = i;
			result++;
			for(int j = 0; j<i; j++){
				if(str[j] == '-')
					str[j] = '+';
				else
					str[j] = '-';
			}
			break;
		}
	}
	
	arrage(str, nextpos);
}