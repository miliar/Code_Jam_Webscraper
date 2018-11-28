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

std::map<int64_t, int64_t> values;

int main() {
	std::ifstream in("input.in");
	std::ofstream out("output.out");

	in >> T;

	for (auto test = 0; test < T; test++) {
		in >> N;

		out << "Case #" << test + 1 << ": ";

		values.clear();
		int64_t number = 0;
		char buffer[1024];
		for(int64_t i = 1; i <= 101; i++) {
			int64_t temp = N * i;

			if (number == temp) {
				number = -1;
				break; 
			}

			number = temp;

			sprintf(buffer, "%ld", number);
			for (int64_t at_char = 0; at_char < strlen(buffer); at_char++) {
				values[buffer[at_char]]++;
			}

			if (values.size() >= 10) {
				break;
			}
		}

		if (number == -1) {
			out << "INSOMNIA" << std::endl;
		} else {
			out << number << std::endl;
		}
	}
}
