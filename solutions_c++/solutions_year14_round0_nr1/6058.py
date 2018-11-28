// GCodeJam_MagicTrick.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"

#include <fstream>
#include <iostream>
#include <stdio.h>
#include <map>
#include <vector>

using namespace std;


int _tmain(int argc, _TCHAR* argv[])
{
	FILE *fp;
	fopen_s(&fp, "some.txt", "r");
	ofstream outf;
	outf.open("result.txt");

	if(fp && outf.is_open()) {
		int N;
		fscanf_s(fp, "%d", &N);

		for(int i = 0 ; i < N ; i++) {

			map<int, int> res;
			map<int, int> res2;

			int nrow;
			fscanf_s(fp, "%d", &nrow);

			int rows[4][4];
			for(int j = 0 ; j < 4 ; j++) {
				fscanf_s(fp, "%d %d %d %d", &rows[j][0], &rows[j][1], &rows[j][2], &rows[j][3] );
			}

			for(int j = 0 ; j < 4 ; j++)
			{
				res[ rows[nrow-1][j] ] = rows[nrow-1][j];
			}

			fscanf_s(fp, "%d", &nrow);
			for(int j = 0 ; j < 4 ; j++) {
				fscanf_s(fp, "%d %d %d %d", &rows[j][0], &rows[j][1], &rows[j][2], &rows[j][3] );
			}

			int matched = 0;
			int matchedVal = -1;
			
			for(int j = 0 ; j < 4 ; j++) {
				//remove from map.

				int valueToRemove = rows[nrow-1][j];

				if(res.find(valueToRemove) != res.end()) {
					matched ++;
					matchedVal = valueToRemove;
				}
				else {
				}

			}

			if(matched == 1) {
				// normal.
				outf << "Case #" << i + 1 << ": " << matchedVal << endl;
			}
			else if(matched > 1) {
				// bad magician.
				outf << "Case #" << i + 1 << ": " << "Bad magician!" << endl;
			}
			else {
				// volunteer cheated.
				outf << "Case #" << i + 1 << ": " << "Volunteer cheated!" << endl;
			}

		}



	}


	return 0;
}

