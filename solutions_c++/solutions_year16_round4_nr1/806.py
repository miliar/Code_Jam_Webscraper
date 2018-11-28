#include <iostream>
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
#include <cctype>
#include <cmath>
#include <ctime>

using namespace std;
FILE* in = stdin; FILE* out = stdout;

const int LVL = 16;
const int MM = 256;

int n;
int R, P, S;
char use[LVL][MM][2];
string ans;
string cur;

void updateAns() {
    int cntR = 0, cntP = 0, cntS = 0;
    for (int i = 0; i < (int)cur.size(); i++) {
        if (cur[i] == 'R') cntR++;
        if (cur[i] == 'P') cntP++;
        if (cur[i] == 'S') cntS++;
    }
    if (cntR == R && cntP == P && cntS == S) {
        if (ans == "IMPOSSIBLE" || cur < ans)
            ans = cur;
    }
}

void buildTree(int level, char parent) {
    if (level == 0) {
        cur += parent;
        return;
    }
    buildTree(level - 1, use[level][parent][0]);
    buildTree(level - 1, use[level][parent][1]);
}

void getMins() {
    n = 12;
    for (int level = 1; level <= n; level++) {
        // We want Rock to win
        cur = "";
        buildTree(level - 1, 'R');
        string lastR1 = cur;
        cur = "";
        buildTree(level - 1, 'S');
        string lastR2 = cur;
        if (lastR1 < lastR2)
            use[level]['R'][0] = 'R', use[level]['R'][1] = 'S';
        else
            use[level]['R'][0] = 'S', use[level]['R'][1] = 'R';

        // We want Paper to win
        cur = "";
        buildTree(level - 1, 'P');
        string lastP1 = cur;
        cur = "";
        buildTree(level - 1, 'R');
        string lastP2 = cur;
        if (lastP1 < lastP2)
            use[level]['P'][0] = 'P', use[level]['P'][1] = 'R';
        else
            use[level]['P'][0] = 'R', use[level]['P'][1] = 'P';

        // We want Scissors to win
        cur = "";
        buildTree(level - 1, 'S');
        string lastS1 = cur;
        cur = "";
        buildTree(level - 1, 'P');
        string lastS2 = cur;
        if (lastS1 < lastS2)
            use[level]['S'][0] = 'S', use[level]['S'][1] = 'P';
        else
            use[level]['S'][0] = 'P', use[level]['S'][1] = 'S';
    }
}

void solveTest() {
    fscanf(in, "%d %d %d %d", &n, &R, &P, &S);

    ans = "IMPOSSIBLE";

    cur = "";
    buildTree(n, 'R');
    updateAns();

    cur = "";
    buildTree(n, 'P');
    updateAns();

    cur = "";
    buildTree(n, 'S');
    updateAns();

    fprintf(out, "%s\n", ans.c_str());
}

int main(void) {
	unsigned sTime = clock();
	in = fopen("RatherPerplexingShowdown.in", "rt");
	out = fopen("RatherPerplexingShowdown.out", "wt");

    getMins();

	int numTests;
	fscanf(in, "%d", &numTests);
	for (int test = 1; test <= numTests; test++) {
		fprintf(stderr, "Currently executing testcase %d...\n", test);
		fprintf(out, "Case #%d: ", test);
		solveTest();
	}

	fprintf(stderr, "Total execution time %.3lf seconds.\n",
        (double)(clock() - sTime) / (double)CLOCKS_PER_SEC);
	return 0;
}
