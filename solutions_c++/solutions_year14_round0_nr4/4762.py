#include <iostream>
#include <fstream>
#include <numeric>
#include <functional>

void swap(double (&data)[1000], int index1, int index2)
{
	double temp = data[index1];
	data[index1] = data[index2];
	data[index2] = temp;
}

int partition(double (&data)[1000], int min, int max)
{
	double partitionValue = data[min];
	int left = min;
	int right = max;

	while (left < right)
    {
		while (data[left] - (partitionValue) <= 0 && left < right)
		{
			left++;
		}
		while (data[right] - (partitionValue) > 0)
		{
			right--;
		}

		if (left < right) 
		{
			swap(data, left, right);
		}
	}

	swap (data, min, right);

	return right;
}

void quicksort(double (&data)[1000], int min, int max)
{
	int pivot;

	if(min < max)
	{
		pivot = partition(data, min, max);
		quicksort(data, min, pivot - 1);
		quicksort(data, pivot + 1, max);
	}
}

int war(int blocks, double (&naomi)[1000], double (&ken)[1000])
{
	int score = 0;

	for(int i = 0; i < blocks; blocks--)
	{
		bool sentinel = false;
		
		for(int j = 0; j < blocks; j++)
		{
			if(naomi[i] < ken[j])
			{
				for(int k = i; k < blocks; k++)
				{
					naomi[k] = naomi[k + 1];
				}
				for(int k = j; k < blocks; k++)
				{
					ken[k] = ken[k + 1];
				}
				sentinel = true;
				break;
			}
		}

		if(sentinel != true)
		{
			score++;
			for(int k = i; k < blocks; k++)
			{
				naomi[k] = naomi[k + 1];
				ken[k] = ken[k + 1];
			}
		}
		naomi[blocks - 1] = NULL;
		ken[blocks - 1] = NULL;
	}

	return score;
}

int deceit(int blocks, double (&naomi)[1000], double (&ken)[1000])
{
	int score = 0;
	int temp = 0;

	if(blocks == 1)
	{
		if(naomi[0] > ken[0])
		{
			return 1;
		}
		else
		{
			return 0;
		}
	}

	if(naomi[1] > ken[blocks - 1])
	{
		return blocks;
	}

	for(int i = 0; i < blocks; blocks--)
	{
		bool sentinel = false;

		for(int j = 0; j < blocks; j++)
		{
			if(naomi[j] < ken[j])
				sentinel = true;
		}

		if(sentinel == true)
		{
			for(int k = i; k < blocks; k++)
			{
				naomi[k] = naomi[k + 1];
			}
			for(int k = blocks - 1; k < blocks; k++)
			{
				ken[k] = ken[k + 1];
			}
		}

		else
		{
			return blocks;
		}

	}

	return score;
}

int main()
{
	std::ifstream file;
	file.open("D-large.in");

	std::ofstream outputFile("output.txt");

	double naomi[1000], naomiCopy[1000];
	double ken[1000], kenCopy[1000];
	int blocks;
	int scoreWar, scoreDeceit;
	int i;

	file >> i;

	for(int j = 0; j < i; j++)
	{
		file >> blocks;
	
		for(int i = 0; i < blocks; i++)
		{
			file >> naomi[i];		
		}
	
		for(int i = 0; i < blocks; i++)
		{
			file >> ken[i];		
		}
	
		quicksort(naomi, 0, blocks - 1);
		quicksort(ken, 0, blocks - 1);
	
		for(int i = 0; i < 1000; i++)
		{
			naomiCopy[i] = naomi[i];
			kenCopy[i] = ken[i];
		}
		scoreWar = war(blocks, naomiCopy, kenCopy);
	
		for(int i = 0; i < 1000; i++)
		{
			naomiCopy[i] = naomi[i];
			kenCopy[i] = ken[i];
		}
		scoreDeceit = deceit(blocks, naomiCopy, kenCopy);
	
		outputFile << "Case #" << j + 1 << ": " << scoreDeceit << " " << scoreWar << std::endl;
	}

	return 0;
}