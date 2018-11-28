#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
using namespace std;

int main()
{
	ifstream infile("B-large.in");
	ofstream outfile("output.txt");

	int numProblems;
	infile >> numProblems;

	string line;

	getline(infile, line);

	for (int problem = 1; problem <= numProblems; problem++)
	{
		getline(infile, line);

		stringstream ss(line);

		int X;
		int Y;

		ss >> Y >> X;

		vector< vector<int> > gridMap;

		for (int yIT = 0; yIT < Y; yIT++)
		{
			vector<int> yROW;

			getline(infile, line);

			stringstream ss(line);

			for (int xIT = 0; xIT < X; xIT++)
			{
				int curNum;
				ss >> curNum;
				yROW.push_back(curNum);
			}

			gridMap.push_back(yROW);
		}

		bool able = true;

		// Brute each of the points and find if it is not trapped in
		for (int yIT = 0; yIT < Y; yIT++)
		{
			for (int xIT = 0; xIT < X; xIT++)
			{
				int max = gridMap[yIT][xIT];
				int dirFailed = 0;

				for (int curAxis = 0; curAxis < Y; curAxis++)
				{
					if (gridMap[curAxis][xIT] > max)
					{
						dirFailed++;
						break; // Impossible in this direction
					}
				}

				for (int curAxis = 0; curAxis < X; curAxis++)
				{
					if (gridMap[yIT][curAxis] > max)
					{
						dirFailed++;
						break; // Impossible in this direction
					}
				}

				if (dirFailed == 2)
				{
					able = false;
					goto endSolution;
				}
			}
		}

endSolution:

		if (!able)
		{
			outfile << "Case #" << problem << ": NO" << endl;
		}
		else
		{
			outfile << "Case #" << problem << ": YES" << endl;
		}
	}

	int x;
	cin >> x;
}