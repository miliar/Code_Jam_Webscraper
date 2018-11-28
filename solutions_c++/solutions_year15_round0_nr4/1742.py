#include <stdio.h>
#include <fstream>
#include <string>

using namespace std;


// Number of problems
int numProblems;

// file readers
ifstream fin;
ofstream fout;

#define RICHARD 1
#define GABRIEL 2

int X;
int W;
int H;

int winner;

void Initialize();
void ReadProblem();
void SolveProblem();
void OutputProblem(int n);

int main()
{
	Initialize();

	for (int i = 1; i <= numProblems; i++)
	{
		ReadProblem();
		SolveProblem();
		OutputProblem(i);
	}
}

void Initialize()
{
	numProblems = 0;

	fin = ifstream("input.txt");
	fout = ofstream("output.txt");

	fin >> numProblems;
}

void ReadProblem(void)
{
	fin >> X;
	fin >> W;
	fin >> H;
}

void SolveProblem(void)
{
	int min;
	int max;

	if (W > H)
	{
		max = W;
		min = H;
	}
	else
	{
		max = H;
		min = W;
	}

	int area = H * W;

	// Cannot file board fully
	if (area % X != 0)
	{
		winner = RICHARD;
		return;
	}

	// Can choose a piece with a hole
	if (X >= 8)
	{
		winner = RICHARD;
		return;
	}

	// Can't fit
	if (area < X)
	{
		winner = RICHARD;
		return;
	}

	// Can choose a piece that doesn't fit
	if (X > max)
	{
		winner = RICHARD;
		return;
	}

	if (X >= min * min && min != 1)
	{
		winner = RICHARD;
		return;
	}

	// A corner piece won't fit
	if (min == 1 && X > 2)
	{
		winner = RICHARD;
		return;
	}

	winner = GABRIEL;
	return;
}

void OutputProblem(int n)
{
	fout << "Case #" << n << ": ";

	if (winner == RICHARD)
	{
		fout << "RICHARD";
	}
	else
	{
		fout << "GABRIEL";
	}

	fout << endl;
}