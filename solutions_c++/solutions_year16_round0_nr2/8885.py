
#include <iostream>
#include <string>
#include <unistd.h>
using namespace std;

class PancakeStack {
public:
	PancakeStack(string stackStr)
	{
		size = stackStr.length();
		for (int i = 0; i < size; i++) data[i] = stackStr.at(i);
		data[size] = 0x00;
	}

	bool isAllHappy()
	{
		for (int i = 0; i < size; i++) {
			if (data[i] != '+') return false;
		}
		return true;
	}

	int getLowestUnhappy()
	{
		for (int i = size - 1; i >= 0; i--) {
			if (data[i] == '-') return i;
		}
		return -1;
	}

	int getLeadingHappy()
	{
		for (int i = 0; i < size; i++) {
			if (data[i] == '-') return (i - 1);
		}
		return size - 1;
	}

	char flipSinglePancake(char pancake)
	{
		if (pancake == '+') return '-';
		else return '+';
	}

	void flip(int numPancakes)
	{
		// Copy
		char dataCopy[100];
		for (int i = 0; i < 100; i++) dataCopy[i] = data[i];

		// Flip
		for (int i = 0; i <= numPancakes; i++) {
			data[i] = flipSinglePancake(dataCopy[numPancakes - i]);
		}
	}

	int getFlipCount()
	{
		int current = 0;

		while (isAllHappy() == false) {
			if (data[0] == '+') flip(getLeadingHappy());
			else flip(getLowestUnhappy());
			current++;
		}

		return current;
	}

	int size;
	char data[101];
};

int main()
{
	// Read number of testcases
	int numTestcases, number;
	cin >> numTestcases;

	for (int i = 1; i <= numTestcases; i++) {
		// Read pancake stack
		string stackStr;
		cin >> stackStr;
		PancakeStack *stack = new PancakeStack(stackStr);

		cout << "Case #" << i << ": " << stack->getFlipCount() << endl;
	}

}