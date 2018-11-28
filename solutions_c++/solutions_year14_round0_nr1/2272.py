#include<cstdio>

int main(void)
{
	int runTimes;
	int volunteerAnswer;
	int possibleAnswers[4];
	int exactAnswers[4],numbersOfExactAnswers;
	
	scanf("%d",&runTimes);
	for(int nowTimes=1;nowTimes<=runTimes;++nowTimes){
		numbersOfExactAnswers=0;
		
		scanf("%d",&volunteerAnswer);
		for(int row=1;row<=4;++row){
			for(int column=1;column<=4;++column){
				int storeInput;
				scanf("%d",&storeInput);
				if(row==volunteerAnswer){
					possibleAnswers[column-1]=storeInput;
				}
			}
		}
		
		scanf("%d",&volunteerAnswer);
		for(int row=1;row<=4;++row){
			for(int column=1;column<=4;++column){
				int storeInput;
				scanf("%d",&storeInput);
				if(row==volunteerAnswer){
					for(int checkIfMatch=1;checkIfMatch<=4;++checkIfMatch){
						if(storeInput==possibleAnswers[checkIfMatch-1]){
							exactAnswers[numbersOfExactAnswers++]=storeInput;
						}
					}
				}
			}
		}
		
		printf("Case #%d: ",nowTimes);
		if(numbersOfExactAnswers>1){
			printf("Bad magician!");
		}
		else if(numbersOfExactAnswers==1){
			printf("%d",exactAnswers[0]);
		}
		else{
			printf("Volunteer cheated!");
		}
		printf("\n");
	}
	
	return 0;
}
