/*GOOGLE CODE JAM
 *ANDREW WILKENING
 *APRIL 11, 2014
 *PROBLEM A - MAGIC TRICK
 */

#include<fstream>
#include<iostream>
#include<iomanip>
#include<algorithm>
#include<vector>

using namespace std;

int main()
{
	ifstream fin("SmallA0.in");
	ofstream fout("SmallASol.out");
	int runs, row, matches, matchNum;
	int temp;
	int cards[4][4];
	int firstRow[4];
	fin >> runs;
	for(int i = 1; i <= runs; i++)
	{
		matches = 0;
		fin >> row;
		for(int j = 0; j < 4; j++){
			for(int k = 0; k < 4; k++){
				fin >> cards[k][j];
				if(row == j+1){
					firstRow[k] = cards[k][j];
				}
			}
		}
		fin >> row;
		for(int j = 0; j < 4; j++){
			for(int k = 0; k < 4; k++){
				fin >> cards[k][j];
				if(row == j+1){
					for(int l = 0; l < 4; l++){
						if(cards[k][j] == firstRow[l]){
							matches++;
							matchNum = cards[k][j];
						}
					}
				}
			}
		}
		
		fout << "Case #" << i << ": ";
		if(matches == 0) fout << "Volunteer cheated!" << endl;
		else if(matches == 1) fout << matchNum << endl;
		else fout << "Bad magician!" << endl;
	}
	return 0;
}
