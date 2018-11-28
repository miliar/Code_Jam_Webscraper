#include<iostream>
#include<fstream>
#include<string>
#include<vector>
#include<map>

using namespace std;

int getNumber(string);
int getNumber(char);
void populateLawn(vector<vector<int>> &, int, int, ifstream&);
int getPlaceValue(int, int);
bool checkLawn(vector<vector<int>> &);

int main()
{
	string inputFilePath = "B-small-attempt2.in";
	string outputFilePath = "bsmalloutput2.txt";
	string input;
	// Input file
	ifstream inputFile;
	int cases;
	inputFile.open(inputFilePath);
	inputFile >> cases;
	vector<vector<vector<int>>> lawns (cases);
	for (int i = 0; i < cases; i++)
	{
		int lines;
		int columns;

		inputFile >> input;
		lines = getNumber(input);

		inputFile >> input;
		columns = getNumber(input);
		
		vector<vector<int>> lawn (lines);

		for (int j = 0; j < lawn.size(); j++)
		{
			lawn[j] = vector<int> (columns);
		}
		
		populateLawn(lawn, lines, columns, inputFile);
		
		lawns[i] = lawn;
	}

	string outcomes = "";

	for (int i = 0; i < lawns.size(); i++)
	{
		outcomes += "Case #" + to_string(static_cast<long long>(i + 1)) + ": ";
		bool impossible = checkLawn(lawns[i]);
		if (impossible)
		{
			outcomes += "NO";
		}
		else
		{
			outcomes += "YES";
		}
		if (i < (lawns.size() - 1))
		{
			outcomes += "\n";
		}
	}

	ofstream outputFile;
	outputFile.open(outputFilePath);
	outputFile << outcomes;
	return 0;
}

bool checkLawn(vector<vector<int>> &lawn)
{
	bool impossible = false;
	map<int, int> rowMaxes;
	map<int, int> colMaxes;

	int rows = lawn.size();
	int cols = lawn[0].size();

	for (int row = 0; row < rows; row++)
	{
		rowMaxes[row] = 0;
	}

	for (int col = 0; col < cols; col++)
	{
		colMaxes[col] = 0;
	}

	for (int row = 0; row < rows; row++)
	{
		for (int col = 0; col < cols; col++)
		{
			int value = lawn[row][col];
			if (value > rowMaxes[row])
			{
				rowMaxes[row] = value;
			}

			if (value > colMaxes[col])
			{
				colMaxes[col] = value;
			}
		}
	}

	for (int row = 0; row < rows; row++)
	{
		for (int col = 0; col < cols; col++)
		{
			int value = lawn[row][col];
			if ((value < rowMaxes[row]) && (value < colMaxes[col]))
			{
				impossible = true;
			}
		}
	}
	return impossible;
}

void populateLawn(vector<vector<int>> &lawn, int rows, int columns, ifstream& inputFile)
{
	for (int row = 0; row < rows; row++)
	{		
		for (int column = 0; column < columns; column++)
		{
			string number;
			inputFile >> number;
			lawn[row][column] = getNumber(number);
		}
	}
}

// Convert ASCII character representation of an integer into an integer
int getNumber(char nChar)
{
	return nChar - '0';
}

int getNumber(string nString)
{
	int total = 0;
	for (int i = 0; i < nString.size(); i++)
	{
		char num = nString[i];
		int value = getNumber(num);
		total += value * getPlaceValue(nString.size(), i);
	}
	return total;
}

int getPlaceValue(int total, int location)
{
	int diff = (total - (location + 1));
	if (diff == 0)
	{
		return 1;
	}
	else
	{
		return diff * 10;
	}
}

// Input file