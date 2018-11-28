// LawnGrassCutting.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include "conio.h"
#include <stdlib.h>   // For _MAX_PATH definition
#include <stdio.h>
#include <malloc.h>
#include <string.h>

typedef struct {
	int M;
	int N;
	int *data;
	int *dataCopy;
}TestCaseT;

bool CanWeGoAhead(int* needed, int*current, int M, int N){
	for (int n=0; n<N; n++){
		for (int m=0; m<M; m++){
			if (current[(n*M)+m] < current[(n*M)+m]){
				fprintf(stderr,"M:%d N:%d m:%d n:%d Not trimmable", M, N, m, n);
				return false;
			}
		}
	}
	return true;
}

void GetTrimmableToLength(int* data, int M, int N, int currRow, int currCol, int currLen, bool * TrimmableRow, bool * TrimmableCol){

	*TrimmableRow = true;
	*TrimmableCol = true;
	for (int col=0; col<M; col++){
		if (data[(currRow*M)+col] > currLen){
			*TrimmableRow = false;
			break;
		}
	}
	for (int row=0; row<N; row++){
		if (data[(row*M)+currCol] > currLen){
			*TrimmableCol = false;
			break;
		}
	}
	return;
}

bool TrimLawnToThisLength(int* data, int* CurrentData, int M, int N, int TrimLen){
	for (int k=0; k<N; k++ ){
		for (int l=0; l<M; l++ ){
			if (data[(k*M)+l] == TrimLen){
				bool TrimmableRow = false;
				bool TrimmableCol = true;
				GetTrimmableToLength(data, M, N, k, l,TrimLen,&TrimmableRow,&TrimmableCol);
				if ((false == TrimmableCol) && (false == TrimmableRow)){
					fprintf(stderr,"M:%d N:%d m:%d n:%d Not trimmable to len:%d\n", M, N, l, k,TrimLen);
					return false;
				}
				if (true == TrimmableRow){
					for (int col=0; col<M; col++){
						CurrentData[(k*M)+col] = TrimLen;
					}
				}
				if (true == TrimmableCol){
					for (int row=0; row<N; row++){
						CurrentData[(row*M)+l] = TrimLen;
					}
				}

			}
		}
	}
	return true;
}

