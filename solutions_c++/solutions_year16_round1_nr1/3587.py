#include <iostream>

int main()
{
	int t;
	std::cin >> t;
	for(int z = 0;z < t;++ z)
	{
		std::string input;
		std::cin >> input;

		std::string output;
		output += input[0];
		for(int i = 1;i < input.size();++ i)
		{
			if(input[i] < output[0])
				output.push_back(input[i]);
			else
				output.insert(output.begin(), input[i]);
			//std::cout << "After " << i << ' ' << output << std::endl;
		}
		std::cout << "Case #" << z+1 << ": " << output << std::endl;
	}

	std::cout << std::endl;
	return 0;
}
