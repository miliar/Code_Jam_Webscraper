#include <iostream>
#include <algorithm>
#include <string>
#include <set>
#include <vector>
#include <queue>
#include <fstream>
#include <sstream>
#include <map>
#include <list>
#include <cmath>
#include <bitset>
#include <stack>
#include <stdio.h>
#include <cstring>
#include <ctime>
#include <ctype.h>
#include <utility>
#include <stdlib.h>
#include <stdio.h>
#include <cstdio>
using namespace std;
 
#define mod 1000000007
#define ll long long
#define INF 1000000000
#define PI 3.1415926

string lent[4];

int main (void)
{

    ifstream cin("A-large.in");
	ofstream cout("out.txt");
    int t;
	cin >> t;
	
	for (int i = 0; i < t; i++)
	{
		bool xwin = false, owin = false;
		int xscore = 0, oscore = 0;

		for (int j = 0; j < 4; j++)
		{
			cin >> lent[j];
			for (int k = 0; k < 4; k++)
				xscore += (lent[j][k] == 'X' || lent[j][k] == 'T');
			if (xscore == 4)
				xwin = true;
			xscore = 0;

			for (int k = 0; k < 4; k++)
				oscore += (lent[j][k] == 'O' || lent[j][k] == 'T');
			if (oscore == 4)
				owin = true;
			oscore = 0;
		}

		for (int j = 0; j < 4; j++)
		{
			for (int k = 0; k < 4; k++)
				xscore += (lent[k][j] == 'X' || lent[k][j] == 'T');

			if (xscore == 4)
				xwin = true;
			xscore = 0;

			for (int k = 0; k < 4; k++)
				oscore += (lent[k][j] == 'O' || lent[k][j] == 'T');

			if (oscore == 4)
				owin = true;
			oscore = 0;
		}

		for (int j = 0; j < 4; j++)
		{
			xscore += (lent[j][j] == 'X' || lent[j][j] == 'T');
			oscore += (lent[j][j] == 'O' || lent[j][j] == 'T');
		}

		if (xscore == 4)
			xwin = true;
		xscore = 0;

		if (oscore == 4)
			owin = true;
		oscore = 0;

		for (int j = 0; j < 4; j++)
		{
			xscore += (lent[j][3-j] == 'X' || lent[j][3-j] == 'T');
			oscore += (lent[j][3-j] == 'O' || lent[j][3-j] == 'T');
		}

		if (xscore == 4)
			xwin = true;
		xscore = 0;

		if (oscore == 4)
			owin = true;
		oscore = 0;
		
		bool done = true;
		for (int j = 0; j < 4; j++)
		{
			for (int k = 0; k < 4; k++)
			{
				if (lent[j][k] == '.')
					done = false;
			}
		}

		cout << "Case #" << i+1 << ": ";
		if (xwin)
			cout << "X won" << endl;
		else if (owin)
			cout << "O won" << endl;
		else if (done)
			cout << "Draw" << endl;
		else
			cout << "Game has not completed" << endl;
	}

}