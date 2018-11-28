//============================================================================
// Name        : .cpp
// Author      : 
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include <stdlib.h>
#include <stdio.h>
using namespace std;

string grid[4];

string fu(){
	bool flag, mayD = false, x, o;

	for(int i=0; i<4 && !mayD; i++)
		for(int j=0; j<4 && !mayD; j++)
			mayD = grid[i][j] == '.';
	mayD = 1-mayD;

	for(int i=0; i<4; i++){
		flag= true, x = false, o = false;
		for(int j=0; j<4 && flag; j++){
			if(grid[i][j]=='X') x++;
			else if(grid[i][j]=='O') o++;
			else if(grid[i][j]=='.')
				flag = false;
			if(x + o == 2)
				flag = false;
		}
		if(flag){
			if(x) return "X won";
			else return "O won";
		}
	}
	for(int j=0; j<4; j++){
		flag= true, x = false, o = false;
		for(int i=0; i<4 && flag; i++){
			if(grid[i][j]=='X') x++;
			else if(grid[i][j]=='O') o++;
			else if(grid[i][j]=='.')
				flag = false;
			if(x + o == 2)
				flag = false;
		}
		if(flag){
			if(x) return "X won";
			else return "O won";
		}
	}

	flag= true, x = false, o = false;
	for(int i=0; i<4 && flag; i++){
		if(grid[i][i]=='X') x++;
		else if(grid[i][i]=='O') o++;
		else if(grid[i][i]=='.')
			flag = false;
		if(x + o == 2)
			flag = false;
	}
	if(flag){
		if(x) return "X won";
		else return "O won";
	}

	flag= true, x = false, o = false;
	for(int i=0; i<4 && flag; i++){
		if(grid[i][3-i]=='X') x++;
		else if(grid[i][3-i]=='O') o++;
		else if(grid[i][3-i]=='.')
			flag = false;
		if(x + o == 2)
			flag = false;
	}
	if(flag){
		if(x) return "X won";
		else return "O won";
	}

	if(mayD == true) return "Draw";
	else return "Game has not completed";
}

int main() {

#ifndef ONLINE_JUDGE
	freopen("A-large.in","rt",stdin);
	freopen("out.txt","wt",stdout);
#endif

	int T;
	cin >> T;
	for(int t=1; t<=T; t++){
		cout << "Case #" << t << ": ";
		for(int i=0; i<4; i++){
			cin >> grid[i];
		}
		cout << fu() << endl;
	}

	return 0;
}
