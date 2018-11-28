/*
ID: paelletadecaragols@gmail.com
PROG: Tic-Tac-Toe-Tomek
LANG: C++
*/

#include <iostream>
#include <fstream>
#include <iomanip>
#include <string>

using namespace std;

int i, j, proofCases, capMatrix = 4;
bool print, finalGame;

ifstream fin;
ofstream fout;


void horizontalTest(string b, int pos);
void verticalTest(string b, int pos);
void diagonalTest(string b, int pos, int d);

int main(){
	string board;
	string line;
	
	fin.open("A-small-attempt1.in");
        fout.open("A-small-attempt1.out");

	fin >> proofCases;
	
	for(i=0; i<proofCases; i++){
		board = "";
		for(j=0; j<capMatrix; j++){
			fin >> line;
			board += line;
		}
		print = false; finalGame = true;
		for(j=0; j<16; j++){
			if(j%capMatrix == 0 and !print) horizontalTest(board, j);
			if(j < capMatrix and !print) verticalTest(board, j);
			if(j == 0 and !print) diagonalTest(board, j, 1);
			if(j == capMatrix-1 and !print) diagonalTest(board, j, -1);
			if(board[j] == '.') finalGame = false;
		}
		if(finalGame and !print)
			fout << "Case #" << i+1 << ": Draw" << endl;
		else if(!finalGame and !print)
			fout << "Case #" << i+1 << ": Game has not completed" << endl;
	}
	fin.close();
	fout.close();
}

void horizontalTest(string b, int pos){
	bool ok = true;
	if(b[pos] == 'T') pos++;
	if(b[pos] == '.') ok = false;
	else{
		for(int i=pos; i<pos+capMatrix; i++){
			if(b[i] != b[pos] and b[i] != 'T'){
				ok = false;
				break;
			}
		}
	}
	if(ok){
		fout << "Case #" << i+1 << ": " << b[pos] << " won" << endl;
		print = true;
	}
}
void verticalTest(string b, int pos){
	bool ok = true;
	if(b[pos] == 'T') pos += capMatrix;
        if(b[pos] == '.') ok = false;
        else{
                for(int i=pos; i<capMatrix*capMatrix; i+=capMatrix){
                        if(b[i] != b[pos] and b[i] != 'T'){
                                ok = false;
                                break;
                        }
                }
        }
        if(ok){
		fout << "Case #" << i+1 << ": " << b[pos] << " won" << endl;
		print = true;
	}
}
void diagonalTest(string b, int pos, int d){
	bool ok = true;
	if(b[pos] == 'T') pos += capMatrix+d;
        if(b[pos] == '.') ok = false;
        else{
                for(int i=pos; i<capMatrix*capMatrix+d; i+=capMatrix+d){
                        if(b[i] != b[pos] and b[i] != 'T'){
                                ok = false;
                                break;
                        }
                }
        }
        if(ok){
		fout << "Case #" << i+1 << ": " << b[pos] << " won" << endl;
		print = true;
	}
}

