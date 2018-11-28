// lawnmower.cpp : 定义控制台应用程序的入口点。
//

#include "stdafx.h"
#include <assert.h>
#include <math.h>
#include <string.h>

#include <algorithm>

typedef unsigned long long uint64_t;

#define INPUT_FILE_NAME "C.in"
#define OUTPUT_FILE_NAME "C.out"
#define NUM_MAX_LEN 12u

struct LargeNum {
	char *num;
	int len;
};

char buf[NUM_MAX_LEN];
bool is_fair(uint64_t num) {
	int len = 0;
	while (num > 0) {
		buf[len++] = num%10;
		num /= 10;
	}
	int l = 0, r = len-1;
	for (; l < r; ++l, --r) {
		if (buf[l] != buf[r])
			break;
	}
	if (l < r)
		return false;
	else
		return true;
}


uint64_t find_sqrt_of(LargeNum &lm) {
	return 0;
}
LargeNum square(LargeNum &lm) {
	return lm;
}
bool is_square_less(uint64_t, LargeNum& lm) {
	return false;
}
bool is_square_fair(uint64_t num) {
	return false;
}
LargeNum find_sqrt(LargeNum &lm) {
	return lm;
}

int _tmain(int argc, _TCHAR* argv[])
{
	FILE *fp_in = fopen(INPUT_FILE_NAME, "r");
	assert(fp_in);
	FILE *fp_out = fopen(OUTPUT_FILE_NAME, "w");
	assert(fp_out);

	int case_num = 0;
	fscanf(fp_in, "%d\n", &case_num);
	for (int case_idx = 1; case_idx <= case_num; ++case_idx) {
		uint64_t low = 0, high = 0;	
		fscanf(fp_in, "%lu %lu", &low, &high);
		printf("%lu, %lu\n", low, high);
		int cnt = 0;
		for (uint64_t i = sqrt(long double(low)); i*i <= high ; ++i) {
			if (i*i < low)
				continue;
			if (!is_fair(i))
				continue;
			if (!is_fair(i*i))
				continue;
			++cnt;
		}
		fprintf(fp_out, "Case #%d: %d\n", case_idx, cnt);
	}
	fclose(fp_in);
	fclose(fp_out);
	return 0;
}

