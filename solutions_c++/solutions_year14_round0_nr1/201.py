#ifdef _MSC_VER
//#define _CRTDBG_MAP_ALLOC
#include <stdlib.h>
#include <crtdbg.h>
#endif

#include "Jams.h"
#include "CodeJam.h"

class MagicTrick : public CodeJam {
protected:
	void solve(int task) override {
		int row1, row2;
		readln(row1);
		row1--;
		int M1[4][4] = { 0 };
		for (int i = 0; i < 4; i++) {
			readln(M1[i][0], M1[i][1], M1[i][2], M1[i][3]);
		}
		readln(row2);
		row2--;
		int M2[4][4] = { 0 };
		for (int i = 0; i < 4; i++) {
			readln(M2[i][0], M2[i][1], M2[i][2], M2[i][3]);
		}

		int Card = -1;
		int foundCards = 0;
		for (int i = 0; i < 4; i++)
			for (int j = 0; j < 4; j++) {
				if (M1[row1][i] == M2[row2][j]) {
					Card = M1[row1][i];
					++foundCards;
				}
			}

		if (foundCards <= 0)
			writeResult("Volunteer cheated!");
		else if (foundCards > 1)
			writeResult("Bad magician!");
		else
			writeResult(Card);

	}
};

void SolveJams() {
	/*OsmosJam jam1;
	jam1.solveJam("osm");

	WordJam jam2;
	jam2.solveJam("test");

	ScaleJam jam3;
	jam3.solveJam("dot");
	T9Jam jam4;
	jam4.solveJam("t9");
	DiamonsJam jam5;
	jam5.solveJam("diamond");*/
}

int main()
{	
	MagicTrick m;
	m.solveJam("m");
	//SolveJams();
#ifdef _MSC_VER
	_CrtDumpMemoryLeaks();
#endif
	return 0;
}

