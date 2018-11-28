#include <iostream>
#include <string>

const int MAX_SHYNESS_IN_PROBLEM = 1000;
int buckets[MAX_SHYNESS_IN_PROBLEM + 1];

int DoTest()
{
	int max_shyness;
	std::cin >> max_shyness;
	std::string input;
	std::cin >> input;

	for (int i = 0; i <= max_shyness; i++)
		buckets[i] = int(input[i] - '0');

	int standing_people = buckets[0];
	int result = 0;
	for (int i = 1; i <= max_shyness; i++)
	{
		if (standing_people < i)
		{
			int diff = i - standing_people;
			result += diff;
			standing_people += diff;
		}
		standing_people += buckets[i];
	}
	return result;
}

int main()
{
	int t;
	std::cin >> t;
	for (int i = 1; i <= t; i++)
	{
		std::cout << "Case #" << i << ": " << DoTest() << '\n';
	}
}