#include <cstdio>
#include <fstream>
#include <string>
#include <vector>
using namespace std;

int T;
string game[4];

bool checkWin(char Player) {
	for (int i = 0; i < 4; i++) {
		bool isGoodLine = true, isGoodColumn = true, isGoodDiagonale1 = true, isGoodDiagonale2 = true;
		for (int j = 0; j < 4; j++) {
			if (game[i][j] != Player && game[i][j] != 'T') isGoodLine = false;
			if (game[j][i] != Player && game[j][i] != 'T') isGoodColumn = false;
			if (game[j][j] != Player && game[j][j] != 'T') isGoodDiagonale1 = false;
			if (game[j][3 - j] != Player && game[j][3 - j] != 'T') isGoodDiagonale2 = false;
		}
		if (isGoodLine || isGoodColumn || isGoodDiagonale1 || isGoodDiagonale2) return true;
	}
	return false;
}

bool isIncomplete() {
	for (int i = 0 ; i < 4; i++)
		for (int j = 0; j < 4; j++) if (game[i][j] == '.') return true;
	return false;
}

int main()
{
	ifstream in("input.txt");
	ofstream out("output.txt");
	
	in >> T;
	for (int t = 1; t <= T; t++)
	{		
		out << "Case #" << t << ": ";
		for (int i = 0; i < 4; i++) {
			string str;
			in >> game[i];
		}		
		
		if (checkWin('X')) out << "X won\n";
		else if (checkWin('O')) out << "O won\n";
		else if (isIncomplete()) out << "Game has not completed\n";
		else out << "Draw\n";
	}
	return 0;
}
