// Code Jam 2013 - Problem B - Lawnmower
// Michael "Klairic" Dolle

#include "stdafx.h"
#include <string>


#define FILENAME_PROBLEM		"E:\\Programming\\Code Jam\\2013\\Round 1\\Problem B - Lawnmower\\B-large.in"
#define FILENAME_OUTPUT			"E:\\Programming\\Code Jam\\2013\\Round 1\\Problem B - Lawnmower\\B-large.out"

#define MAX_BUFFER				250000
#define MAX_LINE				4000
#define MAX_NUMBERS				200



// This is in all solutions, but is problem dependant
void ProcessInput(std::string &FinalOutput, int Index);




// Generic stuff for all code jam
char _Input[MAX_BUFFER + 1];
char _CurrentLine[MAX_LINE + 1];
int _CurrentNumbers[MAX_NUMBERS + 1];

int _InputPlace;
int _InputSize;
int _InputCount;

int _LineSize;
int _LineNumbersSize;

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
	_InputCount = _CurrentNumbers[0];
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
	_LineSize = count;


	int linePlace(0);
	_LineNumbersSize = 0;
	do
	{
		_CurrentNumbers[_LineNumbersSize] = atoi(&_CurrentLine[linePlace]);
		output = strstr(&_CurrentLine[linePlace], " ");
		if (output)
			linePlace = output - _CurrentLine + 1;

		_LineNumbersSize++;
	} while (output);

	
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

int *_Grid;
int _Width;
int _Height;
void CreateGrid()
{
	_Grid = new int[_Width * _Height];
}
void DestroyGrid()
{
	delete []_Grid;
}
int & GetAt(int X, int Y)
{
	return _Grid[(Y * _Width) + X];
}









// Specific to this problem
bool VerifyPoint(int X, int Y)
{
	// Go up/down
	int point = GetAt(X, Y);

	bool ok(true);
	for (int i = 0; i < _Height; i++)
	{
		if (GetAt(X, i) > point)
		{
			ok = false;
			break;
		}
	}
	if (ok)
		return true;

	// Go left/right
	ok = true;
	for (int i = 0; i < _Width; i++)
	{
		if (GetAt(i, Y) > point)
		{
			ok = false;
			break;
		}
	}

	return ok;
}
void ProcessInput(std::string &FinalOutput, int Index)
{
	GetNextLine();
	_Width = _CurrentNumbers[1];
	_Height = _CurrentNumbers[0];
	CreateGrid();

	for (int i = 0; i < _Height; i++)
	{
		GetNextLine();
		for (int j = 0; j < _Width; ++j)
		{
			GetAt(j, i) = _CurrentNumbers[j];
		}
	}


	bool ok(true);
	for (int i = 0; i < _Width; ++i)
	{
		for (int j = 0; j < _Height; ++j)
		{
			if (!VerifyPoint(i, j))
			{
				ok = false;
				break;
			}
		}
		if (!ok)
			break;
	}

	DestroyGrid();

	AppendCaseOutput(FinalOutput, Index, ok ? "YES" : "NO");
}
