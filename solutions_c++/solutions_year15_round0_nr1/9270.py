#include <windows.h>
#include <tchar.h>
#include <stdio.h>
#include <conio.h>
#include <map>
#include <list>
#include <vector>
#include <fstream>
#include <algorithm>
#include <string>

#define DIE(format, ...) do{ wprintf(L"DIE: "format, ##__VA_ARGS__); DebugBreak(); }while(0);

unsigned shyMax;
std::vector<unsigned> shyCnt;
std::wstring shyStr;

std::wstring TrimLeft(const std::wstring & str, const std::wstring & space)
{
	std::wstring::size_type pos;
	pos = str.find_first_not_of(space);
	if(std::wstring::npos == pos)
	{
		pos = str.size();
	}
	return str.substr(pos);
}

std::wstring TrimRight(const std::wstring & str, const std::wstring & space)
{
	std::wstring::size_type pos;
	pos = str.find_last_not_of(space);
	if(std::wstring::npos == pos)
	{
		pos = 0;
	}
	else
	{
		pos++;
	}
	return str.substr(0, pos);
}
std::wstring Trim(const std::wstring & str, const std::wstring & space)
{
	return TrimLeft(TrimRight(str, space), space);
}

void read_task(std::wfstream & input, std::wfstream & output)
{
	unsigned i;
	input >> shyMax;
	std::getline(input, shyStr);
	shyStr = Trim(shyStr, L" \t\n\r");
	if(shyStr.length() != shyMax + 1)
	{
		DIE(L"invalid 1");
	}
	shyCnt.resize(shyMax + 1);
	for(i = 0; i <= shyMax; i++)
	{
		shyCnt[i] = shyStr[i] - '0';
	}
}

void solve_task(std::wfstream & input, std::wfstream & output)
{
	unsigned cTotal, cAdd, i;
	cAdd = 0;
	cTotal = shyCnt[0];
	for(i = 1; i <= shyMax; i++)
	{
		if(shyCnt[i] > 0)
		{
			if(cTotal + cAdd < i)
			{
				cAdd = i - cTotal;
			}
			cTotal += shyCnt[i];
		}
	}
	output << cAdd;
}

int _tmain(int argc, _TCHAR* argv[])
{
	unsigned cTask, iTask;
	std::wfstream input, output;
	input.open(L"task.in"   , std::ios_base::in);
	output.open(L"task.out" , std::ios_base::out);

	input >> cTask;
	for(iTask = 0; iTask < cTask; iTask++)
	{
		read_task(input, output);
		output << L"Case #" << iTask + 1 << L": ";
		solve_task(input, output);
		output << std::endl;
	}

	input.close();
	output.close();
	wprintf(L"DONE\n");
	getch();
	return 0;
}

