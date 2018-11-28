#include <iostream>
#include <string>
#include <fstream>
#include <vector>
#include <algorithm>
using namespace std;

int max(int a, int b)
{
	return (a > b) ? a : b;
}
int min(int a, int b)
{
	return (a < b) ? a : b;
}
int decide(int maxCake, int n, int pancake[])
{
	int minDecide = maxCake;

	for (int i = 1; i < maxCake; i++)
	{
		int decide = 0;
		int eat = i;
		for (int j = 0; j < n; j++)
		{
			if (pancake[j] > i)
			{
				if (pancake[j] % i == 0)
					decide += pancake[j] / i - 1;
				else
				{
					decide += pancake[j] / i;
				}
			}
		}
		decide = eat + decide;
		minDecide = min(minDecide, decide);
	}
	return minDecide;
}
int main()
{
	int t = 0;
	ifstream input;
	ofstream output;

	input.open("B-large.in");
	output.open("B-large.out", ios::app);
	input >> t;
	for (int i = 0; i < t; i++)
	{
		int n = 0;
		input >> n;
		int *pancake = new int[n];
		int maxCake = 0;
		for (int j = 0; j < n; j++)
		{
			input >> pancake[j];
			maxCake = max(maxCake, pancake[j]);
		}
		int count_num = decide(maxCake, n, pancake);
		output << "Case #" << i + 1 << ": " << count_num << endl;
	}
	return 0;
}