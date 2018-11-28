#include <iostream>
#include <fstream>
#include <list>
#include <algorithm>
#include <random>

#define READFROMFILE
#define WRITETOFILE

int splitCostTable[1001][1001];
int min;

inline void insertPlate(std::list<int> &plates, int numberOfPancakes)
{
	for (auto it = plates.begin(); it != plates.end(); it++)
	{
		if (*it < numberOfPancakes)
		{
			plates.insert(it, numberOfPancakes);
			return;
		}
	}
	plates.push_back(numberOfPancakes);
}

void splitAndInsert(std::list<int> &plates, int value, int splitInto)
{
	int res = value / splitInto;
	int remaining = value - res;
	
	insertPlate(plates, res);

	if (splitInto > 1)
	{
		splitAndInsert(plates, remaining, splitInto - 1);
	}
	else
	{
		insertPlate(plates, remaining);
	}
}

void test(int ply, std::list<int> &plates)
{
	if (ply >= min)
		return;
	if (plates.empty())
	{
		min = std::min(ply, min);
		return;
	}

	// Split Up
	if (plates.front() > 3)
	{
		int oldPlate = plates.front();
		for (int i = 2; i < oldPlate; i++)
		{
			std::list<int> newPlates(plates);
			newPlates.pop_front();

			splitAndInsert(newPlates, oldPlate, i);
			test(ply + i - 1, newPlates);
			if (splitCostTable[oldPlate][i] < splitCostTable[oldPlate][i + 1])
				break;
		}
	}

	// Consume
	{
		std::list<int> newPlates(plates);
		for (auto it = newPlates.begin(); it != newPlates.end();)
		{
			int newValue = *it - 1;
			if (newValue > 0)
			{
				*it = newValue;
				it++;
			}
			else
				newPlates.erase(it++);
		}
		test(ply + 1, newPlates);
	}
}

int cost;
int splitTest(int remaining, int splitIn)
{
	int res = remaining / splitIn;
	remaining -= res;
	cost++;

	if (splitIn - 1 > 1 && remaining > 1)
	{
		return std::max(res, splitTest(remaining, splitIn - 1));
	}
	else
		return std::max(res, remaining);
}

int main()
{
	int numOfTestCases;
	/*
	{
		std::ofstream output("ProblemB.in", std::ofstream::out);
		output << 1 << std::endl << 1000 << std::endl;

		std::random_device rd;
		std::mt19937 gen(rd());
		std::uniform_int_distribution<> dis(1, 1000);

		for (int i = 0; i < 1000; i++)
			output << dis(gen) << " ";
	}*/

#ifdef READFROMFILE
	std::ifstream input("ProblemB.in", std::ifstream::in);
#else
	std::istream &input = std::cin;
#endif

#ifdef WRITETOFILE
	std::ofstream output("ProblemB.out", std::ofstream::out);
#else
	std::ostream &output = std::cout;
#endif


	for (int i = 2; i <= 1000; i++)
	{
		cost = 0;

		for (int splitIn = 2; splitIn <= i; splitIn++)
		{
			//std::cout << " (";
			splitCostTable[i][splitIn] = splitTest(i, splitIn) + cost;
			//std::cout << ")";
		}
	}

	input >> numOfTestCases;

	std::list<int> plates;

	for (int testCase = 1; testCase <= numOfTestCases; testCase++)
	{
		int numberOfPlates;
		input >> numberOfPlates;

		plates.clear();

		for (int i = 0; i < numberOfPlates; i++)
		{
			int numberOfPancakes;
			input >> numberOfPancakes;

			insertPlate(plates, numberOfPancakes);
		}
		min = plates.front();
		test(0, plates);

		output << "Case #" << testCase << ": " << min << std::endl;
	}
}