#include <sstream>
#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <set>
#include <math.h>

using namespace std;


bool checkCol(vector<vector<int> > &board, int a){
	for(int b=1; b< board[0].size(); b++){
		if(board[a][b] != board[a][0])
			return false;
	}
	return true;
}

bool checkRow(vector<vector<int> > &board, int b){
	for(int a=1; a< board.size(); a++){
		if(board[a][b] != board[0][b])
			return false;
	}
	return true;
}

bool check(vector<vector<int> > &board, set<int> &mySet){
	set<int>::iterator it = mySet.begin();

	while(it != mySet.end()){
		set<int> row, col;
		for(int a=0; a<board.size(); a++){
			for(int b=0; b<board[0].size(); b++){
				if(board[a][b] == *it){
					if(checkRow(board, b)){
//						cout << "1";
						row.insert(b);
					}
					else if(checkCol(board, a)){
//						cout << "2";
						col.insert(a);
					}
					else{
//						cout << "3";
						return false;
					}
				}
			}
		}
		it++;
		if(it != mySet.end()){
			for(auto val: row){
				for(int a=0; a<board.size(); a++){
					board[a][val] = *it;
				}
			}

			for(auto val: col){
				for(int b=0; b<board[0].size(); b++){
					board[val][b] = *it;
				}
			}
		}
	}

	return true;
}


int main(){
	int round;
	cin >> round;

	for(int i=1; i<=round; i++){
		int m, n;
		cin >> m >> n;
		vector<vector<int> > board(m, vector<int>(n));
		set<int> mySet;
		int tmp = 0;
		for(int a=0; a<m; a++){
			for(int b=0; b<n; b++){
				cin >> tmp;
				board[a][b] = tmp;
				mySet.insert(tmp);
			}

		}
		if(check(board, mySet)){
			cout << "Case #" << i << ": YES\n";
		}
		else{
			cout << "Case #" << i << ": NO\n";
		}


	}

}


