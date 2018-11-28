/* Date: 28 May 2016
 * Comments: (in-contest)
 */

#include <fstream>
#include <iostream>
#include <cstdio>
#include <cstring>
#include <string>
#include <ctime>
#include <cassert>
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;
typedef long long ll;
#define err(...) fprintf(stderr,__VA_ARGS__)
#define debug(var) cerr << #var << " = " << var << " ";

const int MAXN= 100;
int R,C,N;
int love[MAXN];

bool maze[20][20];

void printmaze() {
	for (int i=0; i<R; i++) {
		for (int j=0; j<C; j++) {
			if (maze[i][j]) printf("\\");
			else printf("/");
		}
		printf("\n");
	}
}

struct Cell {
	int i,j;
	Cell(int i, int j): i(i), j(j) {}
};

//Courtier to coordinates
Cell cloc(int a) {
	if (a<C) return Cell(-1,a);
	if (a<C+R) return Cell(a-C, C);
	if (a<2*C+R) return Cell(R, 2*C+R-1-a);
	return Cell(2*C+2*R-1-a, -1);
}
//Coordinates to coortier, or -1 if still in the maze
int court(int i, int j) {
	if (i>=0 && i<R && j>=0 && j<C) return -1;
	if (i==-1) return j;
	if (j==C) return i+C;
	if (i==R) return 2*C+R-1-j;
	if (j==-1) return 2*C+2*R-1-i;

	assert(false);
}

Cell next(Cell prev, Cell cur) {
	if (maze[cur.i][cur.j]) {
		int d = (cur.i+cur.j) - (prev.i+prev.j);
		return Cell(prev.i+d,prev.j+d);
	} else {
		int d = (cur.i-cur.j) - (prev.i-prev.j);
		//err("\n(%d,%d) - (%d,%d) gives d=%d\n",prev.i,prev.j,cur.i,cur.j,d);
		return Cell(prev.i+d,prev.j-d);
	}
}

Cell goin(Cell cur) {
	if (cur.i == -1) return Cell(0,cur.j);
	if (cur.i == R) return Cell(R-1,cur.j);
	if (cur.j == -1) return Cell(cur.i,0);
	if (cur.j == C) return Cell(cur.i,C-1);
	assert(false);
}

bool mazeworks() {
	/*err("trying this maze:\n");
	printmaze();*/
	for (int a=0; a<2*R+2*C; a++) {
		int b = love[a];
		//if (a<b) continue; //No need to try both directions
		Cell prev = cloc(a);
		Cell cur = goin(prev);
		//err("(%d,%d)->(%d,%d)",prev.i,prev.j,cur.i,cur.j);
		while (court(cur.i,cur.j) == -1) {
			Cell nxt = next(prev,cur);
			prev = cur;
			cur = nxt;
			//err("->(%d,%d)",cur.i,cur.j);
		}
		if (court(cur.i,cur.j) != b) return false;
	}


	return true;
}




void doCase(int case_number) {
	cin >> R >> C;
	N = 2*(R+C);
	for (int i=0; i<(R+C); i++) {
		int a,b; cin >> a >> b;
		love[a-1] = b-1;
		love[b-1] = a-1;
	}
	printf("Case #%d:\n",case_number);
	for (int mask=0; mask<(1<< (R*C)); mask++) {
		for (int k=0; k<R*C; k++) {
			int i = k/C;
			int j = k%C;
			maze[i][j] = (mask & (1<<k));
		}
		if (mazeworks()) {
			printmaze();
			return;
		}
	}
	printf("IMPOSSIBLE\n");
}

/* PROBLEM NON-SPECIFIC TEMPLATE CODE FOLLOWS.
 * This template version created 25 April 2016.
 * The code below reads the input, and prints the output either to stdout or to a file.
 * If output goes to a file, it also writes a log file for later reference.
 * Notes:
 * 	- If no arguments are provided, the program reads from standard input and prints to standard output.
 * 	- The first argument specifies the input file name. If it is "x", the standard input is used.
 * 	- The second argument specifies the output file name. If it is "a", an unused filename is created.
 * 	- This code assumes that the first line of the input is the number of cases that follow.
 *	- If output is written to a file, then a corresponding "log" file is also created, to store some basic information and the source code used to create this output.
 */

ofstream logstream;

int main(int argc, char **argv) {
	if (argc>1 && argv[1][0]!= 'x') freopen(argv[1],"r",stdin);
	if (argc>2) {
		// Second argument tells filename for the output.
		// If the argument is "a" (for auto), one is created.
		char outfname[100];
		char logfname[100];
		if (argv[2][0] != 'a') {
			strcpy(outfname,argv[2]);
			sprintf(logfname,"%s.log",outfname);
		} else {
			int id = 0;
			// stem will remove ".in" from the input file name, if present.
			char stem[100];
			strcpy(stem,argv[1]);
			if (strcmp(stem+(strlen(stem)-3),".in") == 0) stem[strlen(stem)-3] = 0;
			char outfname[100];
			while (true) {
				sprintf(outfname,"%s.out%d",stem,id);
				sprintf(logfname,"%s.log%d",stem,id);
				ifstream in(outfname);
				if (!in) break;
				id++;
			}
			freopen(outfname,"w",stdout);
			logstream.open(logfname);
			err("Writing output to %s.\n",outfname);

			// Generate a log for this execution.
			time_t rawtime = time(NULL);
			tm *timeinfo = localtime(&rawtime);
			logstream << asctime(timeinfo);
		}
	}
	int T; cin >> T;
	err("There are %d cases.\n",T);
	logstream << "There are " << T << " cases." << endl;
	
	clock_t prev,cur = clock();
	clock_t start = cur;
	for (int t=1; t<=T; t++) {
		doCase(t);
		prev = cur;
		cur = clock();
		int time_elapsed = (int) ( 1000*(cur - prev) / ((int)CLOCKS_PER_SEC));
		err("_%d(%d)_",t, time_elapsed);
		logstream << "Case #" << t << " completed in " << time_elapsed << "ms" << endl;

	}
	int total_time = (int) ( 1000*(cur-start) / ((int)CLOCKS_PER_SEC) );
	err("\nFinished %d cases in %d milliseconds.\n",T,total_time);

	// Print the source code (minus the template) to the log for reference.
	if (logstream.good()) {
		logstream << "Total time: " << total_time << endl;
		logstream << "\nCurrent source code for " << __FILE__ << ":" << endl;
		ifstream src;
		src.open(__FILE__);
		while (true) {
			string line; getline(src,line);
			if (line == "/* PROBLEM NON-SPECIFIC TEMPLATE CODE FOLLOWS.") break;
			logstream << line << endl;
		}
		logstream << "(Truncating at the beginning of the template code)" << endl;
	}
}
