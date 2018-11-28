// A.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <cstdio>
#include <vector>
#include <algorithm>

using namespace std;

int T;
int r, c;
char mapa[111][111];

int hledej(int X, int Y, int smer, bool R){
	int x = X; int y = Y;
	bool povedlo = false;
	if (smer == 1){
		while (x < r - 1){
			x++;
			if (mapa[x][y] != '.'){ povedlo = true; break; }
		}
		if (povedlo && R){ return 0; }
		if (povedlo){ return 1; }
		if (!R) { return 10; }
		else {
			int ans = hledej(X, Y, 2, false);
			ans = min(ans, hledej(X, Y, 3, false));
			ans = min(ans, hledej(X, Y, 4, false));
			return ans;
		}
	}
	else if (smer == 2){
		while (x > 0 ){
			x--;
			if (mapa[x][y] != '.'){ povedlo = true; break; }
		}
		if (povedlo && R){ return 0; }
		if (povedlo){ return 2; }
		if (!R) { return 10; }
		else {
			int ans = hledej(X, Y, 1, false);
			ans = min(ans, hledej(X, Y, 3, false));
			ans = min(ans, hledej(X, Y, 4, false));
			return ans;
		}
	}
	else if (smer == 3){
		while ( y > 0){
			y--;
			if (mapa[x][y] != '.'){ povedlo = true; break; }
		}
		if (povedlo && R){ return 0; }
		if (povedlo){ return 3; }
		if (!R) { return 10; }
		else {
			int ans = hledej(X, Y, 1, false);
			ans = min(ans, hledej(X, Y, 2, false));
			ans = min(ans, hledej(X, Y, 4, false));
			return ans;
		}
	}
	else if (smer == 4){
		while (y < c - 1){
			y++;
			if (mapa[x][y] != '.'){ povedlo = true; break; }
		}
		if (povedlo && R){ return 0; }
		if (povedlo){ return 4; }
		if (!R) { return 10; }
		else {
			int ans = hledej(X, Y, 1, false);
			ans = min(ans, hledej(X,Y, 3, false));
			ans = min(ans, hledej(X, Y, 2, false));
			return ans;
		}
	}
}



int _tmain(int argc, _TCHAR* argv[])
{
	freopen("vstup.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	char znaky[5];
	znaky[0] = '.';
	znaky[1] = 'v';
	znaky[2] = '^';
	znaky[3] = '<';
	znaky[4] = '>';

	scanf("%d", &T);
	for (int t = 1; t <= T; t++){
		scanf("%d %d", &r, &c);
		for (int i = 0; i <=r; i++){
			for (int j = 0; j <= c; j++){
				mapa[i][j] = '.';
			}
		}
		for (int i = 0; i < r; i++){
			scanf("%s", mapa[i]);
		}



		//if (r == 1 && c == 1 && mapa[0][0] != '.'){ printf("Case %d: IMPOSSIBLE\n"); continue; }
		int rslt = 0;
		bool imposible = false;
		for (int i = 0; i < r; i++){
			for (int j = 0; j < c; j++){
				if (mapa[i][j] == 'v'){
					int ans = hledej(i, j, 1, true);
					if (ans >= 10){ imposible = true; }
					else if (ans != 0){ mapa[i][j] = znaky[ans]; rslt++; }
				}
				else if (mapa[i][j] == '^'){
					int ans = hledej(i, j, 2, true);
					if (ans >= 10){ imposible = true; }
					else if (ans != 0){ mapa[i][j] = znaky[ans]; rslt++; }
				}
				else if (mapa[i][j] == '<'){
					int ans = hledej(i, j, 3, true);
					if (ans >= 10){ imposible = true; }
					else if (ans != 0){ mapa[i][j] = znaky[ans]; rslt++; }
				}
				else if (mapa[i][j] == '>'){
					int ans = hledej(i, j, 4, true);
					if (ans >= 10){ imposible = true; }
					else if (ans != 0){ mapa[i][j] = znaky[ans]; rslt++; }
				}
			}
		}
		if (imposible){
			printf("Case #%d: IMPOSSIBLE\n",t);
		}
		else{
			printf("Case #%d: %d\n",t,rslt);

		}

	}
	return 0;
}

