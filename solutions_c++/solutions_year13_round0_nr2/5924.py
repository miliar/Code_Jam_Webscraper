//============================================================================
// Name        : round0.cpp
// Author      : rodrijuana
// Date	(D/M/Y): 12/04/2013
//============================================================================
#include <fstream>
#include <string>
#include <math.h>
//#include <iostream>

using namespace std;

int main() {
	
ifstream input("inputB-small.txt");
ofstream output("output2a.txt");

int cnt, CNT, c_i, c_j, C_I, C_J;
int Lin[100][100];
int Lout[100][100];
int iaux, jaux;

input >> CNT;

for (cnt = 1; cnt <= CNT; cnt++)
{   //get case 
	input >> C_I >> C_J;
	for (c_i = 1; c_i <= C_I; c_i++)
		for (c_j = 1; c_j <= C_J; c_j++) {
			input >> Lin[c_i][c_j];
			Lout [c_i][c_j] = 0;
		}
	
	
	bool ispos = false;
	bool done = false;
	
	while (!done) {
		int max = 0;
		//find max
		for (c_j = 1; c_j <= C_J; c_j++)
			for (c_i = 1; c_i <= C_I; c_i++)
				if (Lin[c_i][c_j] > max) {
					max = Lin[c_i][c_j];
					iaux = c_i;
					jaux = c_j;
				}
		
		if (max == 0){
			ispos = true;
			done = true;
		}
		else {
			Lin[iaux][jaux] = 0;
			Lout[iaux][jaux] = max;
			
			bool okx = true;
			bool oky = true;
			
			for (c_i = 1; c_i <= C_I; c_i++)
				if (Lout[c_i][jaux] > max) {
					okx = false;
				}		
			
			for (c_j = 1; c_j <= C_J; c_j++)
				if (Lout[iaux][c_j] > max) {
					oky = false;
				}		
			
			if (!(okx || oky))
				done = true;	
		}			
	} //while
	if (ispos)
		output << "Case #" << cnt << ": YES" << '\n';
	else
		output << "Case #" << cnt << ": NO" << '\n';

}

}
