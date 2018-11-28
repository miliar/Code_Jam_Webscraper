#include <fstream>
#include <iostream>
#include <string>
#include <vector>

using namespace std;

int main()
{
	ifstream inFile("input.txt");
	ofstream outFile("output.txt");
	int numCases, numNums;
	string numbers, phoneNum;

	if (!inFile)
	{
		cout << "File not working" << endl;
		return 0;
	}

	inFile >> numCases;

	for (int i = 0; i < numCases; i++)
	{
		inFile >> numbers;
		numNums = 0;
		phoneNum = "";

		outFile << "Case #" << i + 1 << ": ";

		int zero = count(numbers.begin(), numbers.end(), 'Z'),
			six = count(numbers.begin(), numbers.end(), 'X'),
			two = count(numbers.begin(), numbers.end(), 'W'),
			four = count(numbers.begin(), numbers.end(), 'U'),
			eight = count(numbers.begin(), numbers.end(), 'G'),
			one = count(numbers.begin(), numbers.end(), 'O') - zero - two - four,
			seven = count(numbers.begin(), numbers.end(), 'S') - six,
			three = count(numbers.begin(), numbers.end(), 'H') - eight,
			five = count(numbers.begin(), numbers.end(), 'F') - four,
			nine = count(numbers.begin(), numbers.end(), 'I') - six - eight - five;

		numNums = zero + one + two + three + four + five + six + seven + eight + nine;

		for (int i = 0; i < zero; i++)
		{
			phoneNum += '0';
		}

		for (int i = 0; i < one; i++)
		{
			phoneNum += '1';
		}

		for (int i = 0; i < two; i++)
		{
			phoneNum += '2';
		}

		for (int i = 0; i < three; i++)
		{
			phoneNum += '3';
		}

		for (int i = 0; i < four; i++)
		{
			phoneNum += '4';
		}

		for (int i = 0; i < five; i++)
		{
			phoneNum += '5';
		}

		for (int i = 0; i < six; i++)
		{
			phoneNum += '6';
		}

		for (int i = 0; i < seven; i++)
		{
			phoneNum += '7';
		}

		for (int i = 0; i < eight; i++)
		{
			phoneNum += '8';
		}

		for (int i = 0; i < nine; i++)
		{
			phoneNum += '9';
		}

		outFile << phoneNum << endl;
	}

	inFile.close();
	outFile.close();
	return 0;
}