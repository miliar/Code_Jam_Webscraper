#include <iostream>
#include <sstream>
#include <numeric>
#include <set>
#include <algorithm>
#include <map>
#include <vector>
#include <queue>
#include <stack>
#include <list>
#include <strings.h>
#include <limits.h>
#include <stdlib.h>
#include <float.h>

using namespace std;

char symbols[4] = {'^', '>', 'v', '<'};

int moveFirst[4] = {-1, 0, 1, 0};
int moveSecond[4] = {0, 1, 0, -1};
char transformation[256];

int main(){
	transformation['^'] = 0;
	transformation['>'] = 1;
	transformation['v'] = 2;
	transformation['<'] = 3;

	int tests;
	cin >> tests;
	for (int t = 0; t < tests; t++){
		int R, C;
		cin >> R >> C;
		vector< vector < char > > board(R, vector <char > (C));
		vector < pair < int, int > > canChange;
		for (int i = 0; i < R; i++){
			for (int j = 0; j < C; j++){
				cin >> board[i][j];	
			}
		}
		int count = 0;
		bool conflict[board.size()][board[0].size()][4];
		for (int conf = 0; conf < 4; conf++){
			for (int i = 0; i < board.size(); i++){
				for (int j = 0; j < board[i].size(); j++){
					if (board[i][j] == symbols[conf]){
						bool ok = true;
						int currenti = i + moveFirst[conf];
						int currentj = j + moveSecond[conf];
						while(true){
							if ((currenti < 0) || (currentj < 0) || (currenti >= board.size()) || (currentj >= board[0].size())){
								break;
							}
							if (board[currenti][currentj] != '.'){
								ok = false;
								break;
							}
							currenti = currenti + moveFirst[conf];
							currentj = currentj + moveSecond[conf];
						}
						if (ok){//Conflicto, ver si se puede resolver
							bool canSolve = false;
							for (int conf2 = 0; conf2 < 4; conf2++){
								int currenti = i + moveFirst[conf2];
								int currentj = j + moveSecond[conf2];
								while(true){
									if ((currenti < 0) || (currentj < 0) || (currenti >= board.size()) || (currentj >= board[0].size())){
										break;
									} 
									if (board[currenti][currentj] != '.'){
										canSolve = true;
										break;
									}
									currenti = currenti + moveFirst[conf2];
									currentj = currentj + moveSecond[conf2];
								}
							}
							if (canSolve){
								count++;
							} else {
								count = -1000000;
							}
						}
					}
				}
			}
		}
		if (count < 0){
			cout << "Case #" << (t+1) << ": IMPOSSIBLE" << endl;
		} else {
			cout << "Case #" << (t+1) << ": " << count << endl;
		}
	}
}
