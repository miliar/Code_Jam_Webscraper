#include <iostream>
#include <cassert>
#include <bitset>
#include <map>
#include <set>
#include <cstring>
using namespace std;


class Game {
private:
	int Arr[2][4][4];
	int TheRow[2];
	int GameNum;
public:
	Game(int gameNum)
		: GameNum(gameNum)
	{
		memset(Arr, 0, sizeof(Arr));
		for (int i=0;i<2;++i)
			for (int i2=0; i2<4; ++i2)
				for (int i3=0; i3<4; ++i3)
					assert(Arr[i][i2][i3] == 0);
		memset(TheRow, 0, sizeof(TheRow));
	}
	void SetCard(int it, int row, int col, int card) {
		Arr[it][row][col] = card;
	}
	void SetRow(int it, int row) {
		TheRow[it] = row-1;
	}
	void Run() {
		map<int, int> cardcount;
		int counttwos = 0;
		int sampleans = 0;
		for (int it=0;it<2;++it) {
			int row=TheRow[it];
			for (int i=0; i<4; ++i)
				for (int j=0; j<4; ++j) {
					int card = Arr[it][i][j];
					if (i!=row)
						continue;
					if (++cardcount[card] == 2) {
						++counttwos;
						sampleans = card;
					}
				}
		}
		char samplestr[30];
		itoa(sampleans, samplestr, 10);
		cout << "Case #" << GameNum << ": " << (counttwos == 0 ? "Volunteer cheated!" : (counttwos == 1 ? samplestr : "Bad magician!" )) << endl;
	}
};


int main(int argc, const char* argv[]) {
	int T;
	cin >> T;
	for (int gi=1; gi<=T; ++gi) {
		Game gm(gi);
		for (int it=0; it<2; ++it) {
			int row;
			cin >> row;
			for (int i=0; i<4; ++i)
				for (int j=0; j<4; ++j) {
					int card;
					cin >> card;
					gm.SetCard(it, i, j, card);
				}
			gm.SetRow(it, row);
		}
		gm.Run();
	}
	return 0;
}
