#include <cstdio>
#include <iostream>
using namespace std;

int main(void) {
	int testCases, row, col, mine;
	int i, j, t, r, c, m, impossible;
//	int impossibleCount=0;
	char grid[64][64];
	cin >> testCases;
	for (t=1; t<=testCases; t++) {
		cin >> row >> col >> mine;
		for (i=0; i<row; i++) for (j=0; j<col; j++) grid[i][j] = '.';
	//	printf("case %d, %d %d %d\n", t, row, col, mine);
		impossible = 0;
		if (row == 1) {
			for (i=0; i<mine; i++) grid[0][i] = '*';
			grid[0][col-1] = 'c';
		}
		else if (col == 1) {
			for (i=0; i<mine; i++) grid[i][0] = '*';
			grid[row-1][0] = 'c';
		}
		else if (row == 2) {
			if (mine==row*col-1) {
				for (i=0; i<row; i++) for (j=0; j<col; j++) grid[i][j] = '*';
				grid[0][0] = 'c';
			}
			else if ((mine%2) || (mine==row*col-2)) impossible = 1;
			else {
				for (i=0; i<mine/2; i++) grid[0][i] = grid[1][i] = '*';
				grid[0][col-1] = 'c';
			}
		}
		else if (col == 2) {
			if (mine==row*col-1) {
				for (i=0; i<row; i++) for (j=0; j<col; j++) grid[i][j] = '*';
				grid[0][0] = 'c';
			}
			else if ((mine%2) || (mine==row*col-2)) impossible = 1;
			else {
				for (i=0; i<mine/2; i++) grid[i][0] = grid[i][1] = '*';
				grid[row-1][0] = 'c';
			}
		}
		else {
			if ((row*col == mine+2) || (row*col == mine+3) || (row*col == mine+5) || (row*col == mine+7)) impossible = 1;
			else {
				r = row;
				c = col;
				m = mine;
				while (1) {	//try to make it square
					if (r > c) {	//tall, fill bottom row
						if (m < c) break;
						else {
							m -= c;
							r--;
							for (i=0; i<c; i++) grid[r][i] = '*';
						}
					}
					else {	//wide, fill right side
						if (m < r) break;
						else {
							m -= r;
							c--;
							for (i=0; i<r; i++) grid[i][c] = '*';
						}
					}
				}
			//	printf("r %d, c %d, m %d\n", r, c, m);
				if (r == c) {	//square
					if (m==r-1) {
						if (r==3) impossible = 1;
						else {
							for (i=0; i<m-1; i++) grid[r-1-i][c-1] = '*';
							grid[r-1][c-2] = '*';
							grid[0][0] = 'c';	//top left
						}
					}
					else {
						for (i=0; i<m; i++) grid[r-1-i][c-1] = '*';
						grid[0][0] = 'c';	//top left
					}
				}
				else if (r > c) {	//tall, fill right side column starting from bottom
					if (m==r-1) impossible = 1;
					else {
						for (i=0; i<m; i++) grid[r-1-i][c-1] = '*';
						grid[0][0] = 'c';	//top left
					}
				}
				else {	//wide, fill bottom row starting from right
					if (m==c-1) impossible = 1;
					else {
						for (i=0; i<m; i++) grid[r-1][c-1-i] = '*';
						grid[0][0] = 'c';	//top left
					}
				}
			}
		}
		
		printf("Case #%d:\n", t);
		if (impossible) {
			printf("Impossible\n");
		//	impossibleCount++;
		//	fprintf(stderr, "%d %d %d\n", row, col, mine);
		}
		else {
			for (i=0; i<row; i++) {
				for (j=0; j<col; j++) printf("%c", grid[i][j]);
				printf("\n");
			}
		}
	}
	
//	fprintf(stderr, "impossibleCount %d\n", impossibleCount);
	
	return 0;
}