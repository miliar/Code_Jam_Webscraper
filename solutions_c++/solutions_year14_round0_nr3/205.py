#ifdef _MSC_VER
//#define _CRTDBG_MAP_ALLOC
#include <stdlib.h>
#include <crtdbg.h>
#endif

#include "..\Source\Jams.h"
#include "..\Source\CodeJam.h"

class Minesweeper : public CodeJam {
protected:	
	void solve(int task) override {
		int R, C, M;
		readln(R, C, M);
		writeResult("");
		int Map[50][50] = { 0 };
		for (int i = 0; i < R; i++)
			for (int j = 0; j < C; j++)
				Map[i][j] = -1;
		int Cells = R * C;
		int leftMines = Cells - M;

		auto InField = [&](int r, int c) {
			return r >= 0 && c >= 0 && r < R && c < C;
		};

		auto printMap = [&]() {			
			int iMine = 0;
			for (int i = 0; i < R; i++) {
				for (int j = 0; j < C; j++) {
					if (i == 0 && j == 0)
						output << 'c';
					else if (Map[i][j] == -1) {
						output << '*';
						++iMine;
					}
					else
						output << '.';
				}
				output << endl;
			}
			if (iMine != M)
				M = 10;
		};

		auto calcOpeningM = [&](int r, int c) { 
			int mines = 0;
			for (int i = r - 1; i <= r + 1; i++)
				for (int j = c - 1; j <= c + 1; j++)
					if (InField(i, j) && Map[i][j] == -1)
						++mines;
			return mines;
		};

		auto openCell = [&](int r, int c) {
			int mines = 0;
			for (int i = r - 1; i <= r + 1; i++)
				for (int j = c - 1; j <= c + 1; j++)
					if (InField(i, j))
						Map[i][j] = 0;
			for (int i = r - 2; i <= r + 2; i++)
				for (int j = c - 2; j <= c + 2; j++)
					if (InField(i, j) && Map[i][j] >= 0)
						Map[i][j] = calcOpeningM(i, j);			
		};

		if (Cells == M + 1) {
			Map[0][ 0] = 0;
			printMap();
		}
		else if (C > 0 && R > 0) {			
			Map[0][0] = calcOpeningM(0, 0);
			int diagR = 0; int diagC = 0;
			bool Possible = true;
			while (Possible && leftMines > 0) {
				int diagc = diagC;
				int newR = -1; int newC = -1;
				int newLeftMines = leftMines;
				Possible = false;
				for (int diagr = diagR; diagr >= 0; --diagr, ++diagc) {
					if (InField(diagr, diagc)) {
						Possible = true;
						int nm = leftMines - Map[diagr][diagc];
						if (nm < newLeftMines && nm >= 0) {
							newLeftMines = nm;
							newR = diagr;
							newC = diagc;
						}
					}
				}

				if (newR > -1) {
					leftMines -= Map[newR][newC];
					openCell(newR, newC);
				}
				else {
					++diagR;
				}
			}

			if (Possible) {
				printMap();
			} else
				output << "Impossible" << endl;
		}
		else {			
			output << "Impossible" << endl;
		}
	}
};


int main()
{	
	Minesweeper m;
	m.solveJam("m");
	return 0;
}

