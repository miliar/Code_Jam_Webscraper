#include <stdio.h>
#include <fstream>
#include <string>

using namespace std;

#define MAX_SIZE 1000

// Array to hold input
short audience[MAX_SIZE];

short shyestIndex;

// Number of problems
int numProblems;

// Number of friends invited
int numFriends;

// file readers
ifstream fin;
ofstream fout;

void Initialize();
void ReadProblem();
void SolveProblem();
void OutputProblem(int n);

int main()
{
	Initialize();

	fin = ifstream("input.txt");
	fout = ofstream("output.txt");

	fin >> numProblems;

	for(int i = 1; i <= numProblems; i++)
	{
		ReadProblem();
		SolveProblem();
		OutputProblem(i);
	}
}

void Initialize()
{
	for(int i = 0; i < MAX_SIZE; i++)
		audience[i] = 0;

	numProblems = 0;
}

void ReadProblem(void)
{
	numFriends = 0;

	int highIndex = 0;
	fin >> highIndex;

	shyestIndex = highIndex;

	string input;
	fin >> input;

	for(int i = 0; i <= highIndex; i++)
	{
		char c = input[i];

		audience[i] = (int)(c - '0');
	}
}

void SolveProblem(void)
{
	int numClapping = 0;
	int numNeeded = 0;

	numFriends = 0;

	for(int i = 0; i <= shyestIndex; i++)
	{
		numNeeded = i;

		if (numClapping >= numNeeded)
		{
			numClapping += audience[i];
		}
		else
		{
			numFriends += (numNeeded - numClapping);

			// add in friends
			numClapping += (numNeeded - numClapping);

			numClapping += audience[i];
		}
	}
}

void OutputProblem(int n)
{
	fout << "Case #" << n << ": " << numFriends << endl;
}