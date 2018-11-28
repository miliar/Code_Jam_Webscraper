#include<stdio.h>
#define maxLength 1001

int main(){
	FILE *fp, *fp2;
	fp = fopen("A-large.in", "r");
	fp2 = fopen("Output.txt", "w");

	int testCases;
	fscanf(fp, "%d", &testCases);

	char c;
	fscanf(fp, "%c", &c);

	for(int i = 0; i < testCases; i++){
		fprintf(fp2, "Case #%d: ", i + 1);
		fscanf(fp, "%c", &c);
		
		char str[maxLength];
		char strModified[maxLength];
		int counter = 0;

		while(c!= '\n' && !feof(fp)){
//			printf("%c", c);
			str[counter] = c;
			counter++;
			fscanf(fp, "%c", &c);
		}
//		printf("Counter = %d\n", counter);
		
//		for(int j = 0; j < counter; j++)
//			printf("%c", str[j]);

//		printf("\n");
		
		strModified[0] = str[0];
		for(int j = 1; j < counter; j++){
//			printf("\n%c\n", str[j]);
			if(str[j] > strModified[0] || str[j] == strModified[0]){
				for(int k = j; k > 0; k--)
					strModified[k] = strModified[k - 1];
				strModified[0] = str[j];
//				printf("\n%c\n", strModified[j]);
			}
			else if(str[j] < strModified[0])
				strModified[j] = str[j];
		}

		for(int j = 0; j < counter; j++)
			fprintf(fp2, "%c", strModified[j]);

		fprintf(fp2, "\n");

	}

	fclose(fp);
	fclose(fp2);

	return 0;
}