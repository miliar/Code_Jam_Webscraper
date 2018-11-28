#include <string>
#include <vector>
#include <vector>
#include <stack>
#include <queue>
#include <set>
#include <map>
#include <iostream>
#include <sstream>
#include <algorithm>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <assert.h>
#include <math.h>
#include <climits>

using namespace std;

typedef pair<int,int> p_int;

char board[4][4];
p_int arr[10][4];

void build_arr()
{
	int i,j;

	for(i=0; i<4; i++) {
		for(j=0; j<4; j++) {
			arr[i][j] = make_pair(i, j);
		}
	}

	for(i=0; i<4; i++) {
		for(j=0; j<4; j++) {
			arr[i+4][j] = make_pair(j, i);
		}
	}
	
	for(i=0; i<4; i++)
		arr[8][i] = make_pair(i, i);
	for(i=0; i<4; i++)
		arr[9][i] = make_pair(i, 3-i);

	for(i=0; i<10; i++) {
		for(j=0; j<4; j++)
			printf("(%d,%d)", arr[i][j].first, arr[i][j].second);
		printf("\n");
	}
}

string check()
{
	int x,o,t,d,i,j;

	d = 0;

	for(i=0; i<10; i++) {
		x = o = t = 0;

		for(j=0; j<4; j++) {
			switch (board[arr[i][j].first][arr[i][j].second]) {
			case 'X':
				x++;
				break;

			case 'O':
				o++;
				break;

			case 'T':
				t++;
				break;

			case '.':
				d++;
				break;

			default:
				break;
			}
		}

		if (x == 4 || (x == 3 && t == 1) )
			return "X won";
	
		if (o == 4 || (o == 3 && t == 1) )
			return "O won";
	}

	if (d > 0)
		return "Game has not completed";

	return "Draw";
}

void print_b()
{
	int i,j;

	printf("\n");
	for (i=0; i<4; i++) {
		for (j=0; j<4; j++)
			printf("%c", board[i][j]);
		printf("\n");
	}

}

int main()
{
	int T, t, i, j, k;

	bool dot;
	char ctmp;

	FILE *out = fopen("out.txt", "w");

	FILE *f = fopen("a.txt", "r");
	if( !f ) {
		printf("open file fail");
		return 0;
	}

	build_arr();

	fscanf(f, "%d ", &T);

	for( i=0; i<T; i++) {	

		for(j=0; j<4; j++) 
		{
			for (k=0; k<4; k++) 
			{
				fscanf(f, "%c", &board[j][k]);				
			}
			fscanf(f, "%c", &ctmp);
		}
		fscanf(f, "%c", &ctmp);

		print_b();

		fprintf(out, "Case #%d: %s\n", i+1, check().c_str());		
	}
}