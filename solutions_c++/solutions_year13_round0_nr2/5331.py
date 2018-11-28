#include<queue>
#include<fstream>
#include<iostream>
#include<stdlib.h>
#include<math.h>

using namespace std;

ifstream fin("B-large.in");
ofstream fout("out.txt");

int field[200][200];
int target[200][200];

int main(){

	int nCases;
	int rows, columns;

	fin>> nCases;

	for( int l = 1; l <= nCases; l++){

		fin>>rows>>columns;

		for( int i = 0; i < rows; i++){
			for( int j = 0; j < columns; j++){
				field[i][j] = 100;
			}
		}

		for( int i = 0; i < rows; i++){
			for( int j = 0; j < columns; j++){
				fin>>target[i][j];
			}
		}


		int maximum;

		for( int i = 0; i < rows; i++){
			maximum = -1;
			for( int j = 0; j < columns; j++){
				maximum = max(target[i][j], maximum); 
			}

			for( int j = 0; j < columns; j++){
				field[i][j] = min(field[i][j], maximum);
			}
		}

		for( int i = 0; i < columns; i++){
			maximum = -1;
			for( int j = 0; j < rows; j++){
				maximum = max(target[j][i], maximum); 
			}

			for( int j = 0; j < rows; j++){
				field[j][i] = min(field[j][i], maximum);
			}
		}

		bool finished = false;
		for( int i = 0; i < rows && !finished; i++){
			for( int j = 0; j < columns && !finished; j++){
				if( field[i][j] != target[i][j]){
					fout<<"Case #"<<l<<": "<<"NO\n";
					finished = true;
				}
			}
		}

		if( !finished){
			fout<<"Case #"<<l<<": "<<"YES\n";
		}

	}
}