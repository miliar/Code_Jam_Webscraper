#include <stdio.h>
#include <functional>
#include <bitset>
#include <math.h>
#include <time.h>
#include <stdlib.h>
#include <algorithm>
#include <iostream>
#include <string>
#include <vector>
#include <list>
#include <set>
#include <map>
#include <sstream>
#include <queue>
#include <bitset>
#include <string.h>
using namespace std;

int R, C, M;
bool rot;
char field[60][60];

void readCase()
{
	scanf("%d %d %d", &R, &C, &M);
	rot = false;
	if(R > C) {
		swap(R, C);
		rot = true;
	}
	memset(field, 0, sizeof(field));
	for(int i = 0; i < R; i++) {
		for(int j = 0; j < C; j++) {
			field[j][i] = '*';
		}
	}
}

void clear(int x, int y) 
{
	field[x][y] = '.';
}

void printCase()
{
	int bombs = 0;
	if(!rot) {
		for(int i = 0; i < R; i++) {
			printf("\n");
			for(int j = 0; j < C; j++) {
				char c = field[j][i];
				printf("%c", c);
				if(c == '*') bombs++;
			}
		}
	} else {
		for(int i = 0; i < C; i++) {
			printf("\n");
			for(int j = 0; j < R; j++) {
				char c = field[i][j];
				printf("%c", c);
				if(c == '*') bombs++;
			}
		}
	}
}

void printImpossible()
{
	printf("\nImpossible");
}

void solve()
{
	int F = R * C - M;

	if(F == 0) {
		printCase();
		return;
	}

	field[0][0] = 'c';
	F -= 1;

	if(R == 1) {
		for(int i = 1; i < C && F > 0; i++) {
			clear(i, 0);
			F--;
		}
		printCase();
		return;
	}

	if(0 < F) {
		if(F < 3) {
			printImpossible();
			return;
		}	
		clear(0, 1);
		clear(1, 0);
		clear(1, 1);
		F -= 3;
	}

	if( F > 0 ) {
		if(F < 2) {
			printImpossible();
			return;
		}
		clear(2, 0);
		clear(2, 1);
		F -= 2;
	}


	if(R > 2) {
		if(F > 0) {
			if(F < 2) {
				printImpossible();
				return;
			} 
			clear(0, 2);
			clear(1, 2);
			F -= 2;
		
			if(F % 2) {
				clear(2, 2);
				F--;
			}
		}
	}

	for(int i = 3; i < C && F >= 2; i++, F-=2) {
		clear(i, 0);
		clear(i, 1);
	}

	for(int j = 3; j < R && F >= 2; j++, F-=2) {
		clear(0, j);
		clear(1, j);
	}

	for(int j = 2; j < R && F > 0; j++) {
		for(int i = 2; i < C && F > 0; i++) {
			if(i == 2 && j == 2 && field[i][j] == '.') continue;
			clear(i, j);
			F--;
		}
	}

	if(F > 0) {
		printImpossible();
	} else {
		printCase();
	}
}

int main()
{
	//string fname = "./test/C-example.in";
	//string fname = "./test/C-small-attempt0.in";
	string fname = "./test/C-large.in";
	//string fname = "./test/C-large-2.in";

	freopen(fname.c_str(),"r",stdin);freopen((fname+".out").c_str(),"w",stdout);

	int analizeCase = -1;
	
	int T;
	scanf("%d", &T);
	for(int tCase = 1; tCase <= T; tCase++) {
		printf("Case #%d: ", tCase);
		readCase();
		if(analizeCase < 0 || analizeCase == tCase) solve();
		printf("\n");
		fflush(stdout);
		fprintf(stderr, "Done %d %%     \r", 100 * tCase / T );
	}
	return 0;
}

