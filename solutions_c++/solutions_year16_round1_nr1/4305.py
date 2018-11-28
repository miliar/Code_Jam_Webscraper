#include<stdio.h>
#include<stdlib.h>
#include"MySTL_Header.h"
#include"MySTL_Digit_Header.h"
#include"MyStandard_File_Input_Output.h"
#include"MyBigInteger_Header.h"

//Code Jam
#include"Qulification_Round.h"

//STL
#include<iostream>
#include<string>
#include<vector>
#include<stack> //stl queue
#include<queue> //stl stack
#include<deque>
#include<algorithm> //stl sort
#include<string.h>
using namespace std;

#define _CRT_SECURE_NO_WARNINGS
#pragma warning(disable:4996) //이 줄을 추가하면 컴파일러가 경고를 내지 못하게 하는 역할을 합니다.


/* Code Zam Declaration */

void main(void){

	FILE* fp = NULL;
	fp = fopen("1_2.in", "r");
	if (fp == NULL){
		printf("file open is failed 1\n");
		return;
	}

	FILE* ofp = NULL;
	ofp = fopen("Output-round1A-large-practice.txt", "w");
	if (ofp == NULL){
		printf("file open is failed 2\n");
		return;
	}

	//1) get test case
	char buf[5];
	memset(buf, NULL, 5);
	fgets(buf, 5, fp); //어차피 테스트 케이스는 100개 이상 안넘는다.
	int testcase = atoi(buf);

	printf("T: %d", testcase);

	for (int i = 1; i <= testcase; i++){ //testcase: N 50개 미만
	
		deque<char> deck;
		char string[1500]; memset(string, NULL, 1500);
		char result[1500]; memset(result, NULL, 1500);
		fgets(string, 1500, fp);
		printf("%d: %s",i, string);
		
		deck.push_front(string[0]);

		for (int j = 1; string[j] != NULL; j++){
			if (deck.front() > string[j]){
				deck.push_back(string[j]);
			}
			else{
				deck.push_front(string[j]);
			}
		}

		sprintf(result, "Case #%d: ",i);
		char cat[1500]; memset(cat, NULL, 1500);
		int k = 0;
		while (!deck.empty()){
			cat[k] = deck.front(); k++;
			deck.pop_front();
		}
		///printf("%s\n", cat);
		strcat(result, cat);
		fputs(result, ofp);
	}
}

/* Code Zam Definition */
