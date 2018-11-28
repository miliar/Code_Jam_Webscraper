/*
 * main.cpp
 *
 *  Created on: Apr 12, 2013
 *      Author: madagarw
 */

#include <cstdlib>
#include <iostream>
#include <fstream>
class TTTT
{
public:
	void read(std::istream& in)
	{
		bEmpty = false;
		static char line[256];
		for(int i = 0; i < 4; ++i)
		{
			in.getline(line, 256, '\n');
			for(int j = 0; j < 4; ++j)
			{
				switch(line[j])
				{
				case 'X':	rc[i][j] = 10; break;
				case 'O':	rc[i][j] = 1; break;
				case 'T':	rc[i][j] = 0; break;
				case '.':	rc[i][j] = -1; bEmpty = true;break;
				}
			}
		}
		in.getline(line, 256, '\n');
	}
	char getWinner()
	{
		char diag1Sum = 0;
		char diag2Sum = 0;
		//check all rows
		for(int i = 0; i < 4; ++i)
		{
			char sum = 0;
			char sum1 = 0;
			for(int j = 0; j < 4; ++j)
			{
				sum += rc[i][j];
				sum1 += rc[j][i];
				if(i == j)
					diag1Sum += rc[i][j];
				if(i + j == 3)
					diag2Sum += rc[i][j];
			}
			switch(sum)
			{
			case 3:
			case 4:
				return 'O';
			case 30:
			case 40:
				return 'X';
			}
			switch(sum1)
			{
			case 3:
			case 4:
				return 'O';
			case 30:
			case 40:
				return 'X';
			}
		}
		switch(diag1Sum)
		{
		case 3:
		case 4:
			return 'O';
		case 30:
		case 40:
			return 'X';
		}
		switch(diag2Sum)
		{
		case 3:
		case 4:
			return 'O';
		case 30:
		case 40:
			return 'X';
		}

		return bEmpty ? -1 : 0;
	}
	void writeResult(int caseNo, std::ostream& out)
	{
		char winner = getWinner();
		out << "Case #" << (caseNo + 1) << ": ";
		switch(winner)
		{
		case 0:	out << "Draw";	break;
		case -1: out << "Game has not completed";	break;
		default: out << winner << " won";	break;
		}
		out << "\n";
	}
private:
	char rc[4][4];
	bool bEmpty;
};

int main()
{
	std::ifstream inFile("A-large.in");
	std::istream& in = inFile;
	//std::istream& in = std::cin;
	int numTest = 0;
	char line[256];
	in.getline(line, 256, '\n');
	numTest = atoi(line);
	for(int i = 0; i < numTest; ++i)
	{
		TTTT game;

		game.read(in);
		game.writeResult(i, std::cout);
	}
}
