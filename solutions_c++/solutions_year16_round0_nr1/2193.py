
#include <cstdio>
#include <algorithm>
#include <math.h>

using namespace std;

int findSleep(int n){
	if(n == 0)
	return -1;
	
	
	bool digits[10];
	for (int j = 0 ; j < 10 ; j++){
		digits[j] = false;
	}
	int count = 0;
	int k;
	int i = 0;
	while(count < 10){
		i++;
		k = n*i;
		while(k > 0){
			if(!digits[k%10]){
				count++;
				digits[k%10] = true;
			}
			k = k/10;
			
		}
		
	}
	
	return n*i;
}

int main()
{
	FILE * inputFile;
	FILE * outputFile;
	
	inputFile = fopen("A-large.in", "r");
	outputFile = fopen("output_A_Large.txt", "w");
	
	int tCase;
	int n;
	int result;
	fscanf (inputFile, "%d", &tCase);
	//printf("%d\n", tCase);
	
	for (int i = 1 ; i <= tCase ; i++){
		fscanf(inputFile, "%d", &n);
		result = findSleep(n);
		//printf("%d\n",result);
		if (result == -1)
			fprintf(outputFile, "Case #%d: INSOMNIA\n", i);
		else
			fprintf(outputFile, "Case #%d: %d\n", i, result);
		 
	} 
	
	fclose(inputFile);
	fclose(outputFile);
	
	return 0;
}


