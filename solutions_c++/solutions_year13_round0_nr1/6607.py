#include <iostream>
#include <string>
#include <vector>
using namespace std;
//const char* FILE_IN = "test.in";
const char* FILE_IN = "A-large.in";
const char* FILE_OU = "A-large.ou";

#define X_WON 0
#define O_WON 1
#define DRAW 2
#define NOT 3

int judge ( const vector<string>& board ) {
	int i,j;
	//row test
	for ( i=0 ; i<4;  i++)  {
		//x
		for ( j=0 ; j<4 ; j++ ) {
			if ( board[i][j]=='X' || board[i][j]=='T' ) continue;
			else break;
		}
		if ( j==4 ) return X_WON;
		//O
		for ( j=0 ; j<4 ; j++ ) {
			if ( board[i][j]=='O' || board[i][j]=='T' ) continue;
			else break;
		}
		if ( j==4 ) return O_WON;
	}
	//column test
	for ( i=0 ; i<4 ; i++ ) {
		//x
		for ( j=0 ; j<4 ; j++ ) {
			if ( board[j][i]=='X' || board[j][i]=='T' ) continue;
			else break;
		}
		if ( j==4 ) return X_WON;
		//O
		for ( j=0 ; j<4 ; j++ ) {
			if ( board[j][i]=='O' || board[j][i]=='T' ) continue;
			else break;
		}
		if ( j==4 ) return O_WON;
	}
	//diag test X
	for ( i = 0 ;i<4 ; i++ ) {
		if ( board[i][i]=='X' || board[i][i]=='T' ) continue;
		else break;
	}
	if ( i==4 ) return X_WON;
	//diag test O
	for ( i = 0 ;i<4 ; i++ ) {
		if ( board[i][i]=='O' || board[i][i]=='T' ) continue;
		else break;
	}
	if ( i==4 ) return O_WON;
	//oppo diag test X
	for ( i = 0 ;i<4 ; i++ ) {
		if ( board[3-i][i]=='X' || board[3-i][i]=='T' ) continue;
		else break;
	}
	if ( i==4 ) return X_WON;
	//oppo diag test O
	for ( i = 0 ;i<4 ; i++ ) {
		if ( board[3-i][i]=='O' || board[3-i][i]=='T' ) continue;
		else break;
	}
	if ( i==4 ) return O_WON;
	//not complete test
	for ( i =0 ; i<4 ; i++ ) {
		for ( j=0 ; j<4 ; j++ ) {
			if ( board[i][j]=='.' ) return NOT;
		}
	}
	return DRAW;
}

int main ( ){
	int cas;
	freopen(FILE_IN,"r",stdin);
	freopen(FILE_OU,"w",stdout);
	cin>>cas;
	vector<string> board(4,"");
	for ( int i = 1 ; i<=cas ; i++ ) {
		cout<<"Case #"<<i<<": ";
		for ( int j = 0 ; j<4 ; j++ ) {
			cin>>board[j];
		}
		switch ( judge(board) ){
		case X_WON:
			cout<<"X won"<<endl;
			break;
		case O_WON:
			cout<<"O won"<<endl;
			break;
		case DRAW:
			cout<<"Draw"<<endl;
			break;
		case NOT:
			cout<<"Game has not completed"<<endl;
			break;
		default:
			break;
		}
	}

	return 0;
}