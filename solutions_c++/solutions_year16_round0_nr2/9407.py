
#include <iostream>
#include <vector>
#include <algorithm>

void flip(std::string& stack, int flipPoint)
{
	std::reverse(stack.begin(), stack.begin()+flipPoint);

	for (int i = 0; i < flipPoint; i++) {
		// Flip the bit
		stack[i] = stack[i] == '-' ? '+' : '-';
	}
}

int main()
{

	int T;
	std::cin >> T;

	for (int t = 0; t < T; t++) {
		// Load input
		std::string stack;
		std::cin >> stack;

		int numFlips = 0;

		while (true) {
			int flipPoint = stack.find_first_not_of(stack[0]);
			if (stack == std::string(stack.size(), '-'))
			{
				flipPoint = stack.size();
			}

			if (stack == std::string(stack.size(), '+')) {
			  break;
			}

			flip(stack, flipPoint);
			numFlips++;

		}


		std::cout << "Case #" << t+1 << ": " << numFlips << std::endl;

	}

	return 0;
}
