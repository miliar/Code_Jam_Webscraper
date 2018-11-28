// GCJProb1.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"

char *ReadInput()
{
	std::ifstream in("c:\\gcj\\input.txt", std::ios::in | std::ios::binary);
	if (in)
	{			
		in.seekg(0, std::ios::end);
		unsigned int length = (unsigned int)in.tellg();
		char *buffer = new char[length + 1];		
		cout << "Length :- " << length << "\n";
		in.seekg(0, std::ios::beg);
		in.read(buffer, length);
		buffer[length] = '\0';		
		in.close();
		return buffer;
	}
	return NULL;
}

int GetNumberOfTestCases(char *buffer, char **outptr)
{
	char *start = buffer;
	while(*buffer != '\n')
	{
		buffer++;
	}
	*buffer = '\0';

	int numberOfTestCases = atoi(start);
	*outptr = buffer + 1;
	return numberOfTestCases;
}

#define V_DOT 0
#define V_O 1
#define V_X 2
#define V_T 3
#define V_INVALID 4

int GetMapping(char val)
{
	switch(val)
	{
	case 'X':
		return V_X;
	case 'O':
		return V_O;
	case 'T':
		return V_T;
	case '.':
		return V_DOT;
	default:
		return V_INVALID;
	}
}

#define X_WON 0
#define O_WON 1
#define DRAW 2
#define INCOMPLETE 3

#define CASE_NO "Case #"

#define X_WON_STR ": X won"

#define O_WON_STR ": O won"

#define DRAW_STR ": Draw"

#define INCOMPLETE_STR ": Game has not completed"

char *GetNextRow(char *buffer, int *row)
{
	for(int i = 0; i < 4; i++)
	{
		row[i] = GetMapping(buffer[i]);
	}
	return buffer + 4;	
}

void PrintResults(int *results, unsigned int resultLen)
{
	std::ofstream outfile("c:\\gcj\\output.txt", std::ios::out);
	
	for(unsigned int i = 0; i < resultLen; i++)
	{
		char *endchar = (i == resultLen - 1) ? "" : "\n";
		switch(results[i])
		{
		case X_WON:
			outfile << CASE_NO << (i + 1) << X_WON_STR << endchar;
			break;
		case O_WON:
			outfile << CASE_NO << (i + 1) << O_WON_STR << endchar;
			break;
		case DRAW:
			outfile << CASE_NO << (i + 1) << DRAW_STR << endchar;
			break;
		case INCOMPLETE:			
			outfile << CASE_NO << (i + 1) << INCOMPLETE_STR << endchar;
			break;
		default:
			break;
		}
	}

	outfile.close();
}

bool FoundResult(int hash[5], int *results, int t, bool &isInComplete)
{
	int currentResult = DRAW;

	if(hash[V_DOT] != 0)
	{
		currentResult = INCOMPLETE;
		isInComplete = true;
	}
	else if(hash[V_O] == 4)
	{
		results[t] = O_WON;
		return true;
	}
	else if(hash[V_X] == 4)
	{
		results[t] = X_WON;
		return true;
	}
	else if(hash[V_T] == 1)
	{
		if(hash[V_O] == 3)
		{
			results[t] = O_WON;
			return true;
		}
		else if(hash[V_X] == 3)
		{
			results[t] = X_WON;
			return true;
		}
	}	

	return false;
}

void FindWhoWon(int matrix[4][4], int *results, int t)
{
	int hash[5] = {0};
	bool isInComplete = false;

	memset(hash, 0, 5*sizeof(int));
	hash[matrix[0][0]] += 1;
	hash[matrix[1][1]] += 1;
	hash[matrix[2][2]] += 1;
	hash[matrix[3][3]] += 1;
	if(FoundResult(hash, results, t, isInComplete))
		return;

	memset(hash, 0, 5*sizeof(int));
	hash[matrix[3][0]] += 1;
	hash[matrix[2][1]] += 1;
	hash[matrix[1][2]] += 1;
	hash[matrix[0][3]] += 1;
	if(FoundResult(hash, results, t, isInComplete))
		return;

	for(int row = 0; row < 4; row++)
	{
		memset(hash, 0, 5*sizeof(int));
		for(int col = 0; col < 4; col++)
		{
			hash[matrix[row][col]] += 1;
		}
		if(FoundResult(hash, results, t, isInComplete))
			return;
	}

	for(int col = 0; col < 4; col++)
	{
		memset(hash, 0, 5*sizeof(int));
		for(int row = 0; row < 4; row++)
		{
			hash[matrix[row][col]] += 1;
		}
		if(FoundResult(hash, results, t, isInComplete))
			return;
	}

	results[t] = isInComplete ? INCOMPLETE: DRAW; 
}

int _tmain(int argc, _TCHAR* argv[])
{	
	// read input
	char *buffer = ReadInput();
	//cout << buffer;

	// get no of test cases
	char *nextChar;
	int numberOfTestCases = GetNumberOfTestCases(buffer, &nextChar);
	cout << "Number of cases " << numberOfTestCases << "\n";

	// iterate through test cases and generate results
	int matrix[4][4];
	int *results = new int[numberOfTestCases];
	for(int t = 0; t < numberOfTestCases; t++)
	{
		for(int row = 0; row < 4; row++)
		{
			nextChar = GetNextRow(nextChar, matrix[row]);
			nextChar += 1;
		}
		
		nextChar += 1;

		FindWhoWon(matrix, results, t);
	}	
	
	// output results
	PrintResults(results, numberOfTestCases);

	cout << "*******Done with test cases*********\n";

	// cleanup
	delete [] buffer;
	cin.get();
	return 0;
}