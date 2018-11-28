// File Name: A.cpp
// Author: YangYue
// Created Time: 六  4/13 18:46:43 2013
//headers 
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <algorithm>
#include <cstring>
#include <cmath>
#include <ctime>
#include <string>
#include <queue>
#include <set>
#include <map>
#include <iostream>
#include <vector>

using namespace std;

typedef long long LL;
typedef unsigned long long ULL;
typedef pair<int,int> PII;
typedef pair<double,double> PDD;
typedef pair<LL, LL>PLL;
typedef pair<LL,int>PLI;

#define lch(n) ((n<<1))
#define rch(n) ((n<<1)+1)
#define lowbit(i) (i&-i)
#define sqr(x) ((x)*(x))
#define fi first
#define se second
#define MP make_pair
#define PB push_back

const int MaxN = 200005;
const double eps = 1e-7;
const double DINF = 1e100;
const int INF = 1000000006;
const LL LINF = 1000000000000000005ll;

int win;
char MAP[20][20];
void solve() {

	for (int x = 0; x < 4; ++x){
		int cnt = 0;
		if (MAP[x][0] == '.') continue;
		for (int y = 0; y < 4 && (MAP[x][y] == MAP[x][0]); ++y) ++cnt;
		if (cnt == 4) {
			if (MAP[x][0] == 'O') win = 0;
			else win = 1;
		}
	}
	for (int y = 0; y < 4; ++y){
		int cnt = 0;
		if (MAP[0][y] == '.') continue;
		for (int x = 0; x < 4 && (MAP[x][y] == MAP[0][y]); ++x) ++cnt;
		if (cnt == 4) {
			if (MAP[0][y] == 'O') win = 0;
			else win = 1;
		}
	}
	int cnt = 0;
	if (MAP[0][0] != '.')
		for (int x = 0, y = 0; x < 4 && (MAP[x][y] == MAP[0][0]); ++x, ++y) ++cnt;
	if (cnt == 4) {
		if (MAP[0][0] == 'O') win = 0;
		else win = 1;
	}
	cnt = 0;
	if (MAP[3][0] != '.')
		for (int x = 3, y = 0; x >= 0 && (MAP[x][y] == MAP[3][0]); --x, ++y) ++cnt;
	if (cnt == 4) {
		if (MAP[3][0] == 'O') win = 0;
		else win = 1;
	}
}
int main()
{
	//freopen("in","r",stdin);
	//freopen("out","w",stdout);

	int cas = 0;
	int cases; cin >> cases;
	while (cases--) {
		for (int i = 0; i < 4; ++i) scanf("%s", MAP[i]);
		printf("Case #%d: ", ++cas);

		win = -1;
		int sum = 0;
		int x = -1, y = -1;
		for (int i = 0; i < 4; ++i)
		for (int j = 0; j < 4; ++j) {
			if (MAP[i][j] == '.') ++sum;
			if (MAP[i][j] == 'T') x = i, y = j;
		}
		if (x != -1) {
			MAP[x][y] = 'X';
			solve();
			MAP[x][y] = 'O';
			solve();
		} else solve();


		if (win != -1) {
			if (win == 0) puts("O won");
			else puts("X won");
		} else {
			if (!sum) puts("Draw");
			else puts("Game has not completed");
		}

	}
	return 0;
}

// hehe ~


