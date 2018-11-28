#include <fstream>
#include <conio.h>
using namespace std;
ifstream fin("input.txt");
ofstream fout("output.txt");
int main(){
	int N;
	fin>>N;
	int n = N;
	char table[4][4];
	string out[N];
	int ctr = 0;
	while(n > 0){ 
	
	for(int i = 0; i < 4; i++){
		for(int j = 0; j < 4; j++){
			fin>>table[i][j];
		}
	}
	
	int ct = 0, ot = 0, xt = 0, dt = 0;
	for(int i = 0; i < 4; i++){
		if(table[ct][i] == 'X')xt++;
		else if(table[ct][i] == '.')dt++;
		else if(table[ct][i] == 'O')ot++;
	}
	if(xt > 2 && ot == 0 && dt == 0){out[ctr] = "X won"; goto repeat; }
	else if(ot > 2 && xt == 0 && dt == 0){out[ctr] = "O won"; goto repeat; }
	
	ct = 1, ot = 0, xt = 0; dt = 0;
	for(int i = 0; i < 4; i++){
		if(table[ct][i] == 'X')xt++;
		else if(table[ct][i] == '.')dt++;
		else if(table[ct][i] == 'O')ot++;
	}
	if(xt > 2 && ot == 0 && dt == 0){out[ctr] = "X won"; goto repeat; }
	else if(ot > 2 && xt == 0 && dt == 0){ out[ctr] = "O won"; goto repeat; }
	
	ct = 2, ot = 0, xt = 0; dt = 0;
	for(int i = 0; i < 4; i++){
		if(table[ct][i] == 'X')xt++;
		else if(table[ct][i] == '.')dt++;
		else if(table[ct][i] == 'O')ot++;
	}
	if(xt > 2 && ot == 0 && dt == 0){out[ctr] = "X won"; goto repeat; }
	else if(ot > 2 && xt == 0 && dt == 0){out[ctr] = "O won"; goto repeat;}
	
	ct = 3, ot = 0, xt = 0; dt = 0;
	for(int i = 0; i < 4; i++){
		if(table[ct][i] == 'X')xt++;
		else if(table[ct][i] == '.')dt++;
		else if(table[ct][i] == 'O')ot++;
	}
	if(xt > 2 && ot == 0 && dt == 0){out[ctr] = "X won"; goto repeat; }
	else if(ot > 2 && xt == 0 && dt == 0){ out[ctr] = "O won"; goto repeat; }
	
	ot = 0; xt = 0; dt = 0;
	for(int i = 0; i < 4; i++){
		if(table[i][i] == 'X')xt++;
		else if(table[i][i] == '.')dt++;
		else if(table[i][i] == 'O')ot++;
	}	
	if(xt > 2 && ot == 0 && dt == 0){out[ctr] = "X won"; goto repeat;}
	else if(ot > 2 && xt == 0 && dt == 0){ out[ctr] = "O won"; goto repeat; }
	
	ot = 0; xt = 0; dt = 0;
	for(int i = 0; i < 4; i++){
		if(table[i][4-i-1] == 'X')xt++;
		else if(table[i][4-i-1] == '.')dt++;
		else if(table[i][4-i-1] == 'O')ot++;
	}
	if(xt > 2 && ot == 0 && dt == 0){out[ctr] = "X won"; goto repeat; }
	else if(ot > 2 && xt == 0 && dt == 0){out[ctr] = "O won"; goto repeat; }
	
	ct = 0; ot = 0; xt = 0; dt = 0;
	for(int i = 0; i < 4; i++){
		if(table[i][ct] == 'X')xt++;
		else if(table[i][ct] == '.')dt++;
		else if(table[i][ct] == 'O')ot++;
	}
	if(xt > 2 && ot == 0 && dt == 0){out[ctr] = "X won"; goto repeat;}
	else if(ot > 2 && xt == 0 && dt == 0){out[ctr] = "O won"; goto repeat;}
	
	ct = 1; ot = 0; xt = 0; dt = 0;
	for(int i = 0; i < 4; i++){
		if(table[i][ct] == 'X')xt++;
		else if(table[i][ct] == '.')dt++;
		else if(table[i][ct] == 'O')ot++;
	}
	if(xt > 2 && ot == 0 && dt == 0){out[ctr] = "X won"; goto repeat; }
	else if(ot > 2 && xt == 0 && dt == 0){out[ctr] = "O won"; goto repeat; }
	
	ct = 2; ot = 0; xt = 0; dt = 0;
	for(int i = 0; i < 4; i++){
		if(table[i][ct] == 'X')xt++;
		else if(table[i][ct] == '.')dt++;
		else if(table[i][ct] == 'O')ot++;
		
	}
	if(xt > 2 && ot == 0 && dt == 0){out[ctr] = "X won"; goto repeat; }
	else if(ot > 2 && xt == 0 && dt == 0){ out[ctr] = "O won"; goto repeat; }
	
	ct = 3; ot = 0; xt = 0; dt = 0;
	for(int i = 0; i < 4; i++){
		if(table[i][ct] == 'X')xt++;
		else if(table[i][ct] == '.')dt++;
		else if(table[i][ct] == 'O')ot++;
	}
	if(xt > 2 && ot == 0 && dt == 0){out[ctr] = "X won"; goto repeat; }
	else if(ot > 2 && xt == 0 && dt == 0){ out[ctr] = "O won"; goto repeat;}
	xt = 0;
	for(int i = 0; i < 4; i++){
		for(int j = 0; j < 4; j++){
			if(table[i][j] == '.')xt++;
		}
	}
	if(xt == 0){out[ctr] = "Draw";}
	else {out[ctr] = "Game has not completed";}
	repeat: 
	ctr++; n--;
	}
	for(int j = 0; j < N; j++){
			fout<<"Case #"<<j+1<<": "<<out[j]<<'\n';
	}
	getch();
	return 0;
}
