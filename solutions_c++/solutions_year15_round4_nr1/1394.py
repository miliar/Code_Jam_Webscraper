// Problem A

#include <iostream>
#include <stdio.h>
#include <fstream>
#include <iomanip>
#include <cassert>
#include <vector>
#include <algorithm>
#include <set>
#include <string.h>
#include <map>
#include <queue>
#include <stack>

#define pb push_back
#define mp make_pair
#define MAXN 120

using namespace std;

typedef long long int ll;
typedef pair<int, int> ii;
typedef vector<int> vi;
typedef set<int> si;
typedef vector<ii> vii;

void solve() {
	int R, C;
	cin >> R >> C;
	char tab[MAXN][MAXN], pr;
	int su[MAXN][MAXN], giu[MAXN][MAXN], dx[MAXN][MAXN], sx[MAXN][MAXN];
	pr = getchar();
	for (int i=0; i<R; i++) {
		for (int j=0; j<C; j++)
			tab[i][j] = getchar();
		pr = getchar();
	}
	
	//for (int i=0; i<R; i++)
	//	for (int j=0; j<C; j++) cout << tab[i][j];
	//cout << endl;
	
	// riempio su/giu/dx/sx
	for (int i=0; i<R; i++) {
		int s = 0;
		for (int j=0; j<C; j++) {
			sx[i][j] = s;
			if (tab[i][j] !='.') s++;
		}
		for (int j=0; j<C; j++) {
			if (tab[i][j] != '.')	dx[i][j] = s-1-sx[i][j];
			else dx[i][j] = s-sx[i][j];
		}
	}
	
	for (int j=0; j<C; j++) {
		int s = 0;
		for (int i=0; i<R; i++) {
			su[i][j] = s;
			if (tab[i][j] !='.') s++;
		}
		for (int i=0; i<R; i++) {
			if (tab[i][j] != '.')	giu[i][j] = s-1-su[i][j];
			else giu[i][j] = s-su[i][j];
		}
	}
	
	// Controllo se è possibile
	for (int i=0; i<R; i++)
		for (int j=0; j<C; j++)
			if (dx[i][j] == 0 && sx[i][j] == 0 && su[i][j] == 0 && giu[i][j] == 0 && tab[i][j] != '.') {
				cout << "IMPOSSIBLE\n";
				return;
			}
			
	// Controllo quante frecce devo cambiare
	int sol = 0;
	for (int i=0; i<R; i++)
		for (int j=0; j<C; j++) {
			if (tab[i][j] == '^' && su[i][j] == 0) sol++;
			else if (tab[i][j] == '>' && dx[i][j] == 0) sol++;
			else if (tab[i][j] == 'v' && giu[i][j] == 0) sol++;
			else if (tab[i][j] == '<' && sx[i][j] == 0) sol++;
		}
		
	cout << sol << endl;
			
}

int main() {
	int T;
	cin >> T;
	for (int t=1; t<=T; t++) {
		cout << "Case #" << t << ": ";
		solve();
	}
	
	return 0;
}
