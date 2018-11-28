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
	FILE* fp = fopen("B-large.in", "r");
	FILE* ofp = fopen("codejam_two_output.txt", "w");

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

		//0) 추출
		char cake[200]; memset(cake, NULL, 200);
		fgets(cake, 200, fp);

		//1) 루프조건 모두 해피한가
		if (check_all_happy(cake) == true){
			sprintf(output, "Case #%d: 0\n", i + 1);
			fputs(output, ofp);
			continue;
		}
		
		//2) 압축
		char temp_cake[200]; memset(temp_cake, NULL, 200);
		compression_cake(cake, temp_cake);

		int len = strlen(temp_cake);

		//3) 마지막 길이가 '-'면 본연 그대로 길이
		if (temp_cake[len-1] == '-'){
			sprintf(output, "Case #%d: %d\n", i + 1,len);
		}
		//4) 마지막 길이가 '+'면 전체 길이 -1
		else{
			sprintf(output, "Case #%d: %d\n", i + 1,len-1);
		}
		fputs(output, ofp);
	}

}