#define _CRT_SECURE_NO_DEPRECATE
#pragma comment(linker, "/STACK:167772160000")
#include <iostream>
#include <fstream>
#include <cstdio>
#include <stdio.h>
#include <cstdlib>
#include <stdlib.h>
#include <string>
#include <list>
#include <fstream>
#include <algorithm>
#include <cmath>
#include <map>
#include <vector>
#include <iomanip>
#include <queue>
#include <deque>
#include <set>
#include <stack>
#include <sstream>
#include <assert.h>
#include <functional>
#include <climits>
#include <cstring>
typedef long long ll;
typedef std::pair<ll, ll> pll;
typedef std::pair<int, int> pii;
//typedef std::pair<long double,long double> pdd;
#define forn(N)          for(int i = 0; i<(int)N; i++)
#define fornj(N)         for(int j = 0; j<(int)N; j++)
#define fornk(N)         for(int k = 0; k<(int)N; k++)
#define forn1(N)          for(int i = 1; i<=(int)N; i++)
#define fornj1(N)         for(int j = 1; j<=(int)N; j++)
#define fornk1(N)         for(int k = 1; k<=(int)N; k++)
#define PI 3.1415926535897932384626433
#define v vector
#define ll long long
#define print(n) printf("%d ", (n));
#define printll(n) printf("%I64d", (n));
#define printline() printf("\n");
#define read(n) scanf("%d", &n);
#define read2(n, m) scanf("%d%d", &n, &m);
#define readll(n) scanf("%I64d", &n);
#define mp make_pair
using namespace std;










bool used[1100][1100];
bool fail;
char answer[1100][1100];
bool taken[1100][1100];
int R, C;

pii vectors[4];
bool visnow[1100][1100];
bool connect(pii now, int dir, pii goal) {
	if (fail)return 0;
	pii nxt = now;
	if (now == goal)return 1;
	dir = (dir + 2) % 4;
	bool W = 0;
	fornk(3) {
		dir = (dir + 1) % 4;
		nxt = now;
		nxt.first += vectors[dir].first;
		nxt.second += vectors[dir].second;
		pii cell = pii(min(now.first, nxt.first), min(now.second, nxt.second));
		if (nxt.first < 0 || nxt.second < 0 || nxt.first > R || nxt.second > C)continue;
		char ch = '/';
		if (dir % 2 == 1)ch = '\\';
		if (!(taken[cell.first][cell.second] && answer[cell.first][cell.second] == ch))
			if ((used[nxt.first][nxt.second] || taken[cell.first][cell.second]))continue;
		if (visnow[cell.first][cell.second])continue;

		bool prevu = used[nxt.first][nxt.second];
		bool prevt = taken[cell.first][cell.second];
		char preva = answer[cell.first][cell.second];
		visnow[cell.first][cell.second] = 1;
		used[nxt.first][nxt.second] = 1;
		taken[cell.first][cell.second] = 1;
		answer[cell.first][cell.second] = ch;
		if (connect(nxt, dir, goal)) {
			visnow[cell.first][cell.second] = 0;
			return 1;
		}
		visnow[cell.first][cell.second] = 0;
		used[nxt.first][nxt.second] = prevu;
		taken[cell.first][cell.second] = prevt;
		answer[cell.first][cell.second] = preva;
	}
	return 0;
}



int with[4000];
bool vis[4000];

pii getcoord(int a) {
	pii ret = pii(0, 0);
	ret.second += min(C, a);
	a -= min(C, a);
	ret.first += min(R, a);
	a -= min(R, a);
	ret.second -= min(C, a);
	a -= min(C, a);
	ret.first -= min(R, a);
	a -= min(R, a);
	return ret;
}


void con(int a, int b) {
	if (vis[a])return;
	if (a > b)swap(a, b);
	vis[a] = vis[b] = 1;
	for (int i = a + 1; i < b; i++)con(i, with[i]);
	pii st = getcoord(a);
	pii en = getcoord(b);
	if (st == pii(0, 0))st.first++;
	else if (st.first == 0)st.second--;
	else if (st.second == C)st.first--;
	else if (st.first == R)st.second++;
	else st.first++;
	int dir;
	if (st.first == 0 || st.second==0)dir = 1;
	else dir = 3;

	fail |= !connect(st, dir, en);

}


int main()
{
#if defined(_DEBUG) || defined(_RELEASE)
	freopen("input.txt", "r", stdin); freopen("output.txt", "w", stdout);
#else
	//(File".in", "r", stdin); freopen(File".out", "w", stdout);
	freopen("input.txt", "r", stdin); freopen("output.txt", "w", stdout);
#endif
	
	vectors[0] = pii(-1, 1);
	vectors[1] = pii(1, 1);
	vectors[2] = pii(1, -1);
	vectors[3] = pii(-1, -1);
	int T; cin >> T;
	fornk1(T) {
		if (k == 82)
			int asdf = 15;
		fail = 0;
		cin >> R >> C;
		forn(R)fornj(C)visnow[i][j] = 0;
		forn(20)fornj(20)answer[i][j] = 0;
		forn(R + C) {
			int a, b; cin >> a >> b;
			with[a] = b;
			with[b] = a;

		}
		forn(R + 10)fornj(C + 10)taken[i][j] = used[i][j] = 0;
		forn1(3 * (R + C))vis[i] = 0;
		forn1(2 * (R + C))con(i, with[i]);
		forn(R)fornj(C)if (!taken[i][j])answer[i][j] = '/';

		cout << "Case #" << k << ":\n";
		if (fail) {
			cout << "IMPOSSIBLE\n";
			continue;
		}
		forn(R) {
			fornj(C)cout << answer[i][j];
			cout << endl;
		}
		
	}

	return 0;

}
