#include <iostream>
#include <string>

bool isConsonant(char c)
{
	if (c == 'a')
	{
		return false;
	}

	if (c == 'e')
	{
		return false;
	}

	if (c == 'i')
	{
		return false;
	}

	if (c == 'o')
	{
		return false;
	}

	if (c == 'u')
	{
		return false;
	}

	return true;
}

int main(int argc, char *argv[])
{
	unsigned nrTCs;

	std::cin >> nrTCs;
	for(unsigned i = 0; i < nrTCs; i++)
	{
		std::string inpString;
		unsigned long length;
		std::cin >> inpString;
		std::cin >> length;

		unsigned long consonantsFound = 0;
		unsigned long runningSum = 0;
		unsigned long increment = 0;
		for(long j = inpString.length() - 1; j >= 0; j--)
		{
			if (isConsonant(inpString[j]))
			{
				consonantsFound++;
			} else
			{
				consonantsFound = 0;
			}

			if (consonantsFound >= length)
			{
				unsigned long newItems = (inpString.length() - j + 1 - length);
				increment = newItems;
				runningSum += increment;
			} else
			{
				runningSum += increment;
			}
		}

		std::cout << "Case #" << (i + 1) << ": " << runningSum << "\n";
	}

	return 0;
}