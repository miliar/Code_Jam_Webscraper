#include <iostream>
#include <string>
#include <conio.h>
using namespace std;

string scr[4];

bool win(char ch){
	bool good;
	for(int i=0;i<4;i++){
		good = true;
		for(int j=0;j<4;j++)
			if(scr[i][j] != ch) good = false;
		if(good) return true;
		good = true;
		for(int j=0;j<4;j++)
			if(scr[j][i] != ch) good = false;
		if(good) return true;
	}
	good = true;
	for(int i=0;i<4;i++)
		if(scr[i][i] != ch) good = false;
	if(good) return true;

	good = true;
	for(int i=0;i<4;i++)
		if(scr[i][3-i] != ch) good = false;
	return good;
}

void main(){
	freopen("A-small.in", "r", stdin);
	freopen("A-small.out", "w", stdout);

	int T;
	cin>>T;
	for(int tc=1; tc<=T; tc++){
		for(int i=0;i<4;i++)
			cin>>scr[i];
		
		int a=-1,b=-1;
		for(int i=0;i<4;i++)
			for(int j=0;j<4;j++)
				if(scr[i][j] == 'T') a=i,b=j;

		cout << "Case #" << tc << ": ";
		if(a != -1) scr[a][b] = 'X';
		if(win('X')){
			cout << "X won\n";
			continue;
		}
		if(a != -1) scr[a][b] = 'O';
		if(win('O')){
			cout << "O won\n";
			continue;
		}
		
		bool draw = true;
		for(int i=0;i<3;i++)
			for(int j=0;j<3;j++)
				if(scr[i][j] == '.') draw = false;

		if(draw)
			cout << "Draw" << endl;
		else
			cout << "Game has not completed" << endl;
	}

	getch();
}
/*
6

 XXXT
 ....
 OO..
 ....
 
XOXT
 XXOO
 OXOX
 XXOO
 
XOX.
 OX..
 ....
 ....
 
OOXX
 OXXX
 OX.T
 O..O
 
XXXO
 ..O.
 .O..
 T...
 
OXXX
 XO..
 ..O.
 ...O


 Case #1: X won
 Case #2: Draw
 Case #3: Game has not completed
 Case #4: O won
 Case #5: O won
 Case #6: O won
 */