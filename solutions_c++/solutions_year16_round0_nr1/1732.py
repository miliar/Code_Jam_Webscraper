#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

void findNums(unsigned int n, bool* nums) {
	for(;n > 0; n /= 10)
		nums[n % 10] = true;
}

bool checkNums(bool* nums) {
	for (int i = 0; i < 10; i++) 
		if (nums[i] == false) return false;
	return true;
}

int main(void) {
	int T;
	std::cin >> T;
	for (int t = 1; t <= T; t++) {
		std::cout << "Case #" << t << ": ";
		unsigned int N;
		std::cin >> N;
		bool nums[10] = {false};
		findNums(N,nums);
		unsigned int cN = N;
		if (N != 0) {
			for(; !checkNums(nums); cN += N)
				findNums(cN,nums);
			std::cout << cN - N;
		} else std::cout << "INSOMNIA";
		std::cout << std::endl;
	}
	return 0;
}
