#include <iostream>

#define REP(i, n) for(int i = 0; i < n; i++)

using namespace std;


int main(){
	ios_base::sync_with_stdio(0);
	int numberOfTests;
	cin >> numberOfTests;
	REP(x, numberOfTests){
		char t[4][4];
		REP(i, 4){
			REP(j, 4){
				cin >> t[i][j];
			}
		}
		bool draw = 1;
		char winner = 'n';
		REP(i, 4){ //kolumny
			int x = 0;
			int y = 0;
			REP(j, 4){
				switch(t[i][j]){
					case 'X':
						x++;
						y = 0;
						break;
					case 'O':
						y++;
						x = 0;
						break;
					case 'T':
						y++;
						x++;
						break;
					case '.':
						x = 0;
						y = 0;
						draw = 0;
						break;
				}
			}
			if(x == 4)
				winner = 'x';
			if(y == 4)
				winner = 'y';
		}
		if(winner == 'n'){ // rzedy
			REP(j, 4){ 
				int x = 0;
				int y = 0;
				REP(i, 4){
					switch(t[i][j]){
						case 'X':
							x++;
							y = 0;
							break;
						case 'O':
							y++;
							x = 0;
							break;
						case 'T':
							y++;
							x++;
							break;
						case '.':
							x = 0;
							y = 0;
							break;
					}
				}
			if(x == 4)
				winner = 'x';
			if(y == 4)
				winner = 'y';
			}
		}
		if(winner == 'n'){ // 1. diagonala
			int a = 0;
			int b = 0;
			int x = 0;
			int y = 0;
			while(a < 4){
				switch(t[a][b]){
					case 'X':
						x++;
						y = 0;
						break;
					case 'O':
						y++;
						x = 0;
						break;
					case 'T':
						y++;
						x++;
						break;
					case '.':
						x = 0;
						y = 0;
						break;
				}
				a++;
				b++;
			}
			if(x == 4)
				winner = 'x';
			if(y == 4)
				winner = 'y';
		}
		if(winner == 'n'){ // 2. diagonala
			int a = 0;
			int b = 3;
			int x = 0;
			int y = 0;
			while(a < 4){
				switch(t[a][b]){
					case 'X':
						x++;
						y = 0;
						break;
					case 'O':
						y++;
						x = 0;
						break;
					case 'T':
						y++;
						x++;
						break;
					case '.':
						x = 0;
						y = 0;
						break;
				}
				a++;
				b--;
			}
			if(x == 4)
				winner = 'x';
			if(y == 4)
				winner = 'y';
		}
		switch(winner){
			case 'x':
				cout << "Case #" << x+1 << ": X won" << endl;
				break;
			case 'y':
				cout << "Case #" << x+1 << ": O won" << endl;
				break;
			case 'n':
				if(draw)
					cout << "Case #" << x+1 << ": Draw" << endl;
				else
					cout << "Case #" << x+1 << ": Game has not completed" << endl;			
		}
	}
	return 0;
}
