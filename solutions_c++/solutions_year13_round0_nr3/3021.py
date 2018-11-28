#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <cmath>

void Output(int status, int case_num){
	FILE *f1;
	f1 = fopen("output.out", "a");
	fprintf(f1, "Case #%d: %d\n",case_num+1,status);
	fclose(f1);
}

int Numbers(int A, int B){
	int num;
	int total = 0;
	if((A<1001)&&(B<1001)){
		int nums[5];
		nums[0] = 1;
		nums[1] = 4;
		nums[2] = 9;
		nums[3] = 121;
		nums[4] = 484;
		for(int i=0; i<5; i++){
			if(B >= nums[i]){
				total++;
			}
			if(A > nums[i]){
				total--;
			}
		}

	}
	

	return total;
}

int main(){
	int num_cases;
	int A, B;
	FILE *f1;


	f1 = fopen("C-small-attempt0.in", "r");
	fscanf(f1, "%d\n", &num_cases);
	for(int i=0; i<num_cases; i++){
		fscanf(f1, "%d %d\n", &A, &B);
		Output(Numbers(A, B),i);
	}
	fclose(f1);



	return 0;
}