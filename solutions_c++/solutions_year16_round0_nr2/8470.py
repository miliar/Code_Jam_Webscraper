#include <stdint.h>
#include <iostream>
#include <fstream>
#include <vector>
#include <set>
#include <map>
#include <algorithm>
#include <string.h>
#include <stdlib.h>
#include <stdio.h>

uint64_t T, N;

int main() {
	std::ifstream in("input.in");
	std::ofstream out("output.out");

	in >> T;

	for (auto test = 0; test < T; test++) {
		//in >> N;

		out << "Case #" << test + 1 << ": ";

		std::vector<bool> stack_a;
		std::vector<bool> stack_b;

		std::string pancake_stack("");
		in >> pancake_stack;
		printf("%s\n", pancake_stack.c_str());
		
		char prev = '\0';
		int steps = 0;
		for (auto &c : pancake_stack) {
			if (c == '+' && prev == '+') {
				steps += 0;
			}
			if (c == '+' && prev == '-') {
				steps += 0;
			}
			if (c == '-' && prev == '+') {
				steps += 2;
			}
			if (c == '-' && prev == '-') {
				steps += 0;
			}
			if (c == '-' && prev == '\0') {
				steps += 1;
			}
			prev = c;

		}

		out << steps << std::endl;
	}
}
