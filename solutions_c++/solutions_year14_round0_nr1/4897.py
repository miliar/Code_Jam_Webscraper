#include <iostream>
#include <fstream>

int compare(int first, int second, int firstArray[4][4], int secondArray[4][4])
{
	int count = 0;
	int number;

	int array1[4], array2[4];

	for(int i = 0; i < 4; i++)
	{
		array1[i] = firstArray[first - 1][i];
	}

	for(int i = 0; i < 4; i++)
	{
		array2[i] = secondArray[second - 1][i];
	}

	for(int i = 0; i < 4; i++)
	{
		for(int j = 0; j < 4; j++)
		{
			if(array1[i] == array2[j])
			{
				count++;
				number = array1[i];
			}
		}
	}

	if(count == 0)
	{
		return -2;
	}
	else if(count >= 2)
	{
		return -1;
	}
	else if(count == 1)
	{
		return number;
	}

}

int main()
{
	
	std::ifstream file;
	file.open("A-small-attempt0.in");

	std::ofstream outputFile("output.txt");


	int number;
	int firstRow, secondRow;
	int first[4][4], second[4][4];
	int k;

	file >> k;
	for(int l = 0; l < k; l++)
	{
		file >> firstRow;

		for(int i = 0; i < 4; i++)
		{
			for(int j = 0; j < 4; j++)
			{
				file >> first[i][j];
			}
		}
	
		file >> secondRow;
	
		for(int i = 0; i < 4; i++)
		{
			for(int j = 0; j < 4; j++)
			{
				file >> second[i][j];
			}
		}
	
		number = compare(firstRow, secondRow, first, second);
	
		if(number == -1)
		{
			outputFile << "Case #" << l + 1 << ": Bad magician!" << std::endl;
		}
	
		else if(number == -2)
		{
			outputFile << "Case #" << l + 1 << ": Volunteer cheated!" << std::endl;
		}
	
		else
		{
			outputFile << "Case #" << l + 1 << ": " << number << std::endl;
		}
	}
	return 0;
}