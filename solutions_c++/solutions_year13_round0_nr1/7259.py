#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
using namespace std;

ifstream input;
ofstream output;

void Case(int);

int main(){
	input.open ("input.txt");
	output.open ("output.txt");
	int cases=0;
	input >> cases;

	cout << "START"<<endl;
	cout << "Cases #"<<cases<<endl<<endl;
	for(int i=0; i<cases; i++){
		Case(i+1);
	}
	input.close();
	output.close();
	cout << "DONE";

	while(1);
	return 0;
}

void Case(int number){
	cout << "Case #"<<number<<endl;

	unsigned char letters[4][4];
	int clears = 0;
	for(int y=0; y<4; y++) for(int x=0; x<4; x++){
		letters[x][y]=='.';
	}
	for(int y=0; y<4; y++) for(int x=0; x<4; x++){
		input >> letters[x][y];
		if (letters[x][y]=='.')		clears+=1;
	}

	if (letters[0][0]=='X' || letters[0][0]=='T'){
		int chain = 0;
		for(int y=0; y<4; y++){
			if (letters[y][y]=='X' || letters[y][y]=='T')	chain+=1;
		}
		if (chain==4){	output << "Case #"<<number<<": X won" << endl;		return;		}
	}
	if (letters[0][0]=='O' || letters[0][0]=='T'){
		int chain = 0;
		for(int y=0; y<4; y++){
			if (letters[y][y]=='O' || letters[y][y]=='T')	chain+=1;
		}
		if (chain==4){	output << "Case #"<<number<<": O won" << endl;		return;		}
	}

	if (letters[0][3]=='X' || letters[0][3]=='T'){
		int chain = 0;
		for(int y=0; y<4; y++){
			if (letters[y][3-y]=='X' || letters[y][3-y]=='T')	chain+=1;
		}
		if (chain==4){	output << "Case #"<<number<<": X won" << endl;		return;		}
	}
	if (letters[0][3]=='O' || letters[0][3]=='T'){
		int chain = 0;
		for(int y=0; y<4; y++){
			if (letters[y][3-y]=='O' || letters[y][3-y]=='T')	chain+=1;
		}
		if (chain==4){	output << "Case #"<<number<<": O won" << endl;		return;		}
	}

	for(int x=0; x<4; x++){
		if (letters[x][0]=='X' || letters[x][0]=='T'){
			int chain = 0;
			for(int y=0; y<4; y++){
				if (letters[x][y]=='X' || letters[x][y]=='T')	chain+=1;
			}
			if (chain==4){	output << "Case #"<<number<<": X won" << endl;		return;		}
		}
		if (letters[x][0]=='O' || letters[x][0]=='T'){
			int chain = 0;
			for(int y=0; y<4; y++){
				if (letters[x][y]=='O' || letters[x][y]=='T')	chain+=1;
			}
			if (chain==4){	output << "Case #"<<number<<": O won" << endl;		return;		}
		}

		if (letters[0][x]=='X' || letters[0][x]=='T'){
			int chain = 0;
			for(int y=0; y<4; y++){
				if (letters[y][x]=='X' || letters[y][x]=='T')	chain+=1;
			}
			if (chain==4){	output << "Case #"<<number<<": X won" << endl;		return;		}
		}
		if (letters[0][x]=='O' || letters[0][x]=='T'){
			int chain = 0;
			for(int y=0; y<4; y++){
				if (letters[y][x]=='O' || letters[y][x]=='T')	chain+=1;
			}
			if (chain==4){	output << "Case #"<<number<<": O won" << endl;		return;		}
		}
	}

	if (clears==0){
		output << "Case #"<<number<<": Draw" << endl;
		return;
	}

	output << "Case #"<<number<<": Game has not completed" << endl;
}