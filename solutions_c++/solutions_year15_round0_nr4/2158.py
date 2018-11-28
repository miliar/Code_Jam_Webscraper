/*
 * sample.cpp
 *
 *  Created on: Apr 11, 2015
 *      Author: ttcn
 */

#include <stdio.h>
#include <iostream>
#include <fstream>
#include <vector>
#include <stdlib.h>
#include <algorithm>
#include <sstream>

using namespace std;

int main()
{
	fstream infile,outfile;
	infile.open("D-small-attempt2.in", ios::in );
	outfile.open("D-small-attempt2.out", ios::out | ios::trunc );

	int numOfinputs = 0;

	infile>>numOfinputs;
    cout<<"numOfinputs:" << numOfinputs << endl;

    // table for winning
    int oneOnino[][4]={ {1,1,1,1},{1,1,1,1},{1,1,1,1},{1,1,1,1}};
    int twoOnino[][4]={ {0,1,0,1},{1,1,1,1},{0,1,0,1},{1,1,1,1}};
    int threeOnino[][4]={ {0,0,0,0},{0,0,1,0},{0,1,1,1},{0,0,1,0}};
    int fourOnino[][4]={ {0,0,0,0},{0,0,0,0},{0,0,0,1},{0,0,1,1}};


	for(int i=0; i<numOfinputs; i++)
	{
		int X,R,C;

		infile >> X;
		infile >> R;
		infile >> C;

		bool oIsWinning = false;

		if(X <=4 && R <=4 && C <=4)
		{
			switch(X)
			{
				case 1:
					oIsWinning = oneOnino[R-1][C-1];
					break;
				case 2:
					oIsWinning = twoOnino[R-1][C-1];
					break;
				case 3:
					oIsWinning = threeOnino[R-1][C-1];
					break;
				case 4:
					oIsWinning = fourOnino[R-1][C-1];
					break;
				default:
					break;
			}
		}
		outfile << "Case #" << i+1 << ": ";

		if(oIsWinning)
			outfile<<"GABRIEL"<<endl;
		else
			outfile<<"RICHARD"<<endl;
	}

	return 1;
}


