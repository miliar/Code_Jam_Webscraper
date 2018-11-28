// codejam.cpp : 定义控制台应用程序的入口点。
//

#include "stdafx.h"

#include <cstdio>
#include <iostream>
#include <fstream>

#define INPUTFILE "A-small-attempt1.in"
#define OUTPUTFILE "result.txt"


using namespace std;

//#pragma warning(disable:4996)


int main()
{
	fstream infile(INPUTFILE,ios::in);
	fstream outfile(OUTPUTFILE,ios::out);
	int caseN,i,j,temp,row,count;
	bool mark[17];
	int result, resultNum;
	infile >> caseN;
	count = 1;
	while (count<=caseN)
	{
		resultNum = 0;
		memset(mark, false, sizeof(bool)* 17);
		infile >> row;
		for (i = 1; i <= 4; i++){
			for (j = 1; j <= 4; j++){
				infile >> temp;
				if (i == row){
					mark[temp] = true;
				}
			}
		}
		infile >> row;
		for (i = 1; i <= 4; i++){
			for (j = 1; j <= 4; j++){
				infile >> temp;
				if (i == row && mark[temp]){
					result = temp;
					resultNum++;
				}
			}
		}
		if (resultNum >= 2 ){
			outfile << "Case #" << count++ << ": Bad magician!\n";
		}
		else if (resultNum == 1){
			outfile << "Case #" << count++ << ": " << result << endl;
		}
		else{
			outfile << "Case #" << count++ << ": Volunteer cheated!\n";
		}
	}
	infile.close();
	outfile.close();
	return 0;
}

