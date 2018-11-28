/***************************************************************************
 * 
 * Copyright (c) 2013, Inc. All Rights Reserved
 * 
 **************************************************************************/
 
 
 
/**
 * @file 3_small.cpp
 * @author liaoqiang
 * @date 2013/04/13 23:15:04
 * @brief 
 *  
**/

#include<stdio.h>
#include<stdlib.h>
#include<string.h>

int judge_palind(int a) {
	int digit[10];
	int digit_size = 0;
	while (a) {
		digit[digit_size ++] = a % 10;
		a = a / 10;
	}

	int is_palind = 1;

	for (int i = 0; i < digit_size / 2; i ++) {
		if (digit[i] != digit[digit_size - 1 - i]) {
			is_palind = 0;
			break;
		}
	}

	return is_palind;
}

int main() {
	int T, case_no = 1;
	scanf("%d", &T);
	int num[1000];
	memset(num, 0, sizeof(num));

	for (int i = 1; i <= 1000; i ++) {
		if ((i * i) > 1000) {
			break;
		}

		if (judge_palind(i * i) && judge_palind(i)) {
			num[i * i - 1] = 1;
		}

	}

	while (case_no <= T) {
		int A, B;
		scanf("%d%d", &A, &B);
		int result = 0;
		for (int i = A; i <= B; i ++) {
			if (num[i - 1] == 1) {
				result ++;
			}
		}

		printf("Case #%d: %d\n", case_no, result);
		case_no ++;
	}

	return 0;
}



















/* vim: set expandtab ts=4 sw=4 sts=4 tw=100: */
