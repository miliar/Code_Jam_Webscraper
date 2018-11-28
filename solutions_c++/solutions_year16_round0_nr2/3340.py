#include <iostream>
#include <fstream>
#include <string>
#include <bitset>

#define SIZE 101


int main() {
	std::ifstream fin;
	fin.open("input.txt");
	std::ofstream fout;
	fout.open("output.txt");

	int T;
	fin >> T;
	for (int i = 1; i <= T; ++i) {
		std::string in_stack;
		fin >> in_stack;
		int size = in_stack.size();
		std::bitset<SIZE> stack;
		int last_plus = size;
		
		for (int i = 0; i < size; ++i) {
			stack[i] = (in_stack[i] == '+') ? 1 : 0;
		}

		int number_of_flips = 0;
		bool done = false;
		while (!done) {
			while (last_plus > 0 && stack[last_plus - 1] == 1) {
				last_plus--;
			}
			if (last_plus == 0) {
				done = true;
				break;
			}
			if (stack[0] == 1) {
				// flip until the last_plus
				int front = 0;
				int back = last_plus - 1;
				while (front < back) {
					bool tmp = stack[front];
					stack[front] = stack[back];
					stack[back] = tmp;
					front++;
					back--;
				}
				number_of_flips++;
			}
			else {
				// flip top minuses
				int i = 0;
				while (i < last_plus && stack[i] == 0) {
					stack[i] = 1;
					i++;
				}
				number_of_flips++;
			}
		}
		std::cout << number_of_flips << std::endl;
		//std::cout << std::hex << stack.to_ullong() << std::dec << std::endl;
		std::cout << in_stack << std::endl;
		fout << "Case #" << i << ": " << number_of_flips << std::endl;
	}

	fin.close();
	fout.close();
	return 0;
}