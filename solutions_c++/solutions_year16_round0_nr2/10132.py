#include <iostream>
#include <string>
#include <cstring>

unsigned int GetSignChangeNumber(char stack[], unsigned int length)
{
	char current = stack[0];
	unsigned int cpt = 0;
	for (unsigned int i = 0; i < length - 1; ++i)
	{
		current = stack[i];
		if (current != stack[i + 1]) cpt++;
	}
	return cpt;
}


int main()
{
	unsigned int T;
	//std::cout << "Enter number of testcases T : ";
	std::cin >> T;

	for (unsigned int i = 0; i < T; ++i)
	{
		std::string sequence;
		//std::cout << "Input : ";
		std::cin >> sequence;

		auto length = sequence.size();
		char stack[100];
		strncpy(stack, sequence.c_str(), sizeof(sequence));
		stack[sizeof(stack) - 1] = 0;

		unsigned int res = GetSignChangeNumber(stack, length);
		if (stack[length - 1] == '-')
			res = res + 1;

		std::cout << "Case #" << i + 1 << ": " << res << "\n";

	}
}
