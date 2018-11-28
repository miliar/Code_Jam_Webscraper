#include <iostream>
#include <fstream>
using namespace std;
int main(void)
{
	ifstream in;
	ofstream out;
	in.open("A-large.in", ios::in);
	out.open("A-large.out", ios::out);
	int testCase=0;
	in >> testCase;
	char board[2][16];
	for(int testCount=0; testCount < testCase; ++testCount)
	{
		bool emptyFlag = false, winFlag=false;
		char winSym;
		for( int inRep=0; inRep < 16; ++inRep )
		{
			in >> board[0][inRep];
			board[1][inRep] = board[0][inRep];
			if( board[0][inRep] == 'T' ) {
				board[0][inRep] = 'O';
				board[1][inRep] = 'X';
			}
			if( board[0][inRep] == '.')
				emptyFlag = true;
		}
		for( int rep=0; rep < 4; ++rep )
		{
			int colIdx = rep*4;
			if( board[0][colIdx] != '.' ) {
				if( board[0][colIdx] == board[0][colIdx+1] && 
					board[0][colIdx] == board[0][colIdx+2] &&
					board[0][colIdx] == board[0][colIdx+3] )
					winFlag = true, winSym = board[0][colIdx];
				if( board[1][colIdx] == board[1][colIdx+1] && 
					board[1][colIdx] == board[1][colIdx+2] &&
					board[1][colIdx] == board[1][colIdx+3] )
					winFlag = true, winSym = board[1][colIdx];
			}
			if( board[0][rep] != '.' ) {
				if( board[0][rep] == board[0][rep+4] && 
					board[0][rep] == board[0][rep+8] &&
					board[0][rep] == board[0][rep+12] )
					winFlag = true, winSym = board[0][rep];
				if( board[1][rep] == board[1][rep+4] && 
					board[1][rep] == board[1][rep+8] &&
					board[1][rep] == board[1][rep+12] )
					winFlag = true, winSym = board[1][rep];
			}
		}
		if( board[0][0] != '.' ) {
			if( board[0][0] == board[0][5] &&
				board[0][0] == board[0][10] &&
				board[0][0] == board[0][15] )
				winFlag = true, winSym = board[0][0];
			if( board[1][0] == board[1][5] &&
				board[1][0] == board[1][10] &&
				board[1][0] == board[1][15] )
				winFlag = true, winSym = board[1][0];
		}
		if( board[0][3] != '.' ) {
			if( board[0][3] == board[0][6] &&
				board[0][3] == board[0][9] &&
				board[0][3] == board[0][12] )
				winFlag = true, winSym = board[0][3];
			if( board[1][3] == board[1][6] &&
				board[1][3] == board[1][9] &&
				board[1][3] == board[1][12] )
				winFlag = true, winSym = board[1][3];
		}
		if( winFlag ) { // win
			out << "Case #" << testCount+1 << ": " << winSym << " won" << endl;
		}
		else if( emptyFlag ) { // Game has not completed
			out << "Case #" << testCount+1 << ": " << "Game has not completed" << endl;
		}
		else { // Draw
			out << "Case #" << testCount+1 << ": " << "Draw" << endl;
		}
	}
	in.close();
	out.close();
	return 0;
}