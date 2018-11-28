#include <stdio.h>

int T;
int N;

bool A[10];
int count;
int result;

bool isClear(int N);

int main(){
	freopen("sample.in", "r", stdin);
	FILE * pFile;
  
	pFile = fopen ("sample.out","w");


	scanf("%d", &T);
	printf("T = %d\n", T);
	for(int t=1; t<=T; t++){
		printf("Test %d start --------------\n", t);
		scanf("%d", &N);
		printf("N = %d \n", N);
		for(int i=0; i<10; i++){
			A[i] = false;
		}
		count = 0;
		result = -1;
		int value = N;
		int multiple = 2;
		do{
			if(isClear(value)){
				result = value;
				break;
			} else {
				value = multiple*N;
				multiple++;
			}
		}while(N != 0);

		if(result == -1){
			printf("Case #%d: %s\n", t , "INSOMNIA");
			fprintf (pFile, "Case #%d: %s\n", t , "INSOMNIA");
		}
		else {
			printf("Case #%d: %d\n", t , result);
			fprintf (pFile, "Case #%d: %d\n", t , result);
		}
	}	

	fclose(stdin);
	fclose (pFile);
	return true;
}

bool isClear(int number){
	int d;
	do{
		d = number%10;
		number /= 10;
		if(!A[d]){
			A[d] = true;
			count++;
			if(count >= 10){
				return true;
			}
		}
	}while(number > 0);
	
	return false;
}