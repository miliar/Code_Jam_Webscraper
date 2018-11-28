#include <vector>
#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <memory.h>
#include <ctime>
#include <string>
#include <list>
#include <algorithm>
#include <stack>
#include <queue>
#include <deque>
#include <fstream>


using namespace std ;

string Check (char [4][5]) ;

int main ()
{
	ifstream inSt ("A-small-attempt1.in") ;
	try {
		if (inSt.fail ()) throw -1 ;
	}
	catch (int) {
		cerr << "Input file opeing failed." << endl ;
		exit (1) ;
	}
	ofstream outSt ("output.txt") ;
	try {
		if (outSt.fail ()) throw -1 ;
	}
	catch (int) {
		cerr << "Output file opeing failed." << endl ;
		exit (1) ;
	}

	int numT ;
	inSt >> numT ;
	
	for (int i =0 ; i < numT ; i++) {
		char board[4][5] ;
		inSt.ignore (2, '\n') ;

		for (int j =0 ; j < 4 ; j++) inSt.getline (board[j], 5) ;
	
		outSt << "Case #" << i+1 << ": " ;
		outSt << Check (board) << endl ;
	}
	return 0 ;
}

string Check (char board[4][5])
{
	int cnt =1 ;
	bool X =false, O =false, D =false ;
	bool dot =true ;

	for (int i =0 ; i < 4 ; i++) {
		for (int j =0 ; j < 4 ; j++) {
			if (board[i][j] != '.') {
				if ((board[i][j] == 'X' && X < 2) || (board[i][j] == 'O' && O < 2)) {
					cnt =1 ;
					for (int k =j+1, p =i+1 ; p < 4 && k < 4 ; k++, p++)
						if (board[i][j] == board[p][k] || board[p][k] == 'T') cnt++ ;
						else break ;
					if (cnt == 4) {
						if (board[i][j] == 'X') X =true ;
						else if (board[i][j] == 'O') O =true ;
					}

					cnt =1 ;
					for (int k =j-1, p =i+1 ; p < 4 && k >= 0 ; k--, p++)
						if (board[i][j] == board[p][k] || board[p][k] == 'T') cnt++ ;
						else break ;
					if (cnt == 4) {
						if (board[i][j] == 'X') X =true ;
						else if (board[i][j] == 'O') O =true ;
					}

					cnt =1 ;
					for (int k =j, p =i+1 ; p < 4 ; p++)
						if (board[i][j] == board[p][k] || board[p][k] == 'T') cnt++ ;
						else break ;
					if (cnt == 4) {
						if (board[i][j] == 'X') X =true ;
						else if (board[i][j] == 'O') O =true ;
					}

					cnt =1 ;
					for (int k =j+1, p =i ; k < 4 ; k++)
						if (board[i][j] == board[p][k] || board[p][k] == 'T') cnt++ ;
						else break ;
					if (cnt == 4) {
						if (board[i][j] == 'X') X =true ;
						else if (board[i][j] == 'O') O =true ;
					}
				}
			}
			else dot =false ;
		}
	}

	return (O && !X) ? "O won" :
		(!O && X) ? "X won" :
		(dot && (O == X)) ? "Draw" :
		"Game has not completed" ;
}