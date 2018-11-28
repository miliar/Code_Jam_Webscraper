#include <stdio.h>
#include <stdlib.h>

int main(){
	FILE* f = fopen("MushroomMonsterLargeInput.txt", "r");
	FILE* output = fopen("output.txt", "w");

	int testcase;
	fscanf(f,"%d", &testcase);

	for (int j = 0; j < testcase; j++){
		int count;
		fscanf(f, "%d", &count);
		
		int mush[10000] = { 0, };
		
		for (int i = 0; i < count; i++){
			fscanf(f, "%d", &mush[i]);
		}
		
		//strategy 1
		int sum1 = 0;
		for (int i = 0; i < count - 1; i++){
			if (mush[i] - mush[i + 1] > 0){
				sum1 += mush[i] - mush[i + 1];
			}
		}
		//strategy 2
		int sum2 = 0;
		int maxGap = 0;
		//find maxGap
		for (int i = 0; i < count - 1; i++){
			if (mush[i] - mush[i + 1] > maxGap){
				maxGap = mush[i] - mush[i + 1];
			}
		}

		for (int i = 0; i < count - 1; i++){
			if (mush[i] >= maxGap){
				sum2 += maxGap;
			}
			else{
				sum2 += mush[i];
			}
		}
		
		
		fprintf(output,"Case #%d: %d %d\n", j+1, sum1, sum2);
	}


	fclose(f);
	fclose(output);
	return 0;

}