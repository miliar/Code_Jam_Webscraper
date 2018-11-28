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
	FILE* fp = fopen("A-large.in", "r");
	FILE* ofp = fopen("codejam_one_output.txt", "w");

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

		//0) 결과 스트링 배열 생성
		int sleep[10]; for (int k = 0; k < 10; k++) sleep[k] = 0;

		//1) N 추출
		char N[100]; memset(N, NULL, 100);
		fgets(N, 100, fp);
		//printf("%s",N);

		if (strcmp(N, "0\n") == 0){
			sprintf(output, "Case #%d: INSOMNIA\n", i + 1);
		}
		else{
			//2) N 스트링 분석
			int number = 0;
			int mul = 1;
			int backup_number = atoi(N);

			while (check_sleep(sleep) == false ){
				//str to int 변환
				number = backup_number * mul;

				//int to str 변환
				memset(N, NULL, 100);
				sprintf(N, "%d", number);

				//변화된 스트링 분석
				analysis_string(N, sleep);

				//곱
				mul++;
			}
			sprintf(output, "Case #%d: %d\n", i + 1, number);
		}
		fputs(output, ofp);
	}

}