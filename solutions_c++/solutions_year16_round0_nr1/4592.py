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
	FILE* fp = fopen("A-large.in", "r");
	FILE* ofp = fopen("codejam_one_output.txt", "w");

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

		//0) ��� ��Ʈ�� �迭 ����
		int sleep[10]; for (int k = 0; k < 10; k++) sleep[k] = 0;

		//1) N ����
		char N[100]; memset(N, NULL, 100);
		fgets(N, 100, fp);
		//printf("%s",N);

		if (strcmp(N, "0\n") == 0){
			sprintf(output, "Case #%d: INSOMNIA\n", i + 1);
		}
		else{
			//2) N ��Ʈ�� �м�
			int number = 0;
			int mul = 1;
			int backup_number = atoi(N);

			while (check_sleep(sleep) == false ){
				//str to int ��ȯ
				number = backup_number * mul;

				//int to str ��ȯ
				memset(N, NULL, 100);
				sprintf(N, "%d", number);

				//��ȭ�� ��Ʈ�� �м�
				analysis_string(N, sleep);

				//��
				mul++;
			}
			sprintf(output, "Case #%d: %d\n", i + 1, number);
		}
		fputs(output, ofp);
	}

}