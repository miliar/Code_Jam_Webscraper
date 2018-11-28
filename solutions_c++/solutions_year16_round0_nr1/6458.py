#include <cstdio>
#include <set>
#include <algorithm>
#include <cassert>
#include <iostream>
#include <string>

#pragma warning( disable : 4996 ) 

void apply_num_to_digit_set(int num, std::set<int> *digit_set)
{
	for (int val = num ; val > 0; val = val / 10) {
		int x = val % 10;
		auto it = digit_set->find(x);
		if (it == digit_set->end()) {
			digit_set->insert(x);
		}
	}
}

bool is_complete(const std::set<int> &digit_set)
{
	return (digit_set.size() == 10);
}

int count_sheep(int val)
{
	if (val == 0) {
		return -1;
	}

	std::set<int> exist_digit_set;

	for (int i = 1; i < 100; i++) {
		int n = val * i;
		apply_num_to_digit_set(n, &exist_digit_set);

		if (is_complete(exist_digit_set)) {
			return n;
		}
	}
	return 0;
}

void solve_problem(int idx, int num) 
{
	int retval = count_sheep(num);
	if (retval == -1) {
		printf("Case #%d: INSOMNIA\n", idx);
	}
	else {
		printf("Case #%d: %d\n", idx, retval);
	}
}

void assert_based_test()
{
	assert(count_sheep(0) == -1);
	assert(count_sheep(1) == 10);
	assert(count_sheep(2) == 90);
	assert(count_sheep(11) == 110);
	assert(count_sheep(1692) == 5076);
}

void solve_stdin()
{
	int problem_size = 0;
	scanf("%d", &problem_size);

	for (int i = 1; i <= problem_size; i++) {
		int num = 0;
		scanf("%d", &num);
		solve_problem(i, num);
	}
}

void solve_random_problem(int problem_size)
{
	for (int i = 1; i <= problem_size; i++) {
		int num = rand() % 100;
		solve_problem(i, num);
	}
}

int main()
{
	//assert_based_test();
	solve_stdin();
	//solve_random_problem(1000000);
	return 0;
}
