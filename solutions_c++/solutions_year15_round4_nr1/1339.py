/*	Arkadiusz Wróbel - metsuryuu
 *
 *	Konkurs: Google Code Jam 2015
 *	Zadanie: 
 */
#include <cstdio>
#include <iostream>

#include <algorithm>
#include <cmath>
#include <cstring>

#include <vector>
#include <set>
#include <map>
#include <list>
#include <queue>
#include <deque>

using namespace std;

typedef long long LL;
typedef unsigned long long ULL;
typedef pair<int, int> PII;

typedef vector<int> VI;
typedef vector<LL> VLL;
typedef vector<double> VD;
typedef vector<string> VS;
typedef vector<PII> VPII;
typedef vector<VI> VVI;

#define REP(I, N) for(int I = 0; I < (N); ++I)
#define FOR(I, M, N) for(int I = (M); I <= (N); ++I)
#define FORD(I, M, N) for(int I = (M); I >= (N); --I)
//#define FOREACH(IT, CON) for(__typeof((CON).begin()) IT = (CON).begin(); IT != (CON).end(); ++IT)

#define ST first
#define ND second
#define MP make_pair
#define PB push_back
#define SIZE(CON) ((int)(CON).size())
#define ALL(CON) (CON).begin(), (CON).end()

const int INF = 1000000000;
const LL INFLL = 1000000000000000000LL;

//######################################################################

const int wekt[][2] = {
	{0, 1},
	{-1, 0},
	{0, -1},
	{1, 0}
};

int n, m;
int t[1024][1024];

bool check(int y, int x, const int kier) {
	y += wekt[kier][0];
	x += wekt[kier][1];
	if (y <= 0 || y > n || x <= 0 || x > m) {
		return true;
	}
	while (t[y][x] == -1) {
		y += wekt[kier][0];
		x += wekt[kier][1];
		//printf("%d : %d %d\n", kier, y, x);
		if (y <= 0 || y > n || x <= 0 || x > m) {
			return true;
		}
	}
	return false;
}


int make() {
	int res = 0;
	FOR(y, 1, n) {
		FOR(x, 1, m) {
			if (t[y][x] >= 0 && check(y, x, t[y][x])) {
				int ile = 0;
				REP(i, 4) {
					if (check(y, x, i)) {
						++ile;
					}
				}
				if (ile >= 4) {
					return -1;
				}
				++res;
			}
		}
	}
	return res;
}


int main()
{
	int T;
	scanf("%d", &T);
	FOR(testCounter, 1, T){
		//wej
		scanf("%d%d", &n, &m);
		FOR(i, 1, n) {
			FOR(j, 1, m) {
				char c;
				scanf(" %c", &c);
				t[i][j] = -1;
				if (c == '>') t[i][j] = 0;
				if (c == '^') t[i][j] = 1;
				if (c == '<') t[i][j] = 2;
				if (c == 'v') t[i][j] = 3;
			}
		}
		//printf("%d %d %d %d\n", check(2, 1, 0), check(2, 1, 1), check(2, 1, 2), check(2, 1, 3));
		//prog
		int wynik = make();
		//wyj
		if (wynik >= 0) {
			printf("Case #%d: %d\n", testCounter, wynik);
		} else {
			printf("Case #%d: IMPOSSIBLE\n", testCounter);
		}
	}
	return 0;
}
