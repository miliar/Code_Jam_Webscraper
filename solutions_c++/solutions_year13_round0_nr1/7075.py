#include <cstdio>
#include <numeric>
#include <iostream>
#include <vector>
#include <set>
#include <cstring>
#include <string>
#include <map>
#include <cmath>
#include <ctime>
#include <algorithm>
#include <bitset>
#include <queue>
#include <sstream>
#include <deque>
#include <fstream>

using namespace std;

#define mp make_pair
#define pb push_back
#define rep(i,n) for(int i = 0; i < (n); i++)
#define re return
#define fi first
#define se second
#define sz(x) ((int) (x).size())
#define all(x) (x).begin(), (x).end()
#define sqr(x) ((x) * (x))
#define sqrt(x) sqrt(abs(x))
#define y0 y3487465
#define y1 y8687969
#define fill(x,y) memset(x,y,sizeof(x))
                         
typedef vector<int> vi;
typedef long long ll;
typedef long double ld;
typedef double D;
typedef pair<int, int> ii;
typedef vector<ii> vii;
typedef vector<string> vs;
typedef vector<vi> vvi;

#define SIZE 4

class TicTacToe {

public:
	char B[SIZE][SIZE];

	TicTacToe(){
	}

	void readBoard(ifstream &in){
		string line;
		for(int i=0; i<SIZE; i++) {
			getline(in,line);
			for(int j=0; j<SIZE; j++)
				B[i][j] = line[j];
		}
		//printBoard();	
	} 

	void printBoard(){
		cout << "New Board" <<endl;
		for(int i=0; i<SIZE; i++) {
			for(int j=0; j<SIZE; j++)
				cout<<B[i][j];

		cout << endl;
		}	
	}

	bool checkWin(char type) {

		int countType = 0;
		int countT = 0;

		//check horizontally
		for(int i =0 ; i<SIZE; i++){
			countT = 0;
			countType = 0;
			for(int j=0; j<SIZE; j++) {
				if(B[i][j]==type) {
					countType++;
				}
				if(B[i][j]=='T')
					countT ++;
			}
			if(countType == SIZE)
				return true;
			else if(countType == SIZE-1 && countT == 1)
				return true;
		}

		//check vertically
		for(int j =0 ; j<SIZE; j++){
			countT = 0;
			countType = 0;
			for(int i=0; i<SIZE; i++) {
				if(B[i][j]==type) {
					countType++;
				}
				if(B[i][j]=='T')
					countT ++;
			}
			if(countType == SIZE)
				return true;
			else if(countType == SIZE-1 && countT == 1)
				return true;
		}

		//check diagonally
		countT = 0;
		countType = 0;
		for(int i =0 ; i<SIZE; i++){	
			if(B[i][i]==type) 
					countType++;
			if(B[i][i]=='T')
					countT ++;
		}
		if(countType == SIZE)
				return true;
		else if(countType == SIZE-1 && countT == 1)
				return true;
		
		countT = 0;
		countType = 0;
		for(int i =0 ; i<SIZE; i++){
			if(B[i][SIZE-i-1]==type) 
					countType++;
			if(B[i][SIZE-i-1]=='T')
					countT ++;
		}
		if(countType == SIZE)
				return true;
		else if(countType == SIZE-1 && countT == 1)
				return true;

		return false;
	}

	bool checkIncompleteGame() {

		for(int i=0; i<SIZE; i++)
			for(int j=0; j<SIZE; j++)
				if(B[i][j]=='.')
					return true;

		return false;
	}

	bool checkDraw() {
		//nop

	}
};

int main(int argc, char* argv[]){

	ifstream in(argv[1],ios::in);
	ofstream out("tip.txt",ios::out);
	TicTacToe board;
	string line;
	getline(in,line);
	int t;
	stringstream s;
	s << line;
	s >> t;
	int num = 1;
	while(t > 0){
		board.readBoard(in);
		if(board.checkWin('X'))
			out << "Case #"<<num<<": X won" <<endl;
		else if(board.checkWin('O'))
			out << "Case #"<<num<<": O won" <<endl;
		else if(board.checkIncompleteGame()) 
			out << "Case #"<<num<< ": Game has not completed" <<endl;
		else
			out << "Case #"<<num<<": Draw" <<endl;
			 		
		t--;
		num++;
		getline(in,line);
	}
	in.close();
	out.close();
	return 0;
}