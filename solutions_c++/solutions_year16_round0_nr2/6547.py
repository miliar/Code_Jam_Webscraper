#include <cstdio>
#include <set>
#include <algorithm>
#include <cassert>
#include <iostream>
#include <string>

#pragma warning( disable : 4996 ) 

bool is_complete(const std::string &line)
{
	int last_minus_pos = line.find_last_of('-');
	if (last_minus_pos == std::string::npos) {
		return true;
	}
	return false;
}

void swap_range(std::string *line, int size) {
	for (int i = 0; i <= size/2; i++) {
		char tmp_a = (*line)[i];
		char tmp_b = (*line)[size - i];

		tmp_a = (tmp_a == '-') ? '+' : '-';
		tmp_b = (tmp_b == '-') ? '+' : '-';

		(*line)[i] = tmp_b;
		(*line)[size - i] = tmp_a;
	}
}

int calc_fancake(std::string line)
{
	if (is_complete(line)) {
		return 0;
	}

	int step = 0;

	for (size_t i = 0; i < line.length(); i++) {
		// rule 1. 뒤에서 -가 등장하는 지점이 있고 맨앞이 -이면 해당 범위 뒤집기
		int last_minus_pos = line.find_last_of('-');
		if (line[0] == '-') {
			swap_range(&line, last_minus_pos);
			step++;
		}

		if (is_complete(line)) {
			return step;
		}

		int continus_length = 0;
		for (int i = 0; i < line.length(); i++) {
			if (line[0] == line[i]) {
				continus_length++;
			}
			else {
				break;
			}
		}

		swap_range(&line, continus_length-1);
		step++;

		if (is_complete(line)) {
			return step;
		}
	}
	return 0;
}

int main()
{
	/*
	assert(calc_fancake("-") == 1);
	assert(calc_fancake("-+") == 1);
	assert(calc_fancake("+-") == 2);
	assert(calc_fancake("+++") == 0);
	assert(calc_fancake("--+-") == 3);
	*/

	int problem_size = 0;
	scanf("%d", &problem_size);
	for (int i = 1; i <= problem_size; i++) {
		char buf[256];
		scanf("%s", buf);

		std::string line(buf);
		int val = calc_fancake(line);
		printf("Case #%d: %d\n", i, val);
	}
	return 0;
}

