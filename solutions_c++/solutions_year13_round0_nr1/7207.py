#include <cmath>
#include <iostream>
#include <fstream>
#include <cstdlib>
#include <vector>
#include <map>
#include <string>

using namespace std;

int main(){
	ifstream ifile("one.txt");
	ofstream ofile("oneout.txt");
	
	map<char, int> check;	
	vector<char> board;
	
	int size;
	ifile >> size;
	
	for(int i = 0; i < size; i++){
		while(ifile.peek() == '\n'){
			ifile.get();
		}
		bool ocheck = false;
		bool xcheck = false;
		bool complete = true;
		if(!board.empty()){ board.clear(); }
		for(int j = 0; j < 16; j++){
			char getchar = ifile.get();
			board.push_back(getchar);
			if(getchar == '.'){complete = false;}
			if(ifile.peek() == '\n'){
				ifile.get();
			}
		}
		
		for(int j = 0; j < 4; j++){
		// VERTICAL
			check.clear();
			check[board[j]] = 1;
			for(int k = 1; k < 4; k++){
				if(check.find(board[j + (k*4)]) == check.end()){
					check[board[j + (k*4)]] = 1;
				}
				else{
					check[board[j + (k*4)]]++;
				}
			}
			if(check['O'] == 4 || (check['O'] == 3 && check['T'] == 1)){
				ocheck = true;
			}
			if(check['X'] == 4 || (check['X'] == 3 && check['T'] == 1)){
				xcheck = true;
			}
		}
		for(int j = 0; j < 4; j++){
		// HORIZONTAL
			check.clear();
			check[board[j * 4]] = 1;
			for(int k = 1; k < 4; k++){
				if(check.find(board[j*4 + k]) == check.end()){
					check[board[j*4 + (k)]] = 1;
				}
				else{
					check[board[j*4 + (k)]]++;
				}
			}
			if(check['O'] == 4 || (check['O'] == 3 && check['T'] == 1)){
				ocheck = true;
			}
			if(check['X'] == 4 || (check['X'] == 3 && check['T'] == 1)){
				xcheck = true;
			}
		}
		int d = 1;
		
		for(int j = 0; j < 2; j++){
		// DIAGONAL
			check.clear();
			check[board[j * 3]] = 1;
			if(j){ d = -1; }
			for(int k = 1; k < 4; k++){
				if(check.find(board[j*3 + k*(4 + d)]) == check.end()){
					check[board[j*3 + k*(4 + d)]] = 1;
				}
				else{
					check[board[j*3 + k*(4 + d)]]++;
				}
			}
			if(check['O'] == 4 || (check['O'] == 3 && check['T'] == 1)){
				ocheck = true;
			}
			if(check['X'] == 4 || (check['X'] == 3 && check['T'] == 1)){
				xcheck = true;
			}
		}
		
		/**** FINAL CHECK *****/

			if(ocheck){
				ofile << "Case #" << i+1 << ": O won" << endl;
			}
			else if(xcheck){
				ofile << "Case #" << i+1 << ": X won" << endl;
			}
			else if(complete){
				ofile << "Case #" << i+1 << ": Draw" << endl;
			}
			else{
				ofile << "Case #" << i+1 << ": Game has not completed" << endl;
			}
	}

	ofile.close();
	return 0;
}
