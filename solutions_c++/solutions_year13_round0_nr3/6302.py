#include <fstream>
#include <string>
#include <iostream>
#include <math.h>

int IsPalindrome(int x)
{
	char buf[100];
	std::string _x = itoa(x, buf, 10);
	int length = _x.size();
	for (int i = 0; i < length / 2; ++i)
	{
		if (_x[i] != _x[length - i - 1])
		{
			return 0;
		}
	}
	return 1;
}

int Solve (int low, int high)
{
	int l = ceil(sqrt(float(low)));
	int h = floor(sqrt(float(high)));

	int result = 0;
	for (int i = l; i <= h; ++i)
	{
		result += IsPalindrome(i) * IsPalindrome(i*i);
	}

	return result;
}

void main ()
{	
	std::ifstream input ("Input.txt");
	std::string line("");
	getline (input, line);
	int tests_num = atoi(line.c_str());
	
	int low, high;

	std::ofstream output ("Output.txt");

	for (int i = 0; i < tests_num; ++i)
	{
		getline (input, line);
		low = atoi(line.substr(0, line.find_first_of(' ')).c_str());
		high = atoi(line.substr(line.find_first_of(' ') + 1).c_str());

		output << "Case #" << i + 1 << ": " << Solve(low, high) << std::endl;
	}
	
	output.close();
	input.close();
}