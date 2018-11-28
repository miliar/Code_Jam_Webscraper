/**
 * Google Code Jam 2013 - Round 0 Qualification Round
 * Problam A
 */

#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <math.h>
#include <ctype.h>

char line[1024];
char map[5][5];

int main()
{
	int kase, serial = 1,
		r, c;
	bool map_full, // true => no empty space
		four, // true => four in a row/col/diagonal
		x4, o4; // true => win

	gets(line);
	kase = atoi(line);

	while (kase--) {

		map_full = true;
		x4 = false;
		o4 = false;

		for (r=0; r<4; ++r) {
			gets(map[r]);

			for (c=0; c<4; ++c) {
				if (map[r][c] == '.') {
					map_full = false;
				}
			}
		}
		gets(line); // empty line

		for (r=0; r<4; ++r) {

			if (! x4) {
				// horizontally
				four = true;
				for (c=0; c<4; ++c)
					four &= (map[r][c] == 'X' || map[r][c] == 'T');
				if (four) x4 = true;
			}
			if (! x4) {
				// vertically
				four = true;
				for (c=0; c<4; ++c)
					four &= (map[c][r] == 'X' || map[c][r] == 'T');
				if (four) x4 = true;
			}

			if (! o4) {
				// horizontally
				four = true;
				for (c=0; c<4; ++c)
					four &= (map[r][c] == 'O' || map[r][c] == 'T');
				if (four) o4 = true;
			}
			if (! o4) {
				// vertically
				four = true;
				for (c=0; c<4; ++c)
					four &= (map[c][r] == 'O' || map[c][r] == 'T');
				if (four) o4 = true;
			}
		}

		if (! x4) {
			// diagonally
			four = true;
			for (r=0; r<4; ++r)
				four &= (map[r][r] == 'X' || map[r][r] == 'T');
			if (four) x4 = true;
		}
		if (! x4) {
			// anti-diagonally
			four = true;
			for (r=0; r<4; ++r)
				four &= (map[r][3-r] == 'X' || map[r][3-r] == 'T');
			if (four) x4 = true;
		}

		if (! o4) {
			// diagonally
			four = true;
			for (r=0; r<4; ++r)
				four &= (map[r][r] == 'O' || map[r][r] == 'T');
			if (four) o4 = true;
		}
		if (! o4) {
			// anti-diagonally
			four = true;
			for (r=0; r<4; ++r)
				four &= (map[r][3-r] == 'O' || map[r][3-r] == 'T');
			if (four) o4 = true;
		}

		printf("Case #%d: ", serial++);
		if (x4)
			puts("X won");
		else if (o4)
			puts("O won");
		else if (map_full)
			puts("Draw");
		else
			puts("Game has not completed");
	}
	return 0;
}
