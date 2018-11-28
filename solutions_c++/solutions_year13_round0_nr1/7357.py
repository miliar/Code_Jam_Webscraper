#include <iostream>
#include <cstdlib>
#include <cstdio>
#include <cmath>

using namespace std;





int main() {
	char board[6][6];
	
	int T;
	cin >> T;
	
	for (int c = 1; c<= T; c++){
		for(int i = 0; i < 4; i++)
			cin >> board[i];
		
		bool gx = false, go = false, sigue  = false;
		
		
		for(int i = 0; !gx && i < 4; i++) {
			bool checa = true;
			for(int j = 0; checa && j < 4; j++)
				checa = checa && (board[i][j] == 'X' || board[i][j] == 'T');
			
			if(checa) gx = true;
		}
		
		for(int i = 0; !gx && i < 4; i++) {
			bool checa = true;
			for(int j = 0; checa && j < 4; j++)
				checa = checa && (board[j][i] == 'X' || board[j][i] == 'T');
			
			if(checa) gx = true;
		}
		
		bool cdiag =  true;
		
		for(int i = 0; i < 4; i++) {
			cdiag = cdiag && (board[i][i] == 'X' || board[i][i] == 'T');
		}
		
		if(cdiag) gx = true;
		
		cdiag =  true;
		
		for(int i = 0; i < 4; i++) {
			cdiag = cdiag && (board[i][3 - i] == 'X' || board[i][3 - i] == 'T');
		}
		
		if(cdiag) gx = true;
		
		
		
		for(int i = 0; !go && i < 4; i++) {
			bool checa = true;
			for(int j = 0; checa && j < 4; j++)
				checa = checa && (board[i][j] == 'O' || board[i][j] == 'T');
			
			if(checa) go = true;
		}
		
		for(int i = 0; !go && i < 4; i++) {
			bool checa = true;
			for(int j = 0; checa && j < 4; j++)
				checa = checa && (board[j][i] == 'O' || board[j][i] == 'T');
			
			if(checa) go = true;
		}
		
		cdiag =  true;
		
		for(int i = 0; i < 4; i++) {
			cdiag = cdiag && (board[i][i] == 'O' || board[i][i] == 'T');
		}
		
		if(cdiag) go = true;
		
		cdiag =  true;
		
		for(int i = 0; i < 4; i++) {
			cdiag = cdiag && (board[i][3 - i] == 'O' || board[i][3 - i] == 'T');
		}
		
		if(cdiag) go = true;
		
		
		
		
		
		
		for(int i = 0; i < 4; i++) {
			for(int j = 0; j < 4; j++) {
				if(board[i][j] == '.') sigue = true;
			}
		}
		
		if(gx && !go) cout << "Case #" << c << ": X won" << endl;
		else if(go && !gx) cout << "Case #" << c << ": O won" << endl;
		else if(sigue) cout << "Case #" << c << ": Game has not completed" << endl;
		else cout << "Case #" << c << ": Draw" << endl;
	}
	
	
	
}
