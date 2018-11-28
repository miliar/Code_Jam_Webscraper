#include <iostream>
#include <math.h>
#include <string>

bool IsPalindrome(int number)
{
	char szBuffer[1024] = { 0 };
	_itoa_s(number, szBuffer, 10);

	int strLength = strlen(szBuffer);
	for (int i = 0; i < strLength / 2; i++)
	{
		if(szBuffer[i] != szBuffer[strLength - 1 - i])
			return false;
	}

	return true;
}

bool IsFairAndSquare(int number)
{
	if(!IsPalindrome(number))
		return false;

	double numberSqrt = sqrt(number);
	if(numberSqrt != (int)numberSqrt)
		return false;

	if(!IsPalindrome((int)numberSqrt))
		return false;

	return true;
}

int main()
{
	int qtd = 0;
	std::cin >> qtd;

	std::string output;

	for (int i = 0; i < qtd; i++)
	{
		int min = 0;
		int max = 0;

		std::cin >> min;
		std::cin >> max;

		int count = 0;
		for (int j = min; j <= max; j++)
		{
			if(IsFairAndSquare(j))
				count++;
		}

		char szBuffer[1024] = { 0 };
		sprintf_s(szBuffer, "Case #%d: %d", i + 1, count);

		output += szBuffer;
		output += "\n";
	}

	std::cout << output << std::endl;

	return 0;
}