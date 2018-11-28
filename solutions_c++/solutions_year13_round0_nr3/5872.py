#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <time.h>
#include <conio.h>
#include <errno.h>
#include <stdarg.h>
#include <sstream>

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


bool isPalindrom(int i)
{
	std::string s;
	std::stringstream out;
	out << i;
	s = out.str();
	int n = s.length();
	for(int i = 0; i < std::floor((float)(n/2)); ++i)
	{
		if(s[i] != s[n-i-1]) return false;
	}
	return true;
}

bool isSquare(int i)
{
	float sq = std::sqrt((float)i);
	float n;
	float frac = std::modf(sq, &n);
	if(frac==0.0)	return true;
	return false;
}

int problem(int A, int B)
{
	int res = 0;
	std::string result;
	float a = std::sqrt((float)A);
	float b = std::sqrt((float)B);
	std::cout<< " a= " << static_cast<int>(std::floor(a))<< " b= " << static_cast<int>(std::floor(b)) << std::endl;
	for(int i = static_cast<int>(std::ceil(a)), fl = static_cast<int>(std::floor(b)); i <= fl; ++i)
	{
		std::cout << " numb = "<<  i << std::endl;
		if(isPalindrom(i) && isPalindrom(i*i) && isSquare(i*i))
		{
			std::cout << " sqandfair = "<<  i*i << std::endl;
			++res;
		}

	}
	return res;
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
		int A;
		file >> A;
		int B;
		file >> B;
		int res = problem(A, B);
		fprintf(fout, "Case #%d: %d\n", i+1, res);
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

	const std::string sFileIn0 = "C-small-attempt0.in";
	const std::string sFileOut0 = "C-small-attempt0.out";

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