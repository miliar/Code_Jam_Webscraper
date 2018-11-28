// GCJ.cpp : Defines the entry point for the console application.
//
#include <cstdio>
#include <iostream>
#include <vector>
#include <list>
#include <map>
#include <string>
#include <math.h>
#include <functional>

//#define verbose

using namespace std;

int main()
{
	// First let's read the file
	freopen("gcj.in", "r", stdin);
	freopen("gcj.out", "w", stdout);

	int i, j, k, Ncases;
	//list <short> nonEmptyPlates;

	cin >> Ncases;

	// Test cases
	for (i=0; i<Ncases; i++)
	{
		bool RichWins = false;
		short xomino, rows, cols;
		cin >> xomino >> rows >> cols;

		short cells = rows * cols;
		// Ok so we have the data in, now what is the algorithm to solve the problem
		// 1=1 2=1 3=2 4=5
		//	1	2	3	4	4	6	8	9	12	16
		// 1x1 1x2 1x3 1x4 2x2 2x3 2x4 3x3 3x4 4x4
		//1	G	G	G	G	G	G	G	G	G	G
		//2	R	G	R	G	G	G	G	R	G	G
		//3	R	R	R	R	R	G	R	G	G	R
		//4	R	R	R	R	R	R	R	R	G	G

		switch (xomino)
		{
		case 1:
			break;
		case 2:
			switch (cells)
			{
			case 1:
			case 3:
			case 9:
				RichWins = true;
				break;
			}
			break;
		case 3:
			switch (cells)
			{
			case 6:
			case 9:
			case 12:
				break;
			default:
				RichWins = true;
			}
			break;
		case 4:
			switch (cells)
			{
			case 12:
			case 16:
				break;
			default:
				RichWins = true;
			}
			break;
		}
		if (RichWins)
			cout << "Case #" << i + 1 << ": " << "RICHARD" << endl;
		else
			cout << "Case #" << i + 1 << ": " << "GABRIEL" << endl;
	}

	return 0;
}

