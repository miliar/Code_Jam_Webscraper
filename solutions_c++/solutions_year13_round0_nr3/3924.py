// Code Jam 2013 - Problem C - Fair and Square
// Michael "Klairic" Dolle

#include "stdafx.h"
#include <string>


#define FILENAME_PROBLEM		"E:\\Programming\\Code Jam\\2013\\Round 1\\Problem C - Fair and Square\\C-small-attempt0.in"
#define FILENAME_OUTPUT			"E:\\Programming\\Code Jam\\2013\\Round 1\\Problem C - Fair and Square\\C-small-attempt0.out"

#define MAX_BUFFER				250000
#define MAX_LINE				1000



//////////////////////////////////////////////////////////////////////
//////															//////
//////	This is in all solutions, but is problem dependant		//////
//////															//////
//////////////////////////////////////////////////////////////////////
void ProcessInput(std::string &FinalOutput, int Index);




//////////////////////////////////////////////////////////////////////
//////															//////
//////			Generic stuff for all code jam					//////
//////															//////
//////////////////////////////////////////////////////////////////////
char _Input[MAX_BUFFER + 1];
char _CurrentLine[MAX_LINE + 1];

int _InputPlace;
int _InputSize;
int _InputCount;

void LoadInputFile(const char *Filename);
const char * GetNextLine();

void LoadInputFile(const char *Filename)
{
	FILE *file(nullptr);
	fopen_s(&file, Filename, "rb");
	if (file)
	{
		_InputSize = fread_s(_Input, 250000, 1, 250000, file);
		_Input[_InputSize] = 0;
		fclose(file);
	}

	const char *inputCount = GetNextLine();
	_InputCount = atoi(inputCount);
}
const char * GetNextLine()
{
	const char *output = strstr(&_Input[_InputPlace], "\r\n");
	int advance(0);
	if (output)
	{
		advance = 2;
	}
	else
	{
		output = strstr(&_Input[_InputPlace], "\n");
		advance = 1;
	}
	int count = output - _Input - _InputPlace;
	strncpy_s(_CurrentLine, 1000, &_Input[_InputPlace], count);
	_InputPlace = output - _Input + advance;

	return _CurrentLine;
}
void AppendCaseOutput(std::string &Output, int CaseNumber, const char *ResultDescription)
{
	char buffer[10];
	Output += "Case #";
	Output += _itoa(CaseNumber + 1, buffer, 10);
	Output += ": ";
	Output += ResultDescription;
	Output += "\r\n";
}
void SaveOutputFile(const char *Filename, const std::string &Output)
{
	FILE *file(nullptr);
	fopen_s(&file, Filename, "w+b");
	if (file)
	{
		fwrite(Output.c_str(), 1, Output.size(), file);
		fclose(file);
	}
}
int _tmain(int argc, _TCHAR* argv[])
{
	std::string finalOutput;

	LoadInputFile(FILENAME_PROBLEM);
	for (int i = 0; i < _InputCount; i++)
	{
		ProcessInput(finalOutput, i);
	}
	SaveOutputFile(FILENAME_OUTPUT, finalOutput);

	return 0;
}








//////////////////////////////////////////////////////////////////////
//////															//////
//////		Specific to this problem							//////
//////															//////
//////////////////////////////////////////////////////////////////////
__int64 FindNumbers(__int64 Start, __int64 End);

void ProcessInput(std::string &FinalOutput, int Index)
{
	const char *numbers = GetNextLine();
	__int64 start = _atoi64(numbers);
	const char *numbers2 = strstr(numbers, " ");
	__int64 end = _atoi64(numbers2);

	__int64 count = FindNumbers(start, end);

	char buffer[30];
	_i64toa(count, buffer, 10);

	AppendCaseOutput(FinalOutput, Index, buffer);
}

bool IsPalindrome(__int64 TestNumber)
{
	char buffer[40];
	_i64toa(TestNumber, buffer, 10);

	bool ok(true);

	int length = strlen(buffer);
	for (int i = 0; i < length / 2; i++)
	{
		if (buffer[i] != buffer[length - 1 - i])
		{
			ok = false;
			break;
		}
	}

	return ok;
}

__int64 FindNumbers(__int64 Start, __int64 End)
{
	long double sqStart(Start);
	sqStart = sqrt(sqStart);
	__int64 ceilStart = ceil(sqStart);

	long double sqEnd(End);
	sqEnd = sqrt(sqEnd);
	__int64 floorEnd = floor(sqEnd);

	int fairAndSquareCount(0);

	for (__int64 i = ceilStart; i <= floorEnd; ++i)
	{
		if (IsPalindrome(i))
		{
			__int64 test = i * i;
			if (IsPalindrome(test))
				++fairAndSquareCount;
		}
	}
	return fairAndSquareCount;
}
