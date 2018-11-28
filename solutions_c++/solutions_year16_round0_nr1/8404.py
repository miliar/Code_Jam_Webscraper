
#include <fstream>

namespace 
{
	const size_t COUNT_DIGITS = 10;
}

void expandNumber(size_t number, bool* const digits)
{
	while (number)
	{
		digits[number % 10] = true;
		number /= 10;
	}
}

size_t increaseNumber(const size_t sum, const size_t number)
{
	size_t res = sum + number;
	if (sum >= res)
	{
		res = 0;
	}
	return res;
}

bool checkDigits(const bool* const digits)
{
	bool res = true;
	for (size_t i = 0; i < COUNT_DIGITS; i++)
	{
		res &= digits[i];
	}
	return res;
}

size_t getLastNumber(const size_t number)
{
	size_t result = number;
	bool digits[COUNT_DIGITS] = {false, false, false, false, false, false, false, false, false, false};
	bool exit = false;

	expandNumber(result, digits);
	exit = checkDigits(digits);

	while (!exit && result)
	{
		result = increaseNumber(result, number);
		expandNumber(result, digits);
		exit = checkDigits(digits);
	} 
	return result;
}

void main()
{
	std::ifstream in("D:\\GoogleCodeJam2016\\input.txt");
	std::ofstream out("D:\\GoogleCodeJam2016\\output.txt");

	size_t count = 0;
	in >> count;
	if (0 > count)
	{
		count = 0;
	}

	size_t number;
	for (size_t i = 0; i < count && !in.eof(); ++i)
	{
		in >> number;

		const size_t res = getLastNumber(number);
		
		out << "Case #" << i + 1 << ": ";
		if (res)
		{
			out << res;
		}
		else
		{
			out << "INSOMNIA";
		}
		out << std::endl;
	}

	in.close();
	out.close();
}