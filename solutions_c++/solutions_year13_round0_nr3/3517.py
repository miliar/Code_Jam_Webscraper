// FairAndSquares.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include "conio.h"
#include <stdlib.h>   // For _MAX_PATH definition
#include <stdio.h>
#include <malloc.h>
#include <string.h>
#include <math.h>

#define MAX_NUM_LEN 102
typedef struct{
	char minNum[MAX_NUM_LEN];
	char maxNum[MAX_NUM_LEN];
}TestCaseT;

typedef enum {
	NUM1_IS_GREATER,
	NUM1_EQUAL_NUM2,
	NUM2_IS_GREATER,
}CompareResultT;

void CalculateSquare(char* inputNumber,char* SqrNum);
void IncrementNumber(char* Num);
void DecrementNumber(char* Num);

char* compareResultString[3] = {"num1", "equal", "num2"};
CompareResultT CompareTwoNumbers(char* Num1, char* Num2){
	char* n1;
	char* n2;
	int startIndex =0;
	startIndex = 0;
	while (Num1[startIndex] == '0'){
		startIndex++;
	}
	n1 = &Num1[startIndex];

	startIndex = 0;
	while (Num2[startIndex] == '0'){
		startIndex++;
	}
	n2 = &Num2[startIndex];
	//fprintf(stderr, "nnumberToCompare=%s and %s\n", n1, n2);
	if (strlen(n2) > strlen(n1))
		return NUM2_IS_GREATER;
	else if (strlen(n1) > strlen(n2))
		return NUM1_IS_GREATER;
	else{
		for (unsigned int i = 0; i<strlen(n1); i++){
			if (n1[i]>n2[i]){
				return NUM1_IS_GREATER;
			}else if (n2[i]>n1[i]){
				return NUM2_IS_GREATER;
			}
		}
	}
	return NUM1_EQUAL_NUM2;
}
bool CompareNumbers(char* Num1, char* Num2){
	int len1 = strlen(Num1);
	int len2 = strlen(Num2);
	char* bigNum = NULL;
	char* smallNum = NULL;
	int smallNumLen = 0;
	int bigNumLen = 0;
	if (len1>len2){
		bigNum = Num1;
		bigNumLen = len1;
		smallNum = Num2;
		smallNumLen = len2;
	}else{
		bigNum = Num2;
		bigNumLen = len2;
		smallNum = Num1;
		smallNumLen = len1;
	}
	int diff = bigNumLen-smallNumLen;
	for (int i = 0; i<diff; i++){
		if (bigNum[i]!='0')
			return false;
	}
	if (0==strcmp(bigNum+diff, smallNum)){
		return true;
	}else{
		return false;
	}

}
bool IncrementNumNTellCarry(char *c){
	if (*c == '9'){
		*c = '0';
		return true;
	}
	else{
		*c = *c + 1;
		return false;
	}
}
bool DecrementNumNTellCarry(char *c){
	if (*c == '0'){
		*c = '9';
		return true;
	}
	else{
		*c = *c - 1;
		return false;
	}
}
int AddDigitNTellCarry(char *number, int numToAdd){
	int carry = numToAdd/10;
	numToAdd = numToAdd%10;
	char prevNum = *number;

	if (((*number) + numToAdd) > '9'){
		carry++;
		*number = (*number) - 10 + numToAdd;
	}else{
		*number = (*number) + numToAdd;
	}
	//fprintf(stderr, "carry=%d PrevNum=%c NowNum=%c ToAdd=%d\n", carry, prevNum, *number,numToAdd );
	return carry;
}
void FindNextSqrt(char* Num,  char* nextSqrt){
	char* n=NULL;
	int startIndex = 0;
	while (Num[startIndex] == '0'){
		startIndex++;
	}
	n = &Num[startIndex];

	int numOfDigits = strlen(n);
	int numofDigitsInStartNum = 0;
	char startNum[MAX_NUM_LEN] = {0};
	char startNumRefForEveb[4] = {'3','1','6','2'};
	startNum[0] = '0';
	numofDigitsInStartNum = numOfDigits/2;
	if (0 == (numOfDigits%2)){
		/*even*/
		for (int i=1;i<=numofDigitsInStartNum;i++){
			if (i<=4)
				startNum[i] = startNumRefForEveb[i-1];
			else
				startNum[i] = '0';
		}
	}else{
		/*odd*/
		for (int i=1;i<=(numofDigitsInStartNum+1);i++){
			if (i==1)
				startNum[i] = '1';
			else
				startNum[i] = '0';
		}
	}

	char SquareOfStartNum[MAX_NUM_LEN] = {0};
	CompareResultT compareResult;
	for (;;){
		CalculateSquare(startNum,SquareOfStartNum);
		compareResult = CompareTwoNumbers(Num, SquareOfStartNum);
		if ((NUM2_IS_GREATER == compareResult )|| (NUM1_EQUAL_NUM2== compareResult)){
			break;
		}
		IncrementNumber(startNum);
	}
	memcpy(nextSqrt, startNum, MAX_NUM_LEN);
	//fprintf(stderr, "Next squarert no is %s\n", nextSqrt);
	return;
}
void FindPrevSqrt(char* Num,  char* nextSqrt){
	char* n=NULL;
	int startIndex = 0;
	while (Num[startIndex] == '0'){
		startIndex++;
	}
	n = &Num[startIndex];

	int numOfDigits = strlen(n);
	int numofDigitsInStartNum = 0;
	char startNum[MAX_NUM_LEN] = {0};
	char startNumRefForEveb[1] = {'4'};
	startNum[0] = '0';
	numofDigitsInStartNum = (numOfDigits)/2;
	if (0 == (numOfDigits%2)){
		/*even*/
		startNum[1] = '1';
		for (int i=1;i<=numofDigitsInStartNum;i++){
				startNum[i+1] = '0';
		}
	}else{
		/*odd*/
		for (int i=1;i<=(numofDigitsInStartNum +1);i++){
			if (i==1)
				startNum[i] = startNumRefForEveb[0];
			else
				startNum[i] = '0';
		}
	}

	char SquareOfStartNum[MAX_NUM_LEN] = {0};
	CompareResultT compareResult;
	for (;;){
		CalculateSquare(startNum,SquareOfStartNum);
		compareResult = CompareTwoNumbers(Num, SquareOfStartNum);
		if ((NUM1_IS_GREATER == compareResult )|| (NUM1_EQUAL_NUM2== compareResult)){
			break;
		}
		DecrementNumber(startNum);
	}
	memcpy(nextSqrt, startNum, MAX_NUM_LEN);
//	fprintf(stderr, "prev squarert no is %s\n", nextSqrt);
	return;
}
void IncrementNumber(char* Num){
	int length = strlen(Num);
	for(int i=(length-1); i>=0; i--){
		if (false == IncrementNumNTellCarry(&Num[i]))
			break;
	}
}
void DecrementNumber(char* Num){
	int length = strlen(Num);
	for(int i=(length-1); i>=0; i--){
		if (false == DecrementNumNTellCarry(&Num[i]))
			break;
	}
}
void CalculateSquare(char* inputNumber,char* SqrNum){
	char* n;
	char result[MAX_NUM_LEN] = {0};
	int startIndex =0;
	int length =0;

	startIndex = 0;
	while (inputNumber[startIndex] == '0'){
		startIndex++;
	}
	n = &inputNumber[startIndex];

	length = strlen(n);
	int k=0, l=0;
	memset(SqrNum, 0, MAX_NUM_LEN);
	memset(result, '0', MAX_NUM_LEN);
	//fprintf(stderr, "square of:%s needed length=%d\n", n, length);
	if (length == 0){
		memset(SqrNum, '0', 1);
		return;
	}
	for (int i=0; i<length;i++){
		for (int j=0; j<length;j++){
			k=length-i-1;
			l=length-j-1;
			int count = 0;
			int val = (n[k]-'0')*(n[l]-'0');
			int carry = AddDigitNTellCarry(&result[i+j+count], val);
			//fprintf(stderr, "carry=%d i=%d j=%d  k=%d l=%d for input=%s val[%d]=%c\n",carry, i , j, k , l, n, i+j+count,result[i+j+count] );
			count++;
			while(carry!=0){
				carry = AddDigitNTellCarry(&result[i+j+count], carry);
				//fprintf(stderr, "carry=%d i=%d j=%d  k=%d l=%d val[%d]=%c\n",carry, i , j, k , l, i+j+count,result[i+j+count] );
				count++;
			}
		}
	}
	length= MAX_NUM_LEN;
	for (int i=(MAX_NUM_LEN-1); i>=0;i--){
		if (result[i]=='0') length--;
		else
			break;
	}

	for (int i=0; i<length;i++)
	{
		SqrNum[length-i-1] = result[i];
	}
	SqrNum[length] = 0;
	//fprintf(stderr, "square of:%s is %s length=%d\n", n, SqrNum,length);
}

