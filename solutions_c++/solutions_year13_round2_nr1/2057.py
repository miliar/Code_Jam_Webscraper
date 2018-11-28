// Round1BProblem1.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include "Utilities.h"
#include "BigMathematics.h"
#include "conio.h"

void sortList(int *list, int listSize){
	int temp = 0;
	for (int i=0; i<(listSize-1); i++){
		for (int j=(i+1); j<listSize; j++){
			if (list[j] < list[i]){
				temp = list[i];
				list[i] = list[j];
				list[j] = temp;
			}
		}
	}
	//fprintf(stderr, "Sorted List:");
	//for (int i=0; i<listSize; i++){
	//	fprintf(stderr, "%d ", list[i]);
	//}
	//fprintf(stderr, "\n");
}
int GetNumberOfAddsNeeded(int Mote, int MoteToExceed, int * NewMoteValue){
	int result =0;
	int InitialMote = Mote;
	if (Mote == 1){
		//fprintf(stderr, "InitialMote:%d NeedToAdd=%d NewMote=%d\n", InitialMote, ~(1<<31), Mote);
		return ~(1<<31);
	}
	while(Mote<=MoteToExceed){
		Mote+=Mote-1;
		result++;
		//fprintf(stderr, "InLoop InitialMote:%d NeedToAdd=%d NewMote=%d\n", InitialMote, result, Mote);
	}
	*NewMoteValue = Mote;
	//fprintf(stderr, "InitialMote:%d NeedToAdd=%d NewMote=%d\n", InitialMote, result, Mote);

	return result;
}
void ProcessTestCase(int no, FILE* outFile, int Mote, int* MoteList, int NoOfMotes){
	int result = 0;
	sortList(MoteList, NoOfMotes);

	for (int i=0; i<NoOfMotes;i++){
		//fprintf(stderr, "[%d]Mote=%d ToExceed=%d\n",i, Mote, MoteList[i]);
		if (Mote > MoteList[i]){
			//fprintf(stderr, "[%d] Simply Add Mote=%d Made=%d\n",i, Mote, Mote+MoteList[i]);
			Mote +=  MoteList[i];
		}else{
			int noOfRemovesNeeded = NoOfMotes - i;
			int NewMoteValue = 0;
			int noOfAddsNeeded = GetNumberOfAddsNeeded(Mote, MoteList[i], &NewMoteValue);
			if (noOfRemovesNeeded <= noOfAddsNeeded){

				result += NoOfMotes-i;
				//fprintf(stderr, "RemoveIsGreater= %d Result+=%d noOfAddsNeeded=%d noOfRemovesNeeded=%d\n",i, NoOfMotes-i, noOfAddsNeeded, noOfRemovesNeeded);
				goto end;
			}else{
				result += noOfAddsNeeded;
				Mote=NewMoteValue+MoteList[i];
				//fprintf(stderr, "noOfAddsNeededIsLess %d Result+=%d noOfAddsNeeded=%d noOfRemovesNeeded=%d\n",i, noOfAddsNeeded, noOfAddsNeeded, noOfRemovesNeeded);
			}
		}
	}
end:
	if (result>NoOfMotes)
		result = NoOfMotes;
	fprintf(outFile, "Case #%d: %d\n", no+1, result);
	//fprintf(stderr, "Case #%d: %d\n", no+1, result);
	return;
}
int _tmain(int argc, _TCHAR* argv[])
{
	char inputFile[_MAX_PATH];
	char outFile[_MAX_PATH];
	sprintf_s(inputFile,_MAX_PATH, "%S",  argv[1]);
	sprintf_s(outFile,_MAX_PATH, "%S",  argv[2]);
	printf("inFile=%s\n", inputFile);
	printf("outFile=%s\n", outFile);
	//Queue* queue = new Queue();
	//queue->PrintList();
	//char* result = MultiplyNumbers("9","1234");
	//printf("result=%s", result);
	//free(result);
	//delete queue;

	FILE* fileInput = NULL;
	FILE* fileOutput = NULL;

	fopen_s(&fileInput, inputFile, "r");
	if (fileInput == NULL){
		fprintf(stderr, "%s FILE INPUT OPEN FAILED", inputFile );
		return 0;
	}
	fopen_s(&fileOutput, outFile, "w");
	if (fileOutput == NULL){
		fprintf(stderr, "%s FILE OUTPUT OPEN FAILED", outFile);
		fclose(fileInput);
		return 0;
	}
	int NoOfTestCases = 0;
	fscanf_s(fileInput,"%d", &NoOfTestCases);
	fprintf(stderr,"No Of Test Cases:%d \n", NoOfTestCases);
	for (int i=0; i<NoOfTestCases;i++){
		int Mote;
		int NoOfMotes;
		int * motesList = NULL;
		fscanf_s(fileInput,"%d %d", &Mote, &NoOfMotes);
//		fprintf(stderr,"Mote:%d NoOfOtherMotes:%d\n", Mote, NoOfMotes);
//		fprintf(stderr,"Other Motes: ");
		motesList = (int*) malloc(NoOfMotes * sizeof (int));
		for (int j=0; j<NoOfMotes;j++){
			fscanf_s(fileInput,"%d ", &motesList[j]);
//			fprintf(stderr,"%d ", motesList[j]);
		}
		ProcessTestCase(i, fileOutput, Mote, motesList, NoOfMotes);
		free(motesList);

		fprintf(stderr, "Processed %d\n", i+1);
	}
	fclose(fileInput);
	fclose(fileOutput);
	return 0;
}

