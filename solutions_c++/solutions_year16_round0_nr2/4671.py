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
using namespace std; //�� �̰� ������ STL ����� �ȵ�?

#define _CRT_SECURE_NO_WARNINGS
#pragma warning(disable:4996) //�� ���� �߰��ϸ� �����Ϸ��� ��� ���� ���ϰ� �ϴ� ������ �մϴ�.

void main(void){

	/* ���� ���� */
	FILE* fp = fopen("B-large.in", "r");
	FILE* ofp = fopen("codejam_two_output.txt", "w");

	if (fp == NULL) { printf("fp open is failed\n"); return; }
	if (ofp == NULL) { printf("ofp open is failed\n"); return; }

	/* ��ü �׽�Ʈ ���̽� ã�� */
	char T[10]; memset(T, NULL, 10);
	int testcase;
	fgets(T, 10, fp);
	testcase = atoi(T);

	char output[100]; memset(output, NULL, 100);

	/* �׽�Ʈ ���̽��� ���� ���� ���� */
	for (int i = 0; i < testcase; i++){

		//0) ����
		char cake[200]; memset(cake, NULL, 200);
		fgets(cake, 200, fp);

		//1) �������� ��� �����Ѱ�
		if (check_all_happy(cake) == true){
			sprintf(output, "Case #%d: 0\n", i + 1);
			fputs(output, ofp);
			continue;
		}
		
		//2) ����
		char temp_cake[200]; memset(temp_cake, NULL, 200);
		compression_cake(cake, temp_cake);

		int len = strlen(temp_cake);

		//3) ������ ���̰� '-'�� ���� �״�� ����
		if (temp_cake[len-1] == '-'){
			sprintf(output, "Case #%d: %d\n", i + 1,len);
		}
		//4) ������ ���̰� '+'�� ��ü ���� -1
		else{
			sprintf(output, "Case #%d: %d\n", i + 1,len-1);
		}
		fputs(output, ofp);
	}

}