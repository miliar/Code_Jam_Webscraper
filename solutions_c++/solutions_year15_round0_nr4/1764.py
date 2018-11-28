#include <bits/stdc++.h>
using namespace std;

int t;
int x, r, c;
int mapa[10][10][10];

void marca (){
	mapa[1][1][2] = 1;
	mapa[1][1][3] = 1;
	mapa[1][1][4] = 1;
	mapa[1][2][3] = 1;
	mapa[1][2][4] = 1;
	mapa[1][3][2] = 1;
	mapa[1][3][3] = 1;
	mapa[1][3][4] = 1;
	mapa[1][4][3] = 1;
	mapa[1][4][4] = 1;
	mapa[2][1][3] = 1;
	mapa[2][1][4] = 1;
	mapa[2][2][3] = 1;
	mapa[2][2][4] = 1;
	mapa[2][3][4] = 1;
	mapa[2][4][3] = 1;
	mapa[2][4][4] = 1;
	mapa[3][1][2] = 1;
	mapa[3][1][3] = 1;
	mapa[3][1][4] = 1;
	mapa[3][2][4] = 1;
	mapa[3][3][2] = 1;
	mapa[3][3][4] = 1;
	mapa[4][1][3] = 1;
	mapa[4][1][4] = 1;
	mapa[4][2][3] = 1;
	mapa[4][2][4] = 1;
	mapa[4][4][3] = 1;
}

int main (){

	freopen ("D-small-attempt0.in", "r", stdin);
	freopen ("sol.out", "w", stdout);
	marca ();
	scanf ("%d", &t);
	int cont = 0;
	while (t--){
		cont++;
		scanf ("%d%d%d", &x, &r, &c);
		if (mapa[r][c][x])
			printf ("Case #%d: RICHARD\n", cont);
		else
			printf ("Case #%d: GABRIEL\n", cont);
	}
	return 0;
}