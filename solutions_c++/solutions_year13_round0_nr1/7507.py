#include <iostream>
//#include <ifstream>
#include <vector>
#include <queue>
using namespace std;

#define FOR(i,a,b) for(int i = a; i < b; i++)
#define REP(i,n) FOR(i, 0, n)

const int X = 0, O = 1;
//string s[4];
char s[5][5];

bool incomplete() {
	REP(i,4) REP(j,4) if(s[i][j] == '.') return true;
	return false;
}

#define isPlayerCoin(c, p) ((c == 'T') || ((p == X) ? (c == 'X') : (c == 'O')))

bool wins(int p) {
	REP(i,4) {
		int cnt = 0;
		REP(j, 4) cnt += isPlayerCoin(s[i][j], p);
		if(cnt == 4) return true;
	}
	REP(i,4) {
		int cnt = 0;
		REP(j, 4) cnt += isPlayerCoin(s[j][i], p);
		if(cnt == 4) return true;
	}
	if(isPlayerCoin(s[0][0], p) + isPlayerCoin(s[1][1], p) + isPlayerCoin(s[2][2], p) + isPlayerCoin(s[3][3], p) == 4) return true;
	if(isPlayerCoin(s[0][3], p) + isPlayerCoin(s[1][2], p) + isPlayerCoin(s[2][1], p) + isPlayerCoin(s[3][0], p) == 4) return true;	

	return false;
}

int main() {
	//ifstream fin("a.small.in");
	//ifstream fout("a.small.out");
	int n;
	cin >> n;
	FOR(kase, 1, n+1) {
		//char buf[10][10];
		REP(i,4) {
			scanf("%s", s[i]);
			//s[i] = buf;
		}
		cout << "Case #" << kase << ": ";
		if(wins(X)) cout << "X won";
		else if(wins(O)) cout << "O won";
		else if(incomplete()) cout << "Game has not completed";
		else cout << "Draw";
		cout << endl;
	}
	//fin.close();
	//fout.close();
}