int _tmain(int argc, _TCHAR* argv[])
{
	int NoOfTests = 0;

	FILE* fileInput = NULL;
	FILE* fileOutput = NULL;
	char fileName[300] = {0};

	sprintf_s(fileName, 300, "%S", argv[1]);
	fopen_s(&fileInput, fileName, "r");
	if (fileInput == NULL){
		fprintf(stderr, "%s FILE INPUT OPEN FAILED", fileName );
		return 0;
	}
	sprintf_s(fileName, 300, "%S", argv[2]);
	fopen_s(&fileOutput, fileName, "w");
	if (fileOutput == NULL){
		fprintf(stderr, "%s FILE OUTPUT OPEN FAILED", fileName);
		fclose(fileInput);
		return 0;
	}

	fscanf_s(fileInput, "\n%d", &NoOfTests);
	//NoOfTests= 5;
	fprintf(stderr, "NoOfTests=%d Size=%d\n",NoOfTests, NoOfTests*sizeof(TestCaseT));
	TestCaseT* TestCase = (TestCaseT*) malloc(NoOfTests*sizeof(TestCaseT));
	
	for (int i=0; i<NoOfTests; i++){
		fscanf_s(fileInput, "%d %d", &(TestCase[i].N), &(TestCase[i]).M);
		int AllocationSize = (TestCase[i].M)*(TestCase[i].N)*(sizeof(int));
		//fprintf(stderr, "N=%d M=%d size=%d TestNo=%d\n",TestCase[i].N,TestCase[i].M, AllocationSize, i+1);
		
		TestCase[i].data = new int[AllocationSize];
		if (TestCase[i].data == NULL){
			fprintf(stderr, "Malloc failed\n");
			_getch();
			return 0;
		}
		TestCase[i].dataCopy = new int[AllocationSize];
		if (TestCase[i].dataCopy == NULL){
			fprintf(stderr, "Malloc failed\n");
			_getch();
			return 0;
		}
		memset(TestCase[i].data, 0, TestCase[i].M*TestCase[i].N*sizeof(int));
		memset(TestCase[i].dataCopy, 0, TestCase[i].M*TestCase[i].N*sizeof(int));
		for (int n=0; n<TestCase[i].N; n++){
			//fscanf_s(fileInput, "\n%d %d %d", &(TestCase[i].data[(n*TestCase[i].N) + 0]), &(TestCase[i].data[(n*TestCase[i].N) + 1]), &(TestCase[i].data[(n*TestCase[i].N) + 2]));
			//fprintf(stderr, "ReadRow:");
			for (int m=0; m<TestCase[i].M; m++){
				int number;
				if (m==0){
					fscanf_s(fileInput, "\n%d", &number);
				}else{
					fscanf_s(fileInput, "%d", &number);
				}
				if (number<1 || number >100){
					fprintf(stderr, "invalid input %d", number);
					return 1;
				}
				TestCase[i].data[(n*TestCase[i].M) + m] = number;
				TestCase[i].dataCopy[(n*TestCase[i].M) + m] = 100;
				//fprintf(stderr, " %d", number);
			}
			//fprintf(stderr, "\n");
		}
	}

	//fprintf(stderr, "%d", NoOfTests);
	//for (int i=0; i<NoOfTests; i++){
	//	fprintf(stderr, "\n%d %d", (TestCase[i].N), (TestCase[i]).M);
		//for (int n=0; n<TestCase[i].N; n++){
		//	for (int m=0; m<TestCase[i].M; m++){
		//		if (m==0)
		//			fprintf(stderr, "\nn=%d m=%d N=%d M=%d 0x%x (%d)%d",n,m,TestCase[i].N,TestCase[i].M,TestCase[i].data, (n*TestCase[i].M) + m, (TestCase[i].data[(n*TestCase[i].M) + m]));
		//		else
		//			fprintf(stderr, "n=%d m=%d N=%d M=%d  0x%x (%d)%d",n,m,TestCase[i].N,TestCase[i].M,TestCase[i].data, (n*TestCase[i].M) + m, (TestCase[i].data[(n*TestCase[i].M) + m]));
		//	}
		//}
		//for (int n=0; n<TestCase[i].N; n++){
		//	for (int m=0; m<TestCase[i].M; m++){
		//		if (m==0)
		//			fprintf(stderr, "\n%d", (TestCase[i].dataCopy[(n*TestCase[i].N) + m]));
		//		else
		//			fprintf(stderr, " %d", (TestCase[i].dataCopy[(n*TestCase[i].N) + m]));
		//	}
		//}
	//}
	//fprintf(stderr, "\n");

	for (int i=0; i<NoOfTests; i++){
		bool Trimmable = true;
		int M = TestCase[i].M;
		int N = TestCase[i].N;
		int* data = TestCase[i].data;
		int* dataCopy = TestCase[i].dataCopy;
		int lengthsNeeded[100] = {0,};
		
		memset(lengthsNeeded, 0, 100*sizeof(int));
		for (int k=0; k<(M*N); k++){
			if (data[k]<1 || data[k] >100){
				fprintf(stderr, " Invalid M=%d N=%d k=%d data=%d\n",M,N, k, data[k]);
				return 1;
			}
			lengthsNeeded[data[k]-1] = 1;
		}
		fprintf(stderr, "%d %d", (TestCase[i].N), (TestCase[i]).M);
		for (int n=0; n<TestCase[i].N; n++){
			for (int m=0; m<TestCase[i].M; m++){
				if (m==0)
					fprintf(stderr, "\n%d", (data[(n*M) + m]));
				else
					fprintf(stderr, "%d", (data[(n*M) + m]));
			}
		}
		fprintf(stderr,"\n");

		//fprintf(stderr, "Data=");
		//for (int k=0; k<(M*N); k++)
		//{
		//	if (data[k]<1 || data[k] >100){
		//		fprintf(stderr, " Invalid Data=0x%x  M=%d N=%d k=%d input %d", data, M,N,k, data[k]);
		//		return 1;
		//	}
		//	fprintf(stderr, " %d", TestCase[i].data[k]);
		//}
		//fprintf(stderr, " N=%d N=%d Lengths", M, N);
		//for (int j=100; j>0; j--){
		//	if (1 == lengthsNeeded[j-1]){
		//		fprintf(stderr, " %d", j);
		//	}
		//}
		//fprintf(stderr, " Needed\n");

		bool firstTrim = true;
		int lastTrimLength = 0;
		for (int j=100; j>0; j--){
			if ((1 == lengthsNeeded[j-1]) && (true == firstTrim)){
				for (int k=0; k<(M*N);k++ ){
					dataCopy[k] = j;
				}
				firstTrim = false;
				lastTrimLength = j;
				//fprintf(stderr, "Test:%d Trim to length %d Trimmable=%d\n", i+1, j, Trimmable);
			}else if (1 == lengthsNeeded[j-1]){
				Trimmable = TrimLawnToThisLength(data, dataCopy, M, N, j);
				if (false == Trimmable){
					//fprintf(stderr, "Test:%d Trim to length %d Trimmable1=%d\n", i+1, j, Trimmable);
					break;
				}
				Trimmable = CanWeGoAhead(data, dataCopy, M, N);
				if (false == Trimmable){
					fprintf(stderr, "Test:%d Trim to length %d Trimmable2=%d\n", i+1, j, Trimmable);
					return 1;
					break;
				}
				lastTrimLength = j;
				//fprintf(stderr, "Test:%d Trim to length %d Trimmable=%d\n", i+1, j, Trimmable);
			}
		}
		fprintf(fileOutput,"Case #%d: %s\n",i+1, ((Trimmable == true)?"YES":"NO"));
		fprintf(stderr,"Case #%d: %s\n",i+1, ((Trimmable == true)?"YES":"NO"));
	}

	for (int i=0; i<NoOfTests; i++){
		delete TestCase[i].data;
		delete TestCase[i].dataCopy;
	}
	
	delete TestCase;
	fclose(fileInput);
	fclose(fileOutput);
	return 0;
}

