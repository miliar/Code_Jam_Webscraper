#include <iostream>
#include <fstream>
#include <string>
#include <iomanip>
using namespace std;

double checkMyLowest(double* myBlocks, int totalBlocks)
{
	double val = 1.1;
	for(int i = 0; i < totalBlocks; i++)
	{
		if(myBlocks[i] < val)
			val = myBlocks[i];
	}
	return val;
}

double checkMyHighest(double* myBlocks, int totalBlocks)
{
	double val = -0.1;
	for(int i = 0; i < totalBlocks; i++)
	{
		if(myBlocks[i] > val)
			val = myBlocks[i];
	}
	return val;
}

double checkTheirLowest(double* theirBlocks, int totalBlocks)
{
	double val = 1.1;
	for(int i = 0; i < totalBlocks; i++)
	{
		if(theirBlocks[i] < val)
			val = theirBlocks[i];
	}
	return val;
}

double checkTheirHighest(double* theirBlocks, int totalBlocks)
{
	double val = -0.1;
	for(int i = 0; i < totalBlocks; i++)
	{
		if(theirBlocks[i] > val)
			val = theirBlocks[i];
	}
	return val;
}

int getMyLowIndex(double* myBlocks, int totalBlocks)
{
	double val = myBlocks[0];
	int ind = 0;
	int test;
	for(int i = 1; i < totalBlocks; i++)
	{
		test = myBlocks[i];
		if(myBlocks[i] < val)
		{
			val = myBlocks[i];
			ind = i;
		}
	}
	return ind;
}

int getMyHighIndex(double* myBlocks, int totalBlocks)
{
	double val = myBlocks[0];
	int ind = 0;
	for(int i = 1; i < totalBlocks; i++)
	{
		if(myBlocks[i] > val)
		{
			val = myBlocks[i];
			ind = i;
		}
	}
	return ind;
}

int getTheirLowIndex(double* theirBlocks, int totalBlocks)
{
	double val = theirBlocks[0];
	int ind = 0;
	for(int i = 1; i < totalBlocks; i++)
	{
		if(theirBlocks[i] < val)
		{
			val = theirBlocks[i];
			ind = i;
		}
	}
	return ind;
}

int getTheirHighIndex(double* theirBlocks, int totalBlocks)
{
	double val = theirBlocks[0];
	int ind = 0;
	for(int i = 1; i < totalBlocks; i++)
	{
		if(theirBlocks[i] > val)
		{
			val = theirBlocks[i];
			ind = i;
		}
	}
	return ind;
}

int getTheirLowAbove(double* theirBlocks, int totalBlocks, double myLow)
{
	double val = 1.1;
	int ind = 0;
	for(int i = 1; i < totalBlocks; i++)
	{
		if(theirBlocks[i] < val && theirBlocks[i] > myLow)
		{
			val = theirBlocks[i];
			ind = i;
		}
	}
	return ind;
}


int main(int argc, char *argv[])
{
	ifstream input(argv[1]);
	//input.open("test.txt");
	if(!input.is_open())
	{
		cout << "Error Opening";
		return 0;
	}

	double add;
	int total;
	input >> total;

	double* myBlocks;
	double* myBlocks2;
	double* theirBlocks;
	double* theirBlocks2;
	int totalBlocks;
	int totalBlocks2;
	int score = 0;

	for(int count = 0; count < total; count++)
	{
		cout << "Case #" << count + 1 << ": ";
		input >> totalBlocks;
		totalBlocks2 = totalBlocks;

		myBlocks = new double[totalBlocks];
		myBlocks2 = new double[totalBlocks];
		theirBlocks = new double[totalBlocks];
		theirBlocks2 = new double[totalBlocks];

		for(int i = 0; i < totalBlocks; i++)
		{
			input >> add;
			myBlocks[i] = add;
		}

		for(int i = 0; i < totalBlocks; i++)
		{
			myBlocks2[i] = myBlocks[i];
		}

		for(int i = 0; i < totalBlocks; i++)
		{
			input >> add;
			theirBlocks[i] = add;
		}
		
		for(int i = 0; i < totalBlocks; i++)
		{
			theirBlocks2[i] = theirBlocks[i];
		}

		while(totalBlocks != 0)
		{
			if(checkMyLowest(myBlocks, totalBlocks) < checkTheirLowest(theirBlocks, totalBlocks))
			{
				for (int i = getMyLowIndex(myBlocks, totalBlocks); i < totalBlocks; i++)
				{
					myBlocks[i] = myBlocks[i+1];
				}
				myBlocks[totalBlocks-1] = 0;

				for (int i = getTheirHighIndex(theirBlocks, totalBlocks); i < totalBlocks; i++)
				{
					theirBlocks[i] = theirBlocks[i+1];
				}
				theirBlocks[totalBlocks-1] = 0;
			}

			else if(checkMyHighest(myBlocks, totalBlocks) > checkTheirHighest(theirBlocks, totalBlocks))
			{
				for (int i = getMyLowIndex(myBlocks, totalBlocks); i < totalBlocks; i++)
				{
					myBlocks[i] = myBlocks[i+1];
				}
				myBlocks[totalBlocks-1] = 0;

				for (int i = getTheirLowIndex(theirBlocks, totalBlocks); i < totalBlocks; i++)
				{
					theirBlocks[i] = theirBlocks[i+1];
				}
				theirBlocks[totalBlocks-1] = 0;
				score++;
			}

			else
			{
				for (int i = getMyLowIndex(myBlocks, totalBlocks); i < totalBlocks; i++)
				{
					myBlocks[i] = myBlocks[i+1];
				}
				myBlocks[totalBlocks-1] = 0;

				for (int i = getTheirHighIndex(theirBlocks, totalBlocks); i < totalBlocks; i++)
				{
					theirBlocks[i] = theirBlocks[i+1];
				}
				theirBlocks[totalBlocks-1] = 0;
			}
			totalBlocks--;
		}
		cout << score << " ";
		score = 0;

		while(totalBlocks2 != 0)
		{
			if(checkMyHighest(myBlocks2, totalBlocks2) > checkTheirHighest(theirBlocks2, totalBlocks2))
			{
				for (int i = getTheirLowIndex(theirBlocks2, totalBlocks2); i < totalBlocks2; i++)
				{
					theirBlocks2[i] = theirBlocks2[i+1];
				}
				theirBlocks2[totalBlocks2-1] = 0;

				for (int i = getMyHighIndex(myBlocks2, totalBlocks2); i < totalBlocks2; i++)
				{
					myBlocks2[i] = myBlocks2[i+1];
				}
				myBlocks2[totalBlocks2-1] = 0;
				score++;
				totalBlocks2--;
			}
			else
			{
				for (int i = getTheirLowAbove(theirBlocks2, totalBlocks2, checkMyHighest(myBlocks2, totalBlocks2)); i < totalBlocks2; i++)
				{
					theirBlocks2[i] = theirBlocks2[i+1];
				}
				theirBlocks2[totalBlocks2-1] = 0;

				for (int i = getMyHighIndex(myBlocks2, totalBlocks2); i < totalBlocks2; i++)
				{
					myBlocks2[i] = myBlocks2[i+1];
				}
				myBlocks2[totalBlocks2-1] = 0;
				totalBlocks2--;
			}
		}

		cout << score << endl;

		delete[] myBlocks;
		delete[] myBlocks2;
		delete[] theirBlocks;
		delete[] theirBlocks2;
		score = 0;
	}
	return 0;
}