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
	FILE* fp = fopen("D-small-attempt0.in", "r");
	FILE* ofp = fopen("codejam_four_output.txt", "w");

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

		memset(output, NULL, 100);

		//1) ����
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

		//2) ���� ����
		//(��) ������ �� �ִ� ������ 1��, ������ ���� 1�����
		if (K == 1){
			sprintf(output, "Case #%d: %d\n", i + 1, 1);
			fputs(output, ofp);
			continue;
		}
		//(��) ���� 1�ε� �������� ������ �� �ִ� ������ ���ٸ�
		if (K >= 2 && C == 1 && S < K){
			sprintf(output, "Case #%d: IMPOSSIBLE\n", i + 1);
			fputs(output, ofp);
			continue;
		}
		//(��) ��ȭ�� �˰���
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