#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
#include <vector>
#include <math.h>
#include <algorithm>

//Input and Output Files
std::ifstream reader ("C:\\Users\\Dave\\Downloads\\A-small-attempt0.in");
std::ofstream writer("C:\\Users\\Dave\\Documents\\Code Jam\\2014\\bad-magician.out");

int main()
{
	//Check files are ok
	if (!reader)
	{
		std::cout << "Error opening file for input" << std::endl;
		return -1;
	}
	if (!writer)
	{
		std::cout << "Error opening file for output" << std::endl;
		return -1;
	}
	
	int t = 0; //Test Cases
	int x = 0; //Case Number
	int firstNumber = 0; //Row
	int secondNumber = 0; //Row
	int card = 0;
	std::string row1;
	std::string row2;
	int found = 0;
	std::string status;

	reader >> t;

	for(x = 0;x < t;x++)
	{
		row1.clear();
		row2.clear();
		firstNumber = 0;
		secondNumber = 0;
		card = 0;
		status.clear();
		found = 0;

		reader >> firstNumber;
		for(int y=1;y<5;y++)
		{
			if(y==firstNumber)
			{
				reader >> card;
				row1.push_back (card);
				reader >> card;
				row1.push_back (card);
				reader >> card;
				row1.push_back (card);
				reader >> card;
				row1.push_back (card);
			}
			else
			{
				reader >> card;
				reader >> card;
				reader >> card;
				reader >> card;
			}
		}

		reader >> secondNumber;
		for(int z=1;z<5;z++)
		{
			if(z==secondNumber)
			{
				reader >> card;
				row2.push_back (card);
				reader >> card;
				row2.push_back (card);
				reader >> card;
				row2.push_back (card);
				reader >> card;
				row2.push_back (card);
			}
			else
			{
				reader >> card;
				reader >> card;
				reader >> card;
				reader >> card;
			}
		}

		int card1 = 0;
		int card2 = 0;
		int card3 = 0;
		int card4 = 0;

		card1 = row1.at(0);
		card2 = row1.at(1);
		card3 = row1.at(2);
		card4 = row1.at(3);

		std::size_t A = row2.find(card1);
		std::size_t B = row2.find(card2);
		std::size_t C = row2.find(card3);
		std::size_t D = row2.find(card4);

		if( A!= std::string::npos)
		{
			found = found + 1;
		}

		if( B!= std::string::npos)
		{
			found = found + 2;
		}

		if( C!= std::string::npos)
		{
			found = found + 4;
		}
		
		if( D!= std::string::npos)
		{
			found = found + 8;
		}

		writer << "Case #" << x + 1 << ": ";

		switch(found)
		{
			case 0:
				writer << "Volunteer cheated!";
				break;
			case 1:
				writer << card1;
				break;
			case 2:
				writer <<  card2;
				break;
			case 4:
				writer <<  card3;
				break;
			case 8:
				writer <<  card4;
				break;
			default:
				writer << "Bad magician!";
		}

		writer << std::endl;

	}


	//Clean Up
	reader.close();
	writer.close();
	return 0;
}
