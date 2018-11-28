// problemA.cpp : 定义控制台应用程序的入口点。
//

#include "stdafx.h"
#include <iostream>
#include <vector>
#include <fstream>
using namespace std;

int _tmain(int argc, _TCHAR* argv[])
{
	typedef  vector<vector<int> > Matrix;
	ifstream infile("A-small-attempt1.in");
	ofstream outfile("A-small-attempt1.out");

	int caseNum;
	infile >> caseNum;

	for(int c = 0; c < caseNum; ++c){
		int row1, row2;
		int m1[4][4];
		int m2[4][4];

		infile >> row1;

		for(int i = 0; i < 4; ++i){
			for(int j = 0; j < 4; ++j){
				infile >> m1[i][j];
			}
		}

		infile >> row2;
		for(int i = 0; i < 4; ++i){
			for(int j = 0; j < 4; ++j){
				infile >> m2[i][j];
			}
		}

		vector<int> matchNumber;
		vector<bool> dmap(16, false);
		for(int i = 0; i < 4; ++i){
			dmap[ m1[row1-1][i] - 1 ] = 1;
		}

		for(int i = 0; i < 4; ++i){
			if( dmap[ m2[row2-1][i]-1 ] == 1){
				matchNumber.push_back(m2[row2-1][i]);
			}
		}

		//output result
		outfile << "Case #" << c + 1<< ": ";

		if(matchNumber.size() == 0){
			outfile << "Volunteer cheated!\n";
		}else if(matchNumber.size() > 1){
			outfile << "Bad magician!\n";
		}else{
			outfile << matchNumber[0] << endl;;
		}

	}

	return 0;
}

