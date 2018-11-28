#include <iostream>
#include <iomanip>
#include <sstream>
#include <algorithm>
#include <vector>
#include <string>
#include <queue>
#include <set>
#include <map>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <ctime>

#define MAX 1024

using namespace std;
FILE* in; FILE* out;

struct State {
	int guess;
	int board[4][4];
};
State a[2];

void doWork(int testNum) {
	set <int> g[2];
	for (int i = 0; i < 2; i++) {
		fscanf(in, "%d", &a[i].guess);
		a[i].guess--;
		for (int row = 0; row < 4; row++)
		    for (int col = 0; col < 4; col++)
		        fscanf(in, "%d", &a[i].board[row][col]);
		for (int c = 0; c < 4; c++)
		    g[i].insert(a[i].board[a[i].guess][c]);
	}
	int inter = 0, last = -1;
	for (set <int> :: iterator it = g[1].begin(); it != g[1].end(); it++)
	    if (g[0].find(*it) != g[0].end()) inter++, last = *it;
	if (inter == 1)
	    fprintf(out, "%d\n", last);
	else if (inter == 0)
	    fprintf(out, "Volunteer cheated!\n");
	else
	    fprintf(out, "Bad magician!\n");
}

int main(void) {
	unsigned sTime = clock();
	in = fopen("magicTrick.in", "rt");
	out = fopen("magicTrick.out", "wt");
	
	int numTests;
	fscanf(in, "%d", &numTests);
	for (int test = 1; test <= numTests; test++)
	{
		fprintf(stderr, "Currently executing testcase %d...\n", test);
		fprintf(out, "Case #%d: ", test);
		doWork(test);
	}
	
	fprintf(stderr, "Total execution time %.3lf seconds.\n", (double)(clock() - sTime) / (double)CLOCKS_PER_SEC);
	return 0;
}
