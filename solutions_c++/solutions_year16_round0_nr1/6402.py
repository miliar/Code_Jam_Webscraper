#include <iostream>
#include <vector>
#include <string>
#include <fstream>
#include <algorithm>

using namespace std;

bool test(unsigned int num, unsigned long long& multiple) 
{
	int count = 10;
	vector<int> visited(10, false);
	for (int i = 1; i < 100; i++)
	{
		unsigned long long multiples = num * i;
		unsigned long long temp = multiples;
		while (temp)
		{
			int digit = temp % 10;
			if (!visited[digit])
			{
				visited[digit] = true;
				count--;
			}
			if (count == 0)
			{
				multiple = multiples;
				return true;
			}
			temp /= 10;
		}
	}
	return false;
}

int main()
{
    std::ifstream file("A-large.in");
    std::string str;
	std::getline(file, str);
	vector<unsigned int> nums(stoi(str)); // number of lines;
	int i = 0;
    while (std::getline(file, str))
    {
		nums[i++] = stoi(str);
    }
	i = 1;
	std::for_each(nums.begin(), nums.end(), [&](unsigned int num)
	{
		unsigned long long multiple;
		if (!test(num, multiple))
		{
			cout << "Case #" << i << ": INSOMNIA" << endl;
		}
		else
		{
			cout << "Case #" << i << ": " << multiple << endl;
		}
		i++;
	});
	return 0;
}