#include <iostream>
#include <string>

using namespace std;

//For the downmost pancake that's not happy, we're forced to flip that pancake.
//This means that it will get on the top and the stack. The pancakes infront will reverse its order and flip sign.
//This means that the optimal choice is the optimal number of flips of having the i - 1 stack to - plus 1.

//If we don't meet an unhappy pancake we need to know the optimal value of having the topmost stack to +

inline void PrintResult(int testCase, int number)
{
	printf("Case #%i: %i\n", testCase, number);
}

int main() {
	int testCases, stackSize;
	string inputStack;
	pair<int, int> minimumFlipsHappySad;
	cin >> testCases;
	for (int i = 1; i <= testCases; i++)
	{
		cin >> inputStack;
		stackSize = static_cast<int>(inputStack.size());
		minimumFlipsHappySad.first = 0;
		minimumFlipsHappySad.second = 0;
		for (int j = 0; j < stackSize; j++)
		{
			if (inputStack[j] == '+')
				minimumFlipsHappySad.second = minimumFlipsHappySad.first + 1;
			else
				minimumFlipsHappySad.first = minimumFlipsHappySad.second + 1;
		}
		PrintResult(i, minimumFlipsHappySad.first);
	}
	return 0;
}