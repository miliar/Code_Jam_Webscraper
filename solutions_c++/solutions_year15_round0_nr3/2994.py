
#include <stdio.h>
#include <stdlib.h>
#include <sstream>
#include <iostream>
#include <fstream>
#include <vector>
#include <list>
#include <algorithm>

using namespace std;


char multiply(char c1, char c2, bool &minus)
{
	switch (c1)
	{
	case '1':
		switch (c2)
		{
		case '1': return '1';
		case 'i': return 'i';
		case 'j': return 'j';
		case 'k': return 'k';
		}

	case 'i':
		switch (c2)
		{
		case '1': return 'i';
		case 'i': minus = !minus;  return '1';
		case 'j': return 'k';
		case 'k': minus = !minus;  return 'j';
		}

	case 'j':
		switch (c2)
		{
		case '1': return 'j';
		case 'i': minus = !minus;  return 'k';
		case 'j': minus = !minus;  return '1';
		case 'k': return 'i';
		}

	case 'k':
		switch (c2)
		{
		case '1': return 'k';
		case 'i': return 'j';
		case 'j': minus = !minus;  return 'i';
		case 'k': minus = !minus;  return '1';
		}
	}
}

bool getSymbol(char* str, char c, int offset)
{
	if (str[offset] == 0)
		return false;

	bool minus = false;
	char sum = '1';
	while (str[offset] != 0)
	{
		sum = multiply(sum, str[offset], minus);

		if (sum == c)
		{
			if (c == 'i')
			{
				if (getSymbol(str, 'j', offset + 1))
					return true;
			}
			if (c == 'j')
			{
				if (getSymbol(str, 'k', offset + 1))
					return true;
			}
		}
		offset++;
	}

	if (sum == 'k')
		return true;
		
	return false;
}

bool canSplit(int L, int X, char* str)
{
	if (L*X < 3)
		return false;

	char sum = str[0];
	int offset = 1;
	bool minus = false;

	while (str[offset] != 0)
	{
		sum = multiply(sum, str[offset], minus);
		offset++;
	}

	if (sum != '1' || !minus)
		return false;

	if ( !getSymbol(str, 'i', 0) )
		return false;

	return true;
}

int main()
{
	FILE *in;
	if (fopen_s(&in, "C-small-attempt0.in", "r+") != 0)
		printf("The in file was not opened\n");

	fstream out("C-small-attempt0.out", ios::out);
	if (out.bad())
		printf("The out file was not opened\n");

	int T;
	fscanf_s(in, "%d", &T);

	for (int tc = 1; tc <= T; tc++)
	{
		int L, X;
		fscanf_s(in, "%d %d", &L, &X);
		char* str = new char[L*X+1];
		memset(str, 0, L*X + 1);
		fscanf_s(in, "%s", str, L+1);

		for (int i = 1; i < X; i++)
			memcpy(str + L*i, str, L);

		char* answer;
		if (canSplit(L, X, str))
			answer = "YES";
		else
			answer = "NO";

		delete[] str;
		cout << "Case #" << tc << ": " << answer << endl;
		out << "Case #" << tc << ": " << answer << endl;
	}

	_ASSERT(canSplit(2, 1, "sdf") == false);
	cout << "Unit tests of canSplit() are OK" << endl;

	out.close();
	getchar();
}