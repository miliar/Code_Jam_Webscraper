// Tic-Tac-Toe-Tomek.cpp : 定义控制台应用程序的入口点。
//

#include "stdafx.h"
#include <assert.h>
#include <string.h>

#define INPUT_FILE_NAME "A.in"
#define OUTPUT_FILE_NAME "A.out"

int _tmain(int argc, _TCHAR* argv[])
{
	FILE *fp_in = fopen(INPUT_FILE_NAME, "r");
	assert(fp_in);
	FILE *fp_out = fopen(OUTPUT_FILE_NAME, "w");
	assert(fp_out);
	
	int num = 0;
	fscanf(fp_in, "%d\n", &num);	
	char arr[4][4];
	for (int i = 0; i < num; ++i) {
		// 读入棋盘状态
		bool full = true;
		for (int j = 0; j < 4; ++j) {
			for (int k = 0; k < 4; ++k) {
				char ch;
				while(1) {
					ch = fgetc(fp_in);
					if ('T' == ch || 'O' == ch || 'X' == ch || '.' == ch)
						break;
				}
				if ('.' == ch)
					full = false;
				arr[j][k] = ch;
				putchar(ch);
			}
			putchar('\n');
		} 
		// 判断棋局状态
		int win = 0;  // 0:draw, 1:O win, -1:X win
		for (int c = 0; c <= 3; ++c) {
			int cr = 0;
			int rc = 0;
			for (int r = 0; r <= 3; ++r) {
				if (arr[c][r] == 'O' || arr[c][r] == 'T') {
					cr += 1;
				}
				if (arr[c][r] == 'X' || arr[c][r] == 'T') {
					cr += 16;
				}
				if (arr[r][c] == 'O' || arr[r][c] == 'T') {
					rc += 1;
				}
				if (arr[r][c] == 'X' || arr[r][c] == 'T') {
					rc += 16;
				}
			}
			if (((cr & 0xf) == 4) || ((rc & 0xf) == 4)) {
				win = 1;
				break;
			}
			if (((cr &0xf0) == 64) || ((rc & 0xf0) == 64)) {
				win = -1;
				break;
			}
		}
		int diag = 0;
		int gaid = 0;
		for (int x = 0; x < 4; ++x) {
			if (arr[x][x] == 'O' || arr[x][x] == 'T') {
				diag += 1;
			}
			if (arr[x][3-x] == 'O' || arr[x][3-x] == 'T') {
				gaid += 1;
			}
			if (arr[x][x] == 'X' || arr[x][x] == 'T') {
				diag += 16;
			}
			if (arr[x][3-x] == 'X' || arr[x][3-x] == 'T') {
				gaid += 16;
			}
		}
		if (((diag & 0xf) == 4) || ((gaid & 0xf) == 4)) {
			win = 1;
		}
		if (((diag &0xf0) == 64) || ((gaid & 0xf0) == 64)) {
			win = -1;
		}

		fprintf(fp_out, "Case #%d: ",i+1);
		if (win == 1)
			fprintf(fp_out, "O won\n");
		else if (win == -1)
			fprintf(fp_out, "X won\n");
		else if (full == true)
			fprintf(fp_out, "Draw\n");
		else 
			fprintf(fp_out, "Game has not completed\n");
	}
	fclose(fp_in);
	fclose(fp_out);
	return 0;
}

