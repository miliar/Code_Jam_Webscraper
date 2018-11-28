/*************************************************************************
    > File Name: A.cpp
    > Author: csy
    > Mail: chshaoyi7@gmail.com 
    > Created Time: 2014年04月12日 星期六 13时44分03秒
 ************************************************************************/

#include<iostream>

using namespace std;

#include <fstream>

int first[4][4], second[4][4];
int row1, row2;

int main(){
	
	ifstream fin("A-small-attempt0.in");
	ofstream fout("SmallA.out");

	int t;
	
	fin >> t;

	for(int i = 1; i <= t; i ++){
		fin >> row1;
		for(int j = 0; j < 4; j ++){
			for(int k = 0; k < 4; k ++)
				fin >> first[j][k];
		}

		fin >> row2;
		for(int j = 0; j < 4; j ++){
			for(int k = 0; k < 4; k ++)
				fin >> second[j][k];
		}

		row1 --; row2 --;
		
		int counter = 0, number = 0;

		for(int j = 0; j < 4; j ++){
			
			for(int k = 0; k < 4; k ++){
				if(first[row1][j] == second[row2][k]){
					counter ++;
					number = first[row1][j];
				}
			}
		}
		
		fout << "Case #" << i << ": ";
		if(counter == 1) fout << number;
		else if(counter == 0) fout << "Volunteer cheated!";
		else fout << "Bad magician!";

		fout << endl;

	}


	return 0;
}