bool IsPalin(char* Num){
	int startIndex = 0;
	while (Num[startIndex] == '0'){
		startIndex++;
	}
	int length = strlen(&Num[startIndex]);
	for (int i=0;i<length;i++){
		if ( Num[startIndex+i] != Num[startIndex+length-1-i]){
			return false;
		}
	}
	return true;
}

bool isPalin(long unsigned int n) {
	long unsigned int  rev=0,num,digit;
    num=n;
    while(n!=0)
    {
        digit=n%10;
        rev=(rev*10)+digit;
        n=n/10;
    }
    if(rev == num)
		return true;
    else
		return false;
}
	
bool isPerfectRoot(long unsigned int n){
	float p ;   
	long unsigned int m;
	p = sqrt((float)(n)) ;   
	m = (long unsigned int)p ;   
	if (p == m)   
		return true;
	else   
		return false;
}

int _tmain(int argc, _TCHAR* argv[])
{	
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

	int NoOfTests = 0;
	fscanf_s(fileInput, "\n%d", &NoOfTests);
	//fprintf(stderr, "NoOfTests=%d Size=%d\n",NoOfTests, NoOfTests*sizeof(TestCaseT));
	TestCaseT* TestCase = (TestCaseT*) malloc((NoOfTests+1)*sizeof(TestCaseT));
	
	for (int i=0;i<(NoOfTests+1);i++){
		bool isFirstNum = true;
		int index = 1;
		char* buffer = NULL;
		memset(TestCase[i].minNum, 0,MAX_NUM_LEN );
		memset(TestCase[i].maxNum, 0,MAX_NUM_LEN );
		TestCase[i].minNum[0]='0';
		TestCase[i].maxNum[0]='0';
		char c=0;
		fread_s(&c, 1, 1, 1, fileInput);
		//fprintf(stderr,"Character read[%d] = %c\n",i ,c);
		while (c!=EOF && c!='\n'){
			if (isFirstNum == true){
				buffer = TestCase[i].minNum;
			}else{
				buffer = TestCase[i].maxNum;
			}
			if (c==' '){
				isFirstNum = false;
				index = 1;
			}else{
				buffer[index] = c;
				index++;
			}
			fread_s(&c, 1, 1, 1, fileInput);
			//fprintf(stderr,"Character read[%d] = %c\n",i ,c);
		}
		//fprintf(stderr," \n");
	}
	for (int i=1;i<=NoOfTests;i++){
		char sqr1[MAX_NUM_LEN] = {0,};
		char sqr2[MAX_NUM_LEN] = {0,};
		memcpy(sqr1, TestCase[i].minNum,MAX_NUM_LEN );
		memcpy(sqr2, TestCase[i].maxNum,MAX_NUM_LEN );
	}
	for (int i=1;i<=NoOfTests;i++){
		int foundFairNPalin = 0; 
		char MinSqrt[MAX_NUM_LEN] = {0,};
		char MaxSqrt[MAX_NUM_LEN] = {0,};
		char Sqr[MAX_NUM_LEN] = {0,};
		char TempMinSqrt[MAX_NUM_LEN] = {0,};
		memset(MinSqrt, 0,MAX_NUM_LEN );
		memset(MaxSqrt, 0,MAX_NUM_LEN );
		memset(Sqr, 0,MAX_NUM_LEN );
		FindNextSqrt( TestCase[i].minNum,  MinSqrt);
		//FindNextSqrt( TestCase[i].maxNum,  MaxSqrt);
		//fprintf(stderr, "for %s mins :%s for %s min:%s\n",TestCase[i].minNum,  MinSqrt, TestCase[i].maxNum, MaxSqrt);
		//FindPrevSqrt( TestCase[i].minNum,  MinSqrt);
		FindPrevSqrt( TestCase[i].maxNum,  MaxSqrt);
		memcpy(TempMinSqrt,MinSqrt, MAX_NUM_LEN);
		//fprintf(stderr, "for %s max :%s for %s max:%s\n",TestCase[i].minNum,  MinSqrt, TestCase[i].maxNum, MaxSqrt);
		while (NUM1_IS_GREATER!=CompareTwoNumbers(MinSqrt, MaxSqrt)){
			memset(Sqr, 0,MAX_NUM_LEN );
			CalculateSquare(MinSqrt,Sqr);
			if (IsPalin(Sqr) && IsPalin(MinSqrt)){
				fprintf(stderr, "Min=%s Max=%s MinSqrt=%s MaxSqrt=%s sqrt=%s FAIR AND PALIN=%s TestNo:%d\n"
					,TestCase[i].minNum,  TestCase[i].maxNum, TempMinSqrt,  MaxSqrt, MinSqrt, Sqr, i);
				foundFairNPalin++;
			}
			IncrementNumber(MinSqrt);
		}

		//long unsigned int vmin = 0;
		//long unsigned int vmax = 0;
		//char* temp = NULL;
		//int vlen = 0;

		//temp = TestCase[i].minNum;
		//vlen = strlen(TestCase[i].minNum);
		//for(int ii=0; ii<vlen;ii++){
		//	vmin=(10*vmin)+ (temp[ii]-'0');
		//}

		//temp = TestCase[i].maxNum;
		//vlen = strlen(TestCase[i].maxNum);
		//for(int ii=0; ii<vlen;ii++){
		//	vmax=(10*vmax)+ (temp[ii]-'0');
		//}

		//int countByStraightCalc = 0;
		//for (long unsigned int ii =vmin; ii<=vmax; ii++){
		//	if (isPalin(ii) && isPerfectRoot(ii)){
		//		fprintf(stderr, "%d test case found = %lu\n",i,ii);
		//		countByStraightCalc ++;
		//	}
		//}
		fprintf(fileOutput, "Case #%d: %d\n", i,foundFairNPalin);
		fprintf(stderr, "Case #%d: %d\n", i,foundFairNPalin);

		//if (countByStraightCalc!=foundFairNPalin){
		//	fprintf(stderr, "THIS TEST CASE = %d FAILED \n",i);
		//	_getch();
		//}else{
		//	fprintf(stderr, "THIS TEST CASE = %d SUCCESS \n",i);
		//	_getch();
		//}

//		_getch();
	}

	fclose(fileInput);
	fclose(fileOutput);
	return 0;
}

