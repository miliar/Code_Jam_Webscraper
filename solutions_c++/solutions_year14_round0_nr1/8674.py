#include <iostream>
#include <fstream>
using namespace std;

#define SIZE 4

void processOneRound(int caseNo)
{
	cout << "Case #" << caseNo << ": ";
	int row1;
	cin >> row1;

	int temp;
	for (int i = 1; i < row1; ++i)	// Discard first (row1 - 1) lines
		for (int n = 0; n < SIZE; ++n)
			cin >> temp;

	int exists1[SIZE];
	for (int n = 0; n < SIZE; ++n)
	{
		cin >> temp;
		exists1[n] = temp;
	}

	for (int i = 0; i < SIZE - row1; ++i)	// Discard last (SIZE - row1) lines
		for (int n = 0; n < SIZE; ++n)
			cin >> temp;

	int row2;
	cin >> row2;

	for (int i = 1; i < row2; ++i)	// Discard first (row1 - 1) lines
		for (int n = 0; n < SIZE; ++n)
			cin >> temp;

	int exists2[SIZE];
	for (int n = 0; n < SIZE; ++n)
	{
		cin >> temp;
		exists2[n] = temp;
	}

	for (int i = 0; i < SIZE - row2; ++i)	// Discard last (SIZE - row1) lines
		for (int n = 0; n < SIZE; ++n)
			cin >> temp;

	int count = 0, number;
	for (int i = 0; i < SIZE; ++i)
		for (int j = 0; j < SIZE; ++j)
			if (exists1[i] == exists2[j])
			{
				++count;
				number = exists1[i];
			}

	if (count == 0)
		cout << "Volunteer cheated!" << endl;
	else if (count == 1)
		cout << number << endl;
	else
		cout << "Bad magician!" << endl;
}

int main()
{
	std::ifstream in("A-small-attempt0.in");
	std::streambuf *cinbuf = std::cin.rdbuf(); //save old buf
	std::cin.rdbuf(in.rdbuf()); //redirect std::cin to in.txt!

	std::ofstream out("out.txt");
	std::streambuf *coutbuf = std::cout.rdbuf(); //save old buf
	std::cout.rdbuf(out.rdbuf()); //redirect std::cout to out.txt!

	int numCases = 0;
	cin >> numCases;
	for (int i = 0; i < numCases; ++i)
		processOneRound(i + 1);

	return 0;
}