#include <stdio.h>
#include <stdlib.h>
#include <fstream>
#include <iostream>

using namespace std;

int numProblems = 0;
ifstream fin;
ofstream fout;

int N;
int mushrooms[1000];

int minY;
int minZ;

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
	fin = ifstream("input.txt");
	fout = ofstream("output.txt");

	fin >> numProblems;
}

void ReadProblem()
{
	N = 0;
	fin >> N;

	minY = 0;
	minZ = 0;

	for (int i = 0; i < N; i++)
	{
		fin >> mushrooms[i];
	}
}

void SolveProblem()
{
	int change = 0;
	int maxChange = 0;

	for (int i = 0; i < N - 1; i++)
	{
		change = mushrooms[i] - mushrooms[i + 1];

		if (change > 0)
		{
			minY += change;

			if (change > maxChange)
			{
				maxChange = change;
			}
		}
	}

	for (int i = 0; i < N - 1; i++)
	{
		change = mushrooms[i] - mushrooms[i + 1];

		if ((mushrooms[i]) < maxChange)
		{
			minZ += mushrooms[i];
		}
		else
		{
			minZ += maxChange;
		}
	}
}

void OutputProblem(int n)
{
	fout << "Case #" << n << ": " << minY << " " << minZ << endl;
}