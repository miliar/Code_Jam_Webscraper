#include <iostream>
#include <vector>
#include <assert.h>
#include <unordered_set>

using namespace std;

//The challenge of this problem is realizing that we only have insomnia in the case N = 0
//Otherwise we can bound the input to an upper limit to the nearest multiple of 10.
//For the big problem, we are sure that we can bound the upper limit by 10^6, meaning that some multiple will pass (1)*10^6
//and at some point (2)*10^6. Since the number is 0 < x <= 10^6, we are sure that the next time we'll pass we can simply increase the counter
//to (3)*10^6. We are therefore sure that we WILL pass all the digits from 0 to 9.
//What happens for 0? All multiples are trivially 0 and we'll have insomnia.

vector<int> GetAllDigits(int number)
{
	assert(number >= 0);
	vector<int> result;
	while (number > 0)
	{
		result.push_back(number % 10);
		number /= 10;
	}
	return result;
}

inline void PrintResult(int testCase, int number)
{
	if (number >= 1)
		printf("Case #%i: %i\n", testCase, number);
	else
		printf("Case #%i: %s\n", testCase, "INSOMNIA");
}

int main() {
	int testCases, number, multipleCounter, currentMultiple;
	cin >> testCases;
	for (int i = 1; i <= testCases; i++)
	{
		unordered_set<int> foundDigits(10);
		cin >> number;
		if (number < 1)
		{
			PrintResult(i, number);
			continue;
		}
		multipleCounter = 1;
		while (foundDigits.size() != 10)
		{
			currentMultiple = multipleCounter * number;
			auto digits = GetAllDigits(currentMultiple);
			for (auto digit : digits)
			{
				foundDigits.insert(digit);
				if (foundDigits.size() == 10)
					break;
			}
			multipleCounter++;
		}
		PrintResult(i, currentMultiple);
	}

	return 0;
}
