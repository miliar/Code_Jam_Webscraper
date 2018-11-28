#include <iostream>

int count_plusses(const std::string& stack)
{
	int plusses = 0;
	for (int i = 0 ; i < stack.size() ; ++i)
	{
		plusses += stack[i] == '+' ? 1 : 0;
	}
	return plusses;
}

int count_stripe(const std::string& stack)
{
	char first_char = stack[0];
	int stripe = 1;
	for (int i = 1 ; i < stack.size() ; ++i)
	{
		if (stack[i] == first_char)
		{
			++stripe;
		}
		else
		{
		    return stripe;
		}
	}
	return stripe;
}

std::string flip_N(const std::string& stack, int N)
{
	std::string new_stack = stack;
	for (int i = 0 ; i < N ; ++i)
	{
		new_stack[i] = new_stack[i] == '-' ? '+' : '-';
	}
	return new_stack;
}

int main() {
	int test_cases = 0;
	std::cin >> test_cases;
	for (int test_case = 1 ; test_case <= test_cases ; ++test_case)
	{
		std::string stack;
		std::cin >> stack;
		int tries = 0;
		while (count_plusses(stack) != stack.size())
		{
			int next_flip_index = count_stripe(stack);
			stack = flip_N(stack, next_flip_index);
			++tries;
		}
		std::cout << "Case #" << test_case << ": " << tries << std::endl;
	}

	return 0;
}
