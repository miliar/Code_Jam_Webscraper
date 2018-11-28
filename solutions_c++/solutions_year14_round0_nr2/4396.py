#include <fstream>
#include <iostream>
using namespace std;

void readGrid(int * grid, ifstream &fin)
{
	for (int i = 0; i < 4; i++)
	{
		for (int j = 0; j < 4; j ++)
		{
			fin>>grid[i*4+j];
		}
	}
}

void problem1()
{
	ifstream fin("input1.txt");
	ofstream fout("output1.txt");
	int numcases;
	int row1,row2;
	int grid1[16];
	int grid2[16];
	fin>>numcases;

	for (int i=0;i<numcases;i++)
	{
		fin>>row1;
		row1--;
		readGrid(grid1, fin);
		fin>>row2;
		row2--;
		readGrid(grid2, fin);

		int matchCount = 0;
		int matchNumber;
		for (int j = 0; j < 4; j++)
		{
			for (int k = 0; k < 4; k++)
			{
				if (grid1[row1*4 + j] == grid2[row2*4 + k])
				{
					matchCount++;
					matchNumber = grid1[row1*4 + j];
				}
			}
		}

		fout<<"Case #"<<i + 1<<": ";

		if (matchCount == 1)
		{
			fout<<matchNumber;
		}
		else if (matchCount == 0)
		{
			fout<<"Volunteer cheated!";
		}
		else
		{
			fout <<"Bad magician!";
		}
		fout<<endl;
	}
}

double calcTimeWithNFarms(double farmCost, double farmBonus, double scoreLimit, int n)
{
	double time = 0.0;
	const double baseCookieRate = 2.0;

	// Calculate time to build all farms
	for (int i = 0; i< n; i++)
	{
		time += farmCost/(baseCookieRate + farmBonus*i);
	}

	// Calculate time to get to the score limit once all farms have been made
	time += scoreLimit/(baseCookieRate + n*farmBonus);

	return time;

}

double solveProblem2(double farmCost, double farmBonus, double scoreLimit)
{
	int farmCount = 1;
	double fastestTimeSoFar = scoreLimit/2.0; // The time when there are no farms
	while(true)
	{
		double currentTime = calcTimeWithNFarms(farmCost, farmBonus, scoreLimit, farmCount);
		
		if (currentTime > fastestTimeSoFar)
			return fastestTimeSoFar;

		fastestTimeSoFar = currentTime;
		farmCount++;
	}

}

void problem2()
{
	ifstream fin("input2.txt");
	ofstream fout("output2.txt");
	fout.precision(7);
	

	int numcases;
	double farmCost, farmBonus, scoreLimit;
	fin>>numcases;
	for(int i=0;i<numcases;i++)
	{
		fin>>farmCost>>farmBonus>>scoreLimit;
		double solution = solveProblem2(farmCost,farmBonus, scoreLimit);
		fout<<"Case #"<<i + 1<<": "<< std::fixed << solution<<endl;
		cout<<"Done Case #"<<i + 1<<endl;
	}
}
void main()
{

	problem2();
}

