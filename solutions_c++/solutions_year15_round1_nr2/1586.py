#include <stdio.h>
#include <stdlib.h>
#include <fstream>
#include <iostream>

using namespace std;

int numProblems = 0;
ifstream fin;
ofstream fout;

long M[1001];
long remainders[1001];
int barbers[1001];
int myBarber = 0;

int numBarbers;
int N;
int mostMinutes;
int SpeedCustomersServed;

unsigned int hughCycleMinutes;
unsigned int hughCycleNum;

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
	myBarber = 0;
	numBarbers = 0;
	mostMinutes = 0;
	SpeedCustomersServed = 0;
	N = 0;
	hughCycleMinutes = 1;
	hughCycleNum = 0;

	fin >> numBarbers;
	fin >> N;

	for (int i = 1; i <= numBarbers; i++)
	{
		barbers[i] = 0;
	}
	for (int i = 1; i <= numBarbers; i++)
	{
		fin >> M[i];
		if (M[i] > mostMinutes)
		{
			mostMinutes = M[i];
		}

		
		hughCycleMinutes *= M[i];
	}

	for (int i = 1; i <= numBarbers; i++)
	{
		remainders[i] = mostMinutes % M[i];
		SpeedCustomersServed += (int)(((float)mostMinutes + 0.5) / M[i]) + 1;
	}

	for (int i = 1; i <= numBarbers; i++)
	{
		hughCycleNum += hughCycleMinutes / M[i];
	}
}

void SolveProblem()
{
	bool newCustomer = false;
	bool bestDecrement = 0;

	while (N > hughCycleNum)
	{
		N -= hughCycleNum;
	}

	int min = 0;
	while (true)
	{
		bestDecrement = 999999;
		min += 1;
			//cout << "min " << min << endl;
		for (int i = 1; i <= numBarbers; i++)
		{
			barbers[i]--;

			if (barbers[i] <= 0)
			{
				//cout << " serve at " << i << endl;
				barbers[i] = M[i];
				N--;
			}

			if (N == 0)
			{
				myBarber = i;
				return;
			}

			int remainder = barbers[i];
			if (remainder < bestDecrement)
			{
				bestDecrement = remainder;
			}

			
		}

		/*
		for (int i = 1; i <= numBarbers; i++)
		{
			barbers[i] -= (bestDecrement - 1);
		}
		*/
	}
}

void OutputProblem(int n)
{
	fout << "Case #" << n << ": " << myBarber << endl;
	//cout << "Case #" << n << ": " << myBarber << endl;
}