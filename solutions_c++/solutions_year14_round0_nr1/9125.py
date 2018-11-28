#include <iostream>
#include <fstream>

int main()
{
	int amountOfTests;
	int* DataFirstTry = new int[16];
	int  RowFirstTry;
	int* DataSecondTry = new int[16];
	int  RowSecondTry;

	std::ifstream myfile("A-small-attempt2.in");
	std::ofstream output;
	output.open("output.txt");

	if( myfile.is_open() )
	{
		myfile >> amountOfTests;
		
		for (int testIndex = 0; testIndex < amountOfTests; ++testIndex)
		{
			myfile >> RowFirstTry;
			
			for (int dataIndex = 0; dataIndex < 16; ++dataIndex)
			{ 
				myfile >> DataFirstTry[dataIndex];				
			}

			myfile >> RowSecondTry;
			
			for (int dataIndex = 0; dataIndex < 16; ++dataIndex)
			{
				myfile >> DataSecondTry[dataIndex];
			}
			
			int possibleAnswers = 0;
			int theNumber = -1;
			for (int i = 0; i < 4; ++i)
			{
				int first = *(DataFirstTry + (RowFirstTry - 1) * 4 + i);
				for (int dataIndex = 0; dataIndex < 4; ++dataIndex)
				{
					int second = *(DataSecondTry + (RowSecondTry - 1) * 4 + dataIndex);

					if (first == second)
					{
						theNumber = first;
						possibleAnswers++;
					}
				}
			}

			output << "Case #" << (testIndex + 1) << ": ";

			if (possibleAnswers == 0)
			{
				output << "Volunteer cheated!\n";
			}
			else if (possibleAnswers == 1)
			{
				output << theNumber << std::endl;
			}
			else if (possibleAnswers > 1)
			{
				output << "Bad magician!\n";
			}			
		}

		myfile.close();
		output.close();
	}
	
	delete[] DataFirstTry;
	delete[] DataSecondTry;

	return 0;
}