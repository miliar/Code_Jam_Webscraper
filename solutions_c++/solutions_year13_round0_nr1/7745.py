//============================================================================
// Name        : googleJam1.cpp
// Author      : 
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include <string>
#include <sstream>
using namespace std;

inline string intToString(int n) {
	std::ostringstream oss;
	// écrire un nombre dans le flux
	oss << n;
	// récupérer une chaîne de caractères
	return oss.str();
}

int main() {
	int n;
	cin >> n;
	string res;

	char tab[4][4];

	for (int l = 1; l <= n; ++l) {
		for (int i = 0; i < 4; ++i) {
			for (int j = 0; j < 4; ++j) {
				cin >> tab[i][j];
			}
		}
		int nbX = 0;
		int nbO = 0;
		int nbP = 0;
		bool gameover = false;
		for (int lignes = 0; lignes < 4 && !gameover; ++lignes) {
			nbX = 0;
			nbO = 0;
			for (int col = 0; col < 4; ++col) {
				if (tab[lignes][col] == 'X' || tab[lignes][col] == 'T')
					nbX++;
				if (tab[lignes][col] == 'O' || tab[lignes][col] == 'T')
					nbO++;
				else if (tab[lignes][col] == '.')
					nbP++;
			}
			if (nbX == 4) {
				res += "Case #" + intToString(l) + ": X won\n";
				gameover = true;
			} else if (nbO == 4) {
				res += "Case #" + intToString(l) + ": O won\n";
				gameover = true;
			}
		}

		for (int clonnnes = 0; clonnnes < 4 && !gameover; ++clonnnes) {
			nbX = 0;
			nbO = 0;
			for (int li = 0; li < 4; ++li) {
				if (tab[li][clonnnes] == 'X' || tab[li][clonnnes] == 'T')
					nbX++;
				if (tab[li][clonnnes] == 'O' || tab[li][clonnnes] == 'T')
					nbO++;
			}
			if (nbX == 4) {
				res += "Case #" + intToString(l) + ": X won\n";
				gameover = true;
			} else if (nbO == 4) {
				res += "Case #" + intToString(l) + ": O won\n";
				gameover = true;
			}
		}
		nbX = 0;
		nbO = 0;
		for (int diag = 0; diag < 4&& !gameover; ++diag) {
			if (tab[diag][diag] == 'X' || tab[diag][diag] == 'T')
				nbX++;
			if (tab[diag][diag] == 'O' || tab[diag][diag] == 'T')
				nbO++;
			if (nbX == 4) {
				res += "Case #" + intToString(l) + ": X won\n";
				gameover = true;
			} else if (nbO == 4) {
				res += "Case #" + intToString(l) + ": O won\n";
				gameover = true;
			}
		}
		nbX = 0;
		nbO = 0;
		for (int diag = 0; diag < 4&& !gameover; ++diag) {
			if (tab[diag][3-diag] == 'X' || tab[diag][3-diag] == 'T')
				nbX++;
			if (tab[diag][3-diag] == 'O' || tab[diag][3-diag] == 'T')
				nbO++;
			if (nbX == 4) {
				res += "Case #" + intToString(l) + ": X won\n";
				gameover = true;
			} else if (nbO == 4) {
				res += "Case #" + intToString(l) + ": O won\n";
				gameover = true;
			}
		}
		//cout << nbO  << ","  << nbX <<endl;
		if (!gameover) {
			if (nbP > 0)
				res += "Case #" + intToString(l) + ": Game has not completed\n";

			else
				res += "Case #" + intToString(l) + ": Draw\n";
		}

	}
	cout << res; // prints !!!Hello World!!!
	return 0;
}
