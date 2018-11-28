/*
 * =====================================================================================
 *
 *       Filename:  a.cc
 *
 *    Description:  
 *
 *        Version:  1.0
 *        Created:  04/12/2013 05:22:10 PM
 *       Revision:  none
 *       Compiler:  gcc
 *
 *         Author:  Martin Cai (MC), mrtncai@gmail.com
 *   Organization:  
 *
 * =====================================================================================
 */


#include	<stdlib.h>
#include <iostream>

using namespace std;

char checkArr(char *a){
	char p = 0;
	for ( int i = 0; i < 4; i ++ ) {
		char cur = a[i];
//		cout << cur;
		if(cur == 'T')
			continue;
		if(cur == '.'){
//			cout << "incomplete\n";
			return 0; // not complete
		} else if(p == 0) {
			p = cur;
		}else if(p != cur){
//			cout << "draw\n";
			return 0; // draw
		}
	}
//	cout << "winner: " << p;
	return p;
}

char check4(char a, char b, char c, char d){
	char arr[4] = {a, b, c, d};
	return checkArr(arr);
}
/* 
 * ===  FUNCTION  ======================================================================
 *         Name:  main
 *  Description:  
 * =====================================================================================
 */
	int
main ( int argc, char *argv[] )
{
	int T;
	cin >> T;

	for ( int i = 0; i < T; i ++ ) {
		char board[4][4];
		bool complete = true; // assume complete
		cout << "Case #" << (i+1) << ": ";
//		cout << endl;
		// read into matrix
		for ( int j = 0; j < 4; j ++ ) {
			for ( int k = 0; k < 4; k ++ ) {
				char c;
				cin >> c;
				board[j][k] = c;
				if(c == '.') complete = false;
			}
		}
		
	// check game
		char wp = 0;
		// row
		for ( int j = 0; j < 4; j ++ ) {
			if((wp = checkArr(board[j]))) break;
		}
		// col
		if(!wp)
			for ( int j = 0; j < 4; j ++ ) {
				if((wp = check4(board[0][j], board[1][j], board[2][j], board[3][j]))) break;
			}
		// diagonal
		if(!wp)
			wp = check4(board[0][0], board[1][1], board[2][2], board[3][3]);
		if(!wp)
			wp = check4(board[3][0], board[2][1], board[1][2], board[0][3]);

		if(wp){
			cout << wp << " won\n";
		}else if(!complete){
			cout << "Game has not completed\n";
		}else{
			cout << "Draw\n";
		}
	}
	return EXIT_SUCCESS;
}				/* ----------  end of function main  ---------- */
