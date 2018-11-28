#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <stack>
#include <iomanip>
#include <cstdlib>

using namespace std;

//const char inputFile[] = "D-small-attempt2.in";
const char inputFile[] = "D-large.in";
const char outputFile[] = "results.out";

int playDeceitfulWar(double *array1, double *array2, int size);
int playWar(double *array1, double *array2, int size);
void sortAscending(double *array, int size);

int main()
{
	ifstream input;
	input.open(inputFile);
	
	ofstream output;
	output.open(outputFile);
	
	int N;
	input >> N;
	
	for (int a = 0; a < N; a++)
	{
		int n;
		input >> n;
		
		double *blocksNaomi = new double[n];
		double *blocksKen = new double[n];
		
		for (int i = 0; i < n; i++)
			input >> blocksNaomi[i];
		for (int i = 0; i < n; i++)
			input >> blocksKen[i];
		
		int scoreNaomi;
		
		output << "Case #" << a + 1 << ": ";
		scoreNaomi = playDeceitfulWar(blocksNaomi, blocksKen, n);
		output << scoreNaomi << " ";
		
		scoreNaomi = playWar(blocksNaomi, blocksKen, n);
		output << scoreNaomi << endl;
		
		delete []blocksNaomi;
		delete []blocksKen;
	}
	
	return 0;
}

int playDeceitfulWar(double *array1, double *array2, int size)
{
	int score = 0;
	
	double blocksNaomi[size];
	double blocksKen[size];
	
	for (int i = 0; i < size; i++)
	{
		blocksNaomi[i] = array1[i];
		blocksKen[i] = array2[i];
	}
		
	sortAscending(blocksNaomi, size);
	sortAscending(blocksKen, size);
	
	for (int i = 0; i < size; i++)
		for (int j = 0; j < size; j++)
		{
			if (blocksNaomi[i] != -1 && blocksKen[j] != -1)
			{
				if (blocksNaomi[i] > blocksKen[j])
				{
					blocksNaomi[i] = blocksKen[j] = -1;
					score++;
					continue;
				}
				else if (blocksNaomi[i] < blocksKen[j])
				{
					for (int k = size - 1; k > j + 1; k--)
						if (blocksKen[k] != -1 && blocksNaomi[i] < blocksKen[k])
						{
							if (blocksNaomi[i] == -1)
								break;
							blocksNaomi[i] = blocksKen[k] = -1;
						}
				}
			}
		}
	return score;
}

int playWar(double *array1, double *array2, int size)
{
	int score = size;
	
	double blocksNaomi[size];
	double blocksKen[size];
	
	for (int i = 0; i < size; i++)
	{
		blocksNaomi[i] = array1[i];
		blocksKen[i] = array2[i];
	}
	
	sortAscending(blocksNaomi, size);
	sortAscending(blocksKen, size);
	
	for (int i = 0; i < size; i++)
	{			
		int k = -1;
		for (int j = 0; j < size; j++)
			if (blocksKen[j] > blocksNaomi[i] && blocksNaomi[i] != -1)
			{
				blocksKen[j] = blocksNaomi[i] = -1;
				score--;
			}
	}
		
	return score;
}

void sortAscending(double *array, int size)
{
	do
	{
		for (int i = 0; i < size - 1; i++)
			if (array[i] > array[i + 1])
			{
				double temp = array[i];
				array[i] = array[i + 1];
				array[i + 1] = temp;
			}
		size--;
	}
	while (size > 1);
}






