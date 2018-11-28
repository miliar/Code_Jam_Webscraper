#include <iostream>
#include <fstream>
#include <vector>
#include <cstdlib>


int main()
{
	int cards1[4][4];
	int cards2[4][4];
	int firstRow;
	int secondRow;
	int totalGames = 0;
	std::ifstream inFile;
	inFile.open("input.txt", std::ifstream::in);
	char temp[5];
	inFile.getline(temp, 5);
	totalGames = atoi(temp);
	for(int i = 0; i < totalGames; i++)
	{
		inFile.getline(temp, 5);
		firstRow = atoi(temp);
		for(int j = 0; j < 4; j++)
		{
			for(int k = 0; k < 3; k++)
			{
				inFile.getline(temp, 5, ' ');
				cards1[j][k] = atoi(temp);
			}
			inFile.getline(temp, 5);
			cards1[j][3] = atoi(temp);
		}
		inFile.getline(temp, 5);
		secondRow = atoi(temp);
		for(int j = 0; j < 4; j++)
		{
			for(int k = 0; k < 3; k++)
			{
				inFile.getline(temp, 5, ' ');
				cards2[j][k] = atoi(temp);
			}
			inFile.getline(temp, 5);
			cards2[j][3] = atoi(temp);
		}
		int count = 0;
		int cardValue;
		for(int j = 0; j < 4; j++)
		{
			for(int k = 0; k < 4; k++)
			{
				if(cards1[firstRow - 1][j] == cards2[secondRow - 1][k])
				{
					count++;
					cardValue = cards1[firstRow - 1][j];
				}
			}
		}
		std::cout<<"Case #"<<i+1<<": ";
		if(count == 1)
		{
			std::cout<<cardValue<<std::endl;
		}
		else if(count > 1)
		{
			std::cout<<"Bad magician!"<<std::endl;
		}
		else
		{
			std::cout<<"Volunteer cheated!"<<std::endl;
		}
	}
	return 0;
}
