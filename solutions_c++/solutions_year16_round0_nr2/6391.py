#include<stdio.h>
//#include<string.h>

int hotCakeFlipper(char pancakes[], int strLength)
{
//	printf("\nstrLength = %d\n", strLength);

	int flips = 0;
	for(int i = strLength - 1; i >= 0; i--){
		if(pancakes[i] == '-'){
			for(int j = i; j >= 0; j--){
				if(pancakes[j] == '-')
					pancakes[j] = '+';
				else if(pancakes[j] == '+')
					pancakes[j] = '-';
			}
			flips++;
		}
	}

	return flips;
}

int main(){
	FILE *fp, *fp2;
	fp = fopen("B-large.in", "r");
	fp2 = fopen("pancakesOut.txt", "w");

	int testCases;
	fscanf(fp, "%d", &testCases);
//	printf("testCases = %d\n", testCases);

	char c;
	fscanf(fp, "%c", &c);

	for(int i = 0; i < testCases; i++){
		char pancakes[101];
		int strLength = 0;
		c = 'z';
		while(c != '\n'){
			fscanf(fp, "%c", &c);
			if(feof(fp))
				break;
			if(c == '+' || c == '-'){
//				printf("%c", c);
				pancakes[strLength] = c;
				strLength++;
			}
		}

		int flips = hotCakeFlipper(pancakes, strLength);
		fprintf(fp2, "Case #%d: %d\n", i + 1, flips);
	}

	fclose(fp);
	fclose(fp2);

	return 0;
}