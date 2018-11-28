#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <time.h>
#include <conio.h>
#include <errno.h>
#include <stdarg.h>

#include <string>
#include <vector>
#include <map>

#include <iostream>
#include <iterator>
#include <fstream>

#define FOPEN(f, name, rights) f = fopen(name, rights); if(f == NULL) { printf("FOPEN failed to fopen('%s', '%s')!\n", name, rights); return 1; }

#define FILE_PREFIX		"A"
#define PROBLEM_NAME	"TicTacToeTomek"


bool notComplete = false;
const int nDefaultTestType = 0; 
// 0 - data from task, 1 - Small Test, 2 - Big Test


std::string problem(std::vector<char>& v)
{
	bool win = false;
	std::string result;
	
	char x = 'X';
	char o = 'O';
	
	for( int i = 0; i < 4; ++i)
	{
		int fullX = 0;
		int fullO = 0;

		for( int j = 0; j < 4; ++j)
		{
			if( (int)(v[ i * 4 + j ] - x) == 0 || (int)(v[ i * 4 + j ] - x) == -4)
			{
				++fullX;
			}  else continue;
		}
		for( int j = 0; j < 4; ++j)
		{
			if( (int)(v[ i * 4 + j ] - o) == 0 || (int)(v[ i * 4 + j ] - o) == 5)
			{
				++fullO;
			}  else continue;
		}
		if(fullX == 4)
		{
			return result = "X won";
		}
		if(fullO == 4)
		{
			return result = "O won";
		}
	}

	for( int j = 0; j < 4; ++j)
	{
		int fullX = 0;
		int fullO = 0;

		for( int i = 0; i < 4; ++i)
		{
			if( (int)(v[ i * 4 + j ] - x) == 0 || (int)(v[ i * 4 + j ] - x) == -4)
			{
				++fullX;
			} else continue;
		}

		for( int i = 0; i < 4; ++i)
		{

			if( (int)(v[ i * 4 + j ] - o) == 0 || (int)(v[ i * 4 + j ] - o) == 5)
			{
				++fullO;
			} else continue;
		}
		if(fullX == 4)
		{
			return result = "X won";
		}
		if(fullO == 4)
		{
			return result = "O won";

		}
	}


	int fullX = 0;
	int fullO = 0;
	for( int j = 0; j < 4; ++j)
	{
		if( (int)(v[ j * 4 + j ] - x) == 0 || (int)(v[ j * 4 + j ] - x) == -4)
		{
			++fullX;
		} 

		if( (int)(v[ j * 4 + j ] - o) == 0 || (int)(v[ j * 4 + j ] - o) == 5)
		{
			++fullO;
		} 
	}
	if(fullX == 4)
	{
		return result = "X won";
		win = true;
	}
	if(fullO == 4)
	{
		return result = "O won";
		win = true;
	}

	fullX = 0;
	fullO = 0;

	for( int j = 0; j < 4; ++j)
	{

		if( (int)(v[ (4 - j - 1) * 4 + j ] - x) == 0 || (int)(v[ (4 - j - 1 ) * 4 + j ] - x) == -4)
		{
			++fullX;
		} 

		if( (int)(v[ (4 - j - 1) * 4 + j ] - o) == 0 || (int)(v[ (4 - j - 1) * 4 + j ] - o) == 5)
		{
			++fullO;
		} 
	}
	if(fullX == 4)
	{
		return result = "X won";
		win = true;
	}
	if(fullO == 4)
	{
		return result = "O won";
	}


	if(notComplete)
	{
		return result = "Game has not completed";
	}
	else
	{
		return result = "Draw";
	}
	//return result;
}


int process(const std::string& sFileIn, const std::string& sFileOut)
{
	FILE* fout = NULL; FOPEN(fout, sFileOut.c_str(), "w");
	std::ifstream file(sFileIn.c_str());
	std::string s;
	int T = 0;
	file >> T;
	std::vector<char> raw;
	for(int i = 0; i < T; ++i)
	{
		notComplete = false;
		char symb;
		for(int j = 0; j < 16; ++j)
		{
			file >> symb;
			if(symb == '.')
			{
				notComplete = true;
			}
			raw.push_back(symb);
		}
		std::string res = problem(raw);
		fprintf(fout, "Case #%d: %s\n", i+1, res.c_str());
		raw.clear();

	}
	file.close();
	fclose(fout);
	return 0;
}

int main(int argc, char* argv[])
{
	const time_t t1 = clock();
	const int nTestType = argc > 1 ? atoi(argv[1]) : nDefaultTestType;

	const std::string sFileIn0 = "A-large.in";
	const std::string sFileOut0 = "A-large.out";

	const std::string sFileIn1 = FILE_PREFIX "-small-attempt.in";
	const std::string sFileOut1 = FILE_PREFIX "-small-attempt.out";
	const std::string sFileIn2 = FILE_PREFIX "-large-attempt..in";
	const std::string sFileOut2 = FILE_PREFIX "-large-attempt..out";

		int res = 0;
	try
	{
		switch(nTestType)
		{
		case 0:
			res = process(sFileIn0, sFileOut0);
			break;
		case 1:
			res = process(sFileIn1, sFileOut1);
			break;
		case 2:
			res = process(sFileIn2, sFileOut2);
			break;
		default:
			printf("ERROR! Unknown test data index!\n");
			res = 1;
		}
	}
	catch (std::exception &e)
	{
		printf("ERROR! Unhandled std exception: %s: %s!\n", typeid(e).name(), e.what());
	}

	const time_t t2 = clock();
	system("pause");
	return 0;
}