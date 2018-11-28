#include <iostream>
#include <vector>
#include <fstream>

std::ifstream fin("J:\\sedrak files\\Codes\\A-small-attempt1.in");
std::ofstream fout("C:\\Users\\Sedrak\\Desktop\\Ans.txt");

void Reading (int& CurrentLine, std::vector<std::vector<int>>& Cards)
{
	int k;
	//std::cin >> k;
	fin >> k;
	CurrentLine = k - 1;
	for(int i = 0; i < 4; ++i)
	{
		for(int j = 0; j < 4; ++j)
		{
			//std::cin >> Cards[i][j];
			fin >> Cards[i][j];
		}
	}
}

int main()
{
	
	int n;
	//std::cin >> n;
	fin >> n;
	for(int h = 1; h <= n; ++h)
	{
		int CurrentLine1;
		std::vector<std::vector<int>> Cards1 (4, std::vector<int> (4));
		Reading(CurrentLine1, Cards1);
		int CurrentLine2;
		std::vector<std::vector<int>> Cards2 (4, std::vector<int> (4));
		Reading(CurrentLine2, Cards2);
		int counter = 0;
		int ans = 0;
		for(int i = 0; i < 4; ++i)
		{
			for(int j = 0; j < 4; ++j)
			{
				if(Cards1[CurrentLine1][i] == Cards2[CurrentLine2][j])
				{
					++counter;
					ans = Cards1[CurrentLine1][i];
				}
			}
		}
		std::cout << "Case #" << h << ": ";
		fout << "Case #" << h << ": ";
		if(counter == 1)
		{
			std::cout << ans << "\n";
			fout << ans << "\n";
		}
		else if(counter == 0)
		{
			std::cout << "Volunteer cheated!\n";
			fout << "Volunteer cheated!\n";
		}
		else if(counter > 1)
		{
			std::cout << "Bad magician!\n";
			fout << "Bad magician!\n";
		}
	}
}