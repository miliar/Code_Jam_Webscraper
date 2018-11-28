#include <algorithm>
#include <bitset>
#include <cassert>
#include <cctype>
#include <cfloat>
#include <climits>
#include <cmath>
#include <complex>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <deque>
#include <functional>
#include <iostream>
#include <limits>
#include <list>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <utility>
#include <vector>

using namespace std;

//#define NDEBUG
#ifdef NDEBUG
#define DEBUG if (false)
#else
#define DEBUG if (true)
#endif

#pragma GCC diagnostic warning "-Wall"
#define WRITE(x) DEBUG { cout << x << endl; }
#define WATCH(x) DEBUG { cout << #x << " = " << x << endl; }
#define ALL(x) (x).begin(), (x).end()
#define FORN(i, a, b) for(typeof(b) i = (a); i < (b); i++)
#define FOREACH(i, c) for(typeof((c).begin()) i = (c).begin(); i != (c).end(); i++)

bool done;
char m[10][10];
int checkLine(){
	int no;
	int nx;
	int nt;
	FORN(i, 0, 4){
		no = 0;
		nx = 0;
		nt = 0;
		FORN(j, 0, 4){
			switch(m[i][j]){
				case 'X':
					nx++;
					break;
				case 'O':
					no++;
					break;
				case 'T':
					nt++;
					break;
				case '.':
					done = false;
					break;
			}
		}
		if ((nx == 3 && nt == 1) || (nx==4)) return 1;
		if ((no == 3 && nt == 1) || (no==4)) return -1;
	}
	return 0;
}

	

int checkDiag(){
	int no;
	int nx;
	int nt;
		no = 0;
		nx = 0;
		nt = 0;
	FORN(i, 0, 4){
			switch(m[i][i]){
				case 'X':
					nx++;
					break;
				case 'O':
					no++;
					break;
				case 'T':
					nt++;
					break;
			}
	}
	if ((nx == 3 && nt == 1) || (nx==4)) return 1;
	if ((no == 3 && nt == 1) || (no==4)) return -1;
		no = 0;
		nx = 0;
		nt = 0;

	FORN(i, 0, 4){
			switch(m[i][3-i]){
				case 'X':
					nx++;
					break;
				case 'O':
					no++;
					break;
				case 'T':
					nt++;
					break;
			}
	}
	if ((nx == 3 && nt == 1) || (nx==4)) return 1;
	if ((no == 3 && nt == 1) || (no==4)) return -1;
	return 0;
}



int checkCol(){
	int no;
	int nx;
	int nt;
	FORN(i, 0, 4){
		no = 0;
		nx = 0;
		nt = 0;
		FORN(j, 0, 4){
			switch(m[j][i]){
				case 'X':
					nx++;
					break;
				case 'O':
					no++;
					break;
				case 'T':
					nt++;
					break;
			}
		}
		if ((nx == 3 && nt == 1) || (nx==4)) return 1;
		if ((no == 3 && nt == 1) || (no==4)) return -1;
	}
	return 0;
}

void printWinner(int w){
	if (w == 1)
		puts("X won");
	if (w == -1)
		puts("O won");
}

int main(){
	//Descomente para acelerar cin
	ios::sync_with_stdio(false);
	int t;
	scanf("%d", &t);
	
	FORN(tg, 0, t){
		FORN(i, 0, 4) scanf("%s", m[i]);
//		FORN(i, 0, 4) printf("%s\n", m[i]);
		done = true;

		printf("Case #%d: ", tg+1);
		int winner;
		winner = checkLine();
		if (winner != 0){
			printWinner(winner);
			continue;
		}
		winner = checkCol();
		if (winner != 0){
			printWinner(winner);
			continue;
		}
		winner = checkDiag();
		if (winner != 0){
			printWinner(winner);
			continue;
		}
		if (done)
			puts("Draw");
		else
			puts("Game has not completed");
	}
	scanf("%s", m[0]);
	return 0;
}
