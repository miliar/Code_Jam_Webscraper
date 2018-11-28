#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

int main(){
	int numCases, i, j, lowerLimit, upperLimit, numFS = 0, tens, ones, temp = 0;
	double root;
	char tempStr[1001];
	FILE *outputFile;
	FILE *inputFile;

	//open the files for reading
	inputFile = fopen("input.txt", "r");
	outputFile = fopen("output.txt", "w");

	//terminate if file not found
	if(inputFile == NULL){
		puts("Cannot open file to read");
		return -1;
	}

	//read number of cases
	fgets(tempStr, 60, inputFile);

	//convert
	numCases = atoi(tempStr); 

	for(i = 0; i < numCases; i++){
		//scan the limits and convert to int
		fscanf(inputFile, "%s", tempStr);
		lowerLimit = atoi(tempStr);
		fscanf(inputFile, "%s", tempStr);
		upperLimit = atoi(tempStr);

		for(j = lowerLimit; j <= upperLimit; j++){
			if(j == 1 || j == 4 || j == 9){
				numFS++;
			}else{
				if (j > 120 && j < 1000){
					tens = j/100;
					ones = j%10;
					if (tens == ones){
						root = sqrt((double)j);
						temp = root;
						if(root == temp){
							tens = root/10;
							ones = (int)root%10;
							if(tens == ones){
								numFS++;
							}
						}
					}
				}
			}
		}
		fprintf(outputFile, "Case #%i: %i\n", i+1, numFS);
		numFS = 0;
	}

	fclose(inputFile);
	fclose(outputFile);
	return 0;
}