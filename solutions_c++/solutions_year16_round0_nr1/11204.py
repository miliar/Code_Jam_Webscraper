#include <iostream>
#include <stdio.h>
#include <vector>
#include <string>
#include <stdlib.h>
#include <algorithm>


using namespace std;

int main(int argc, char const *argv[])
{
	int T, N,flag = 0;
	std::cin >> T;
	std::vector<int> numbers;
	std::vector<std::string> outputs;
	int j = 1;
	while (T > 0)
	{
		std::cin >> N;
		int i = 0;
		int trial = N;
		while (1)
		{
			if (trial == 0)
			{
				//flag = 1;
				break;
			}
			int num = trial;
			int ret = trial;
			while (ret > 0)
			{
				num = ret;
				ret = ret / 10;
				num = num % 10;
				if (std::find(numbers.begin(), numbers.end(), num) != numbers.end()) {
				}
				else {
					numbers.push_back(num);
					if (numbers.size() == 10)
					{
						flag = 1;
						break;
					}
				}
				
			}
			
			if (flag == 1)
			{
				flag = 0;
				break;
			}
			i++;
			trial = (i+1) * N;
			flag = 0;
		}
		numbers.clear();
		outputs.push_back(std::to_string(trial));
		T--;
	}
	for (int j = 0; j < outputs.size(); j++)
	{
		if (outputs.at(j) == "0")
		{
			std::cout << "Case #" << j + 1 << ": INSOMNIA" << std::endl;
		}
		else
		{
			std::cout << "Case #" << j + 1 << ": " << outputs.at(j) << std::endl;
		}
	}
}
