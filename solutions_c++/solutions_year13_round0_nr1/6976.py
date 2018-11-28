#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <string>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
using namespace std; 

char B[4][4];

int main(){

	freopen("B.in", "rt", stdin);
	freopen("B.out", "wt", stdout);

	int r,N,i,j;
	char current;
	char it;
	char w;
	bool points;
	
   	cin >> N;

   	for(r=0;r<N;r++){
   		cout << "Case #" << r+1 << ": ";
		//cerr << "Case #" << r+1 << ": ";
		w = '-';
		points = false;

		for(i=0;i<4;i++){
			for(j=0;j<4;j++){
				cin >> B[i][j];
				if(B[i][j]=='.') points = true;
			}	
		}
	
		//check rows and columns
		for(i=0;i<4;i++){
			if((B[i][0] == 'X' or B[i][0] == 'T') && (B[i][1] == 'X' or B[i][1] == 'T') && (B[i][2] == 'X' or B[i][2] == 'T') && (B[i][3] == 'X' or B[i][3] == 'T')){
				w = 'X';
				break;	
			} 
			if((B[i][0] == 'O' or B[i][0] == 'T') && (B[i][1] == 'O' or B[i][1] == 'T') && (B[i][2] == 'O' or B[i][2] == 'T') && (B[i][3] == 'O' or B[i][3] == 'T')){
				w = 'O';
				break;	
			}
			if((B[0][i] == 'X' or B[0][i] == 'T') && (B[1][i] == 'X' or B[1][i] == 'T') && (B[2][i] == 'X' or B[2][i] == 'T') && (B[3][i] == 'X' or B[3][i] == 'T')){
				w = 'X';
				break;
			} 
			if((B[0][i] == 'O' or B[0][i] == 'T') && (B[1][i] == 'O' or B[1][i] == 'T') && (B[2][i] == 'O' or B[2][i] == 'T') && (B[3][i] == 'O' or B[3][i] == 'T')){
				w = 'O';
				break;
			} 
		}
		//check diagonals
		if(w=='-'){
			if((B[0][0] == 'X' or B[0][0] == 'T') && (B[1][1] == 'X' or B[1][1] == 'T') && (B[2][2] == 'X' or B[2][2] == 'T') && (B[3][3] == 'X' or B[3][3] == 'T')){
			 	w = 'X';
			 }
			if(w=='-'){
				if ((B[0][0] == 'O' or B[0][0] == 'T') && (B[1][1] == 'O' or B[1][1] == 'T') && (B[2][2] == 'O' or B[2][2] == 'T') && (B[3][3] == 'O' or B[3][3] == 'T')){
					w = 'O';	
				} 
			}
			if(w=='-'){
				if ((B[0][3] == 'X' or B[0][3] == 'T') && (B[1][2] == 'X' or B[1][2] == 'T') && (B[2][1] == 'X' or B[2][1] == 'T') && (B[3][0] == 'X' or B[3][0] == 'T')){
					w = 'X';
				} 
			}
			if(w=='-'){
				if ((B[0][3] == 'O' or B[0][3] == 'T') && (B[1][2] == 'O' or B[1][2] == 'T') && (B[2][1] == 'O' or B[2][1] == 'T') && (B[3][0] == 'O' or B[3][0] == 'T')){
					w = 'O';	
				} 
			}
		}

		if(w=='X') cout << "X won" << endl;
		else if(w=='O') cout << "O won" << endl;
		else if(points) cout << "Game has not completed" << endl;
		else cout << "Draw" << endl;
	}
}

