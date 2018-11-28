//	Problem X

const bool debug=false;

#include <iostream>
#include <cstdio>
#include <iomanip>
#include <sstream>
#include <cmath>
#include <numeric>
#include <algorithm>
#include <functional>
#include <cstring>
#include <cstdlib>
#include <cstdarg>
#include <utility>
#include <cassert>
#include <ctime>
#include <string>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <bitset>
#include <deque>
#include <queue>
#include <stack>

#define TIMES(n) for (int i=0; i<(n); ++i)
#define REPE(i,s,t) for (int (i)=(s); (i)<=(t); ++(i))
#define RESET(a) memset((a), 0, sizeof((a)))
#define P(x, ...) printf((x), ##__VA_ARGS__)
#define D(x, ...) if (debug) printf((x), ##__VA_ARGS__)
#define MP(x, y) make_pair((x), (y))

const int INF = 0x3F3F3F3F; // or (unsigned)(-1)>>1
int caseI = 0, caseD = -1;

using namespace std;

//void P(char *f, ...) {va_list v; va_start(v, f); vprintf(f, v); va_end(v);}
//void D(char *f, ...) {if (!debug) return; va_list v; va_start(v, f); vprintf(f, v); va_end(v);}


/*

Sample Input:



Sample Output:


*/

const int maxN = 1005, maxM = 1005;

typedef pair<int, int> ii;
typedef vector<vector<ii> > graph;

class Qs {
	int n, m, k;
	char game[maxN][maxN];
	int o[2][maxN]; // {horz, vert}
	int x[2][maxN];
	int t[2][maxN];

	int chess;
	//int e_n[maxN];

public:
	Qs() {
		RESET(game);
		RESET(o);
		RESET(x);
		RESET(t);
		chess = 0;
	}

	bool input() {

		TIMES(4) REPE(j, 0, 3) {
			scanf(" %c", &game[i][j]);
			if (game[i][j] != '.')
				++chess;
			D("%c", game[i][j]);
		}

		return true;
	}

	void solve() {

		bool xWin = false, oWin = false;
		
		TIMES(4) REPE(j, 0, 3) {
			o[0][i] += (game[i][j] == 'O');
			x[0][i] += (game[i][j] == 'X');
			t[0][i] += (game[i][j] == 'T');

			o[1][j] += (game[i][j] == 'O');
			x[1][j] += (game[i][j] == 'X');
			t[1][j] += (game[i][j] == 'T');
		}

		TIMES(4) {
			if ( (o[0][i] == 4 || (o[0][i] == 3 && t[0][i] == 1)) ||
				(o[1][i] == 4 || (o[1][i] == 3 && t[1][i] == 1)) )
				oWin = true;
			if ( (x[0][i] == 4 || (x[0][i] == 3 && t[0][i] == 1)) ||
				(x[1][i] == 4 || (x[1][i] == 3 && t[1][i] == 1)) )
				xWin = true;

			D(">> o[0][%d] = %d\n", i, o[0][i]);
			D(">> o[1][%d] = %d\n", i, o[1][i]);
			D(">> x[0][%d] = %d\n", i, x[0][i]);
			D(">> x[1][%d] = %d\n", i, x[1][i]);
		}

		{
			int xCnt = 0, oCnt = 0, tCnt = 0;

			TIMES(4) {
				xCnt += (game[i][i] == 'X');
				oCnt += (game[i][i] == 'O');
				tCnt += (game[i][i] == 'T');
			}

			D(">> %d %d %d\n", xCnt, oCnt, tCnt);

			if (xCnt == 4 || (xCnt == 3 && tCnt == 1))
				xWin = true;

			if (oCnt == 4 || (oCnt == 3 && tCnt == 1))
				oWin = true;
		}

		{
			int xCnt = 0, oCnt = 0, tCnt = 0;

			TIMES(4) {
				xCnt += (game[i][3-i] == 'X');
				oCnt += (game[i][3-i] == 'O');
				tCnt += (game[i][3-i] == 'T');
			}

			D(">> %d %d %d\n", xCnt, oCnt, tCnt);

			if (xCnt == 4 || (xCnt == 3 && tCnt == 1))
				xWin = true;

			if (oCnt == 4 || (oCnt == 3 && tCnt == 1))
				oWin = true;
		}

		P("Case #%d: ", caseI);

		if (xWin && oWin)
			P("Draw\n");
		else if (xWin)
			P("X won\n");
		else if (oWin)
			P("O won\n");
		else if (chess == 16)
			P("Draw\n");
		else
			P("Game has not completed\n");

	}
};

void pre_process() {
	freopen("qA-large.in", "r", stdin);
	freopen("qA-large.out", "w", stdout);
	scanf("%d", &caseD);
}

int main() {
	Qs *p = new Qs;
	pre_process();
	while ((++caseI|1) && caseD-- && p->input()) {
		p->solve();
		delete p;
		p = new Qs;
	}
	delete p;
	return 0;
}
