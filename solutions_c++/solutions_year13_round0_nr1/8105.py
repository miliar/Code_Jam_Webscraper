/***************************************************************************
 * 
 * Copyright (c) 2013, Inc. All Rights Reserved
 * 
 **************************************************************************/
 
 
 
/**
 * @file 1.cpp
 * @author liaoqiang
 * @date 2013/04/13 09:04:01
 * @brief 
 *  
 **/



#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main() {
	int T, case_no = 1;
	scanf("%d", &T);
	while (case_no <= T) {
		char status[4][4];
		char tmp;
		int is_full = 1, is_x_win = 0, is_o_win = 0;
		printf("Case #%d: ",case_no);
		scanf("%c", &tmp);
		for (int i = 0; i < 4; i ++) {
			for (int j = 0; j < 4; j++) {
				scanf("%c", &status[i][j]);
				//printf("%c", status[i][j]);
				if (status[i][j] == '.') {
					is_full = 0;
					//break;
				}
			}
			scanf("%c", &tmp);
			//printf("\n");
		}

		for (int i = 0; i < 4; i++) {
			if (status[i][0] == '.') {
				continue;
			}

			if (status[i][0] == status[i][1] && status[i][1] == status[i][2] && (status[i][2] == status[i][3] || status[i][3] == 'T')) {
				if (status[i][0] == 'X') {
					is_x_win = 1;
				}
				else {
					is_o_win = 1;
				}
				break;
			}
		}

		if (is_x_win) {
			printf("X won\n");
			case_no ++;
			continue;
		}
		else if (is_o_win) {
			printf("O won\n");
			case_no ++;
			continue;
		}

		for (int i = 0; i < 4; i ++) {
			if (status[0][i] == '.') {
				continue;
			}

			if (status[0][i] == status[1][i] && status[1][i] == status[2][i] && (status[2][i] == status[3][i] || status[3][i] == 'T')) {
				if (status[0][i] == 'X') {
					is_x_win = 1;
				}
				else {
					is_o_win = 1;
				}
				
				break;
			}
		}

		if (is_x_win) {
			printf("X won\n");
			case_no ++;
			continue;
		}
		else if (is_o_win) {
			printf("O won\n");
			case_no ++;
			continue;
		}

		if (status[0][0] != '.') {
			if (status[0][0] == status[1][1] && status[1][1] == status[2][2] && (status[2][2] == status[3][3] || status[3][3] == 'T')) {
				if (status[0][0] == 'X') {
					is_x_win = 1;
				}
				else {
					is_o_win = 1;
				}
			}
		}

		if (is_x_win) {
			printf("X won\n");
			case_no ++;
			continue;
		}
		else if (is_o_win) {
			printf("O won\n");
			case_no ++;
			continue;
		}

		if (status[0][3] != '.') {
			if (status[0][3] == status[1][2] && status[1][2] == status[2][1] && (status[3][0] == status[2][1] || status[3][0] == 'T')) {
				if (status[0][3] == 'X') {
					is_x_win = 1;
				}
				else {
					is_o_win = 1;
				}
			}
		}

		if (is_x_win) {
			printf("X won\n");
			case_no ++;
			continue;
		}
		else if (is_o_win) {
			printf("O won\n");
			case_no ++;
			continue;
		}

		if (is_full) {
			printf("Draw\n");
		}
		else {
			printf("Game has not completed\n");
		}
		case_no ++;
	}
	return 0;
}

















/* vim: set expandtab ts=4 sw=4 sts=4 tw=100: */
