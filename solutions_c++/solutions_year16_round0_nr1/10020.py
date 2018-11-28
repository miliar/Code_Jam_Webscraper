#include <iostream>

bool IsDigitInNumber(unsigned int digit, unsigned int number)
{
	while (number)
	{
		if (number % 10 == digit) return true;
		number /= 10;
	}
	return false;
}

bool AllDigitFound(bool array[], int length = 10)
{
	for (unsigned int i = 0; i < length; ++i)
	{
		if (array[i] == false) return false;
	}
	return true;
}

unsigned int EvaluateNumber(unsigned int number)
{
	bool digitMemory[10] = {};
	unsigned int iteration = 1;
	unsigned int n;
	while (!AllDigitFound(digitMemory))
	{
		n = number * iteration;
		//std::cout << n << std::endl;
		for (unsigned int i = 0; i < 10; ++i)
		{
			if (digitMemory[i] == false) digitMemory[i]=IsDigitInNumber(i, n);
		}
		iteration++;
	}
	return n;
}

int main()
{
	unsigned int T;
	//std::cout << "Enter number of testcases T : ";
	std::cin >> T;

	for (unsigned int i = 0; i < T; ++i)
	{
		unsigned int number;
		//std::cout << "Input : ";
		std::cin >> number;

		if (number == 0)
			std::cout << "Case #" << i + 1 << ": " << "INSOMNIA" << "\n";
		else
			std::cout << "Case #" << i + 1 << ": " << EvaluateNumber(number) << "\n";

	}
}
