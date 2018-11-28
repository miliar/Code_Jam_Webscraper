#include<stdio.h>
#include<stdlib.h>
#include"MySTL_Header.h"
#include"MySTL_Digit_Header.h"
#include"MyStandard_File_Input_Output.h"

//Code Jam
#include"Qulification_Round.h"

//STL
#include<iostream>
#include<string>
#include<vector>
#include<stack> //stl queue
#include<queue> //stl stack
#include<algorithm> //stl sort
#include<string.h>
using namespace std; //왜 이게 없으면 STL 사용이 안돼?

#define _CRT_SECURE_NO_WARNINGS
#pragma warning(disable:4996) //이 줄을 추가하면 컴파일러가 경고를 내지 못하게 하는 역할을 합니다.

void main(void){

	/* 파일 열기 */
	FILE* fp = fopen("D-small-attempt0.in", "r");
	FILE* ofp = fopen("codejam_four_output.txt", "w");

	if (fp == NULL) { printf("fp open is failed\n"); return; }
	if (ofp == NULL) { printf("ofp open is failed\n"); return; }

	/* 전체 테스트 케이스 찾기 */
	char T[10]; memset(T, NULL, 10);
	int testcase;
	fgets(T, 10, fp);
	testcase = atoi(T);
	
	char output[100]; memset(output, NULL, 100);

	/* 테스트 케이스에 따른 루프 뼈대 */
	for (int i = 0; i < testcase; i++){

		memset(output, NULL, 100);

		//1) 추출
		char str[100]; memset(str, NULL, 100);
		fgets(str, 100, fp);

		char *ptr = strtok(str, " ");
		int count = 0;
		int K = 0; int C = 0; int S = 0;
		while (ptr != NULL){
			switch (count){
			case 0:
				K = atoi(ptr);
				break;
			case 1:
				C = atoi(ptr);
				break;
			case 2:
				S = atoi(ptr);
				break;
			}
			ptr = strtok(NULL, " ");
			count++;
		}

		printf("%d %d %d %d\n", K, C, S, i);

		//2) 배제 조건
		//(ㄱ) 선택할 수 있는 여지도 1나, 선택할 곳도 1나라면
		if (K == 1){
			sprintf(output, "Case #%d: %d\n", i + 1, 1);
			fputs(output, ofp);
			continue;
		}
		//(ㄴ) 깊이 1인데 선택지가 선택할 수 있는 수보다 많다면
		if (K >= 2 && C == 1 && S < K){
			sprintf(output, "Case #%d: IMPOSSIBLE\n", i + 1);
			fputs(output, ofp);
			continue;
		}
		//(ㄷ) 점화식 알고리즘
		if (K == S){
			sprintf(output, "Case #%d:", i + 1);
			fputs(output, ofp);
			for (int i = 1; i <= S; i++){
				sprintf(output, " %d", i);
				fputs(output, ofp);
			}
			fputs("\n", ofp);
		}
	}
}