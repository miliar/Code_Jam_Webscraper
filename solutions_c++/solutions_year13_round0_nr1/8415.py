// test.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <sstream>
#include <fstream>
#include <iostream>

using namespace std;

typedef char layout_t[4][4];
typedef int repr_t[4][4];

typedef enum {N, X, O, D} res_t;

res_t determine(layout_t *layout)
{
	int i, j;
	repr_t reprs[2];
	bool t;
	bool determined;
	bool blank;
	int sum;
	res_t res;
	
	blank = false;
	for (i = 0; i < 4; i ++)
	{
		for (j = 0; j < 4; j ++)
		{
			switch((*layout)[i][j])
			{
			case 'X':
				reprs[0][i][j] = -1;
				reprs[1][i][j] = -1;
				break;
			case 'O':
				reprs[0][i][j] = 1;
				reprs[1][i][j] = 1;
				break;
			case 'T':
				reprs[0][i][j] = -1;
				reprs[1][i][j] = 1;
				t = true;
				break;
			case '.':
				reprs[0][i][j] = 0;
				reprs[0][i][j] = 0;
				blank = true;
				break;
			}
		}
	}

	///calculate row
	for (i = 0; i < 4; i ++)
	{
		for (determined = false, sum = 0, j = 0; j < 4; j ++)
		{
			sum += reprs[0][i][j];
		}
		if (sum == -4)
		{
			res = X;
			goto finished;
		}
		else if (sum == 4)
		{
			res = O;
			goto finished;
		}
		if (t)
		{    
			for (determined = false, sum = 0, j = 0; j < 4; j ++)
			{
				sum += reprs[1][i][j];
			}

			if (sum == -4)
			{
				res = X;
				goto finished;
			}
			else if (sum == 4)
			{
				res = O;
				goto finished;
			}
		}
	}

	/// calculate colume
	for (j = 0; j < 4; j ++)
	{
		for (determined = false, sum = 0, i = 0; i < 4; i ++)
		{
			sum += reprs[0][i][j];
		}
		if (sum == -4)
		{
			res = X;
			goto finished;
		}
		else if (sum == 4)
		{
			res = O;
			goto finished;
		}
		if (t)
		{    
			for (determined = false, sum = 0, j = 0; j < 4; j ++)
			{
				sum += reprs[1][i][j];
			}

			if (sum == -4)
			{
				res = X;
				goto finished;
			}
			else if (sum == 4)
			{
				res = O;
				goto finished;
			}
		}
	}

	/// calculate diagonal 
	sum = 0;
	sum = reprs[0][0][0] + reprs[0][1][1] + reprs[0][2][2] + reprs[0][3][3];
	if (sum == -4)
	{
		res = X;
		goto finished;
	}		
	else if (sum == 4)	
	{
		res = O;
		goto finished;
	}
	if (t)
	{ 
		sum = 0;	
		sum = reprs[1][0][0] + reprs[1][1][1] + reprs[1][2][2] + reprs[1][3][3];
		if (sum == -4)
		{
			res = X;
			goto finished;
		}		
		else if (sum == 4)	
		{
			res = O;
			goto finished;
		}
	}

	/// calculate reverse diagonal 
	sum = 0;
	sum = reprs[0][0][3] + reprs[0][1][2] + reprs[0][2][1] + reprs[0][3][0];
	if (sum == -4)
	{
		res = X;
		goto finished;
	}		
	else if (sum == 4)	
	{
		res = O;
		goto finished;
	}
	if (t)
	{ 
		sum = 0;	
		sum = reprs[1][0][3] + reprs[1][1][2] + reprs[1][2][1] + reprs[1][3][0];
		if (sum == -4)
		{
			res = X;
			goto finished;
		}		
		else if (sum == 4)	
		{
			res = O;
			goto finished;
		}
	}

	/// still un-determined?
	if (blank)
		res = N;
	else
		res = D;

finished:
	return res;
}

int main(int argc, char* argv[])
{
	int i, c;
	layout_t *layouts;

	ifstream from(argv[1]);
	if (!from)
	{
		cout << "error open input file" << endl;
		return -1;
	}
	ofstream to(argv[2]);

	if (!to)
	{
		cout << "error open input file" << endl;
		return -1;
	}

	string input;

	getline(from, input);
	c = atoi(input.c_str());
	
	layouts = new layout_t[c];
	
	i = 0;
	while(getline(from, input))
	{
		if (input.length() == 0)
			continue;
		layouts[i][0][0] = input[0];
		layouts[i][0][1] = input[1];
		layouts[i][0][2] = input[2];
		layouts[i][0][3] = input[3];
		getline(from, input);
		layouts[i][1][0] = input[0];
		layouts[i][1][1] = input[1];
		layouts[i][1][2] = input[2];
		layouts[i][1][3] = input[3];
		getline(from, input);
		layouts[i][2][0] = input[0];
		layouts[i][2][1] = input[1];
		layouts[i][2][2] = input[2];
		layouts[i][2][3] = input[3];
		getline(from, input);
		layouts[i][3][0] = input[0];
		layouts[i][3][1] = input[1];
		layouts[i][3][2] = input[2];
		layouts[i][3][3] = input[3];

		i ++;
	}


	for (i = 0; i < c; i ++)
	{
		res_t res;
		res = determine(&layouts[i]);
	
		switch (res)
		{
		case N:
			to << "Case #" << i + 1 << ": Game has not completed" << endl;
			break;
		case X:
			to << "Case #" << i + 1<< ": X won" << endl;
			break;
		case O:
			to << "Case #" << i + 1<< ": O won" << endl;
			break;
		case D:
			to << "Case #" << i + 1<< ": Draw" << endl;
			break;
		}
	}

	delete[] layouts;
	return 0;
}

