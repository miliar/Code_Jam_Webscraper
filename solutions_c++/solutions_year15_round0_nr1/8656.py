#include <iostream>
#include <stdint.h>
#include <string>

int32_t solve(int32_t arg)
{
	int32_t counter, friends, n;
	std::string input;

	std::cin >> n >> input;
	friends = counter = 0;

	for(int32_t i = 0; i < input.size(); ++i)
	{
		if(counter < i)
		{
			friends += i - counter;
			counter = i;
		}

		counter += input[i] - 48;
	}

	std::cout << "Case #" << arg << ": " << friends << std::endl;
}

int main(int argc, char** argv)
{
	int32_t z;
	std::cin >> z;
	
	for(int32_t i = 0; i < z; ++i)
		solve(i+1);
	return 0;
}