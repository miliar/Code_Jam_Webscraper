// Problem2.cpp : Defines the entry point for the console application.
//


#include <iostream>

using namespace std;



int iterationsRequired(char orientationString[], int pancakeCount, char requiredOrientation)
{
	if (pancakeCount == 1)
		return (requiredOrientation == '+' ^ orientationString[0] == '+');
	else if (orientationString[pancakeCount - 1] ^ requiredOrientation)
		return iterationsRequired(orientationString, pancakeCount - 1, orientationString[pancakeCount - 1]) + 1;
	else
		return iterationsRequired(orientationString, pancakeCount - 1, requiredOrientation);
}

int main()
{

	int tCount;
	cin >> tCount;  // read t. cin knows that t is an int, so it reads it as such.
	char orientationString[150];
	bool pancakeCount;

	for (int t = 1; t <= tCount; ++t)
	{
		cin >> orientationString;

		int pancakeCount = 0;
		while (orientationString[pancakeCount] != '\0') pancakeCount++;

		int required = iterationsRequired(orientationString, pancakeCount, '+');

		cout << "Case #" << t << ": " << required << endl;

	}
}


