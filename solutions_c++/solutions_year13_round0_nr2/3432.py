#include <iostream>
#include <string>
#include <fstream>
#include <vector>
#include <stdio.h>
#include <math.h>
#include <queue>

using namespace std;
using namespace stdext;

bool openFileHandles(ifstream& readFile, const string& inFile, ofstream& writeFile, const string& outFile);

struct Square
{
	int height;
	bool visited;

	Square(int h=0, bool v=false)
		: height(h), visited(v)
	{}
};

int main()
{
	// files
	ifstream readFile;
	ofstream writeFile;
	
	//string fileIn("practice");
	//string fileIn("small");
	string fileIn("large");

	if (!openFileHandles(readFile, fileIn + ".txt", writeFile, fileIn + "_out.txt"))
		return -1;

	// read # of lines
	int T;
	readFile >> T;
	readFile.get();  // get rid of the newline

	// for each test case, ...
	for (int t = 0; t < T; ++t)
	{
		int N, M;
		readFile >> N >> M;

		// populate the lawn
		vector<vector<Square> > lawn(N);
		for (int r = 0; r < N; ++r)
		{
			lawn[r].resize(M);
			for (int c = 0; c < M; ++c)
			{
				Square s;
				readFile >> s.height;
				lawn[r][c] = s;
			}
		}

		// mowe the lawn
		int visitedCount = 0;

		// 1. mowe rows
		for (int r = 0; r < N; ++r)
		{
			// max height for this row
			int bladeHeight(-1);
			for (int c = 0; c < M; ++c)
				if (lawn[r][c].height > bladeHeight)
					bladeHeight = lawn[r][c].height;

			// mowe rows
			for (int c = 0; c < M; ++c)
			{
				if (lawn[r][c].height != bladeHeight ||
					lawn[r][c].visited)
				{ continue; }
				
				lawn[r][c].visited = true;
				++visitedCount;
			}
		}

		// 2. mowe columns
		for (int c = 0; c < M; ++c)
		{
			// max height for this col
			int bladeHeight(-1);
			for (int r = 0; r < N; ++r)
				if (lawn[r][c].height > bladeHeight)
					bladeHeight = lawn[r][c].height;

			// mowe cols
			for (int r = 0; r < N; ++r)
			{
				if (lawn[r][c].height != bladeHeight ||
					lawn[r][c].visited)
				{ continue; }
				
				lawn[r][c].visited = true;
				++visitedCount;
			}
		}

		//  if visitedCount == N*M, we've cut all squares to desired height
		//cout << "Case #" << t+1 << ": " << (visitedCount == N*M ? "YES" : "NO") << endl;
		writeFile << "Case #" << t+1 << ": " << (visitedCount == N*M ? "YES" : "NO") << endl;
	}  // for (n)

	// close file handles
	readFile.close();
	writeFile.close();

	// no error
	return 0;
}

bool openFileHandles(ifstream& readFile, const string& inFile, ofstream& writeFile, const string& outFile)
{
	// input file
	readFile.open(inFile.c_str());
	if (!readFile)
	{
		cout << "Could not find '" << inFile << "'\n\n";
		return false;
	}

	// output file
	writeFile.open(outFile.c_str());
	if (!writeFile)
	{
		cout << "Could not find '" << outFile << "'\n\n";
		return false;
	}

	return true;
}
