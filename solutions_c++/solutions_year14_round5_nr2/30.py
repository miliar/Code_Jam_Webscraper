#include <iostream>
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
#include <cctype>

using namespace std;
FILE *in; FILE *out;

const int MAX = 102;
const int MM = 202;
const int LIM = (MAX * 10 + 2);

int n;
int a[MAX][2];
int dmg1, dmg2;
int dyn[MAX][MM][LIM][2][2];

int recurse(int idx, int rem, int canUse, int first, int who) {
    canUse = min(canUse, LIM - 1);

    if (idx >= n)
        return 0;
    if (dyn[idx][rem][canUse][first][who] != -1)
        return dyn[idx][rem][canUse][first][who];
    
    int ans = 0;

    if (first) {
        for (int i = 0; i <= canUse; i++) {
            int nrem = rem - i * dmg1;
            if (nrem <= 0) {
                ans = max(ans, recurse(idx + 1, a[idx + 1][0], canUse - i, 1, who) + a[idx][1]);
                break;
            }
            else {
                ans = max(ans, recurse(idx, nrem, canUse - i, 0, who));
            }
        }
        return dyn[idx][rem][canUse][first][who] = ans;
    }


    if (who == 1 || canUse == 0) {
        int nrem = rem - dmg2;
        if (nrem <= 0) {
            ans = max(ans, recurse(idx + 1, a[idx + 1][0], canUse + 1, 1, 0));
        }
        else {
            ans = max(ans, recurse(idx, nrem, canUse + 1, 0, 0));
        }
        return dyn[idx][rem][canUse][first][who] = ans;
    }

    // Shoot
    int nrem = rem - dmg1;
    if (nrem <= 0) {
        ans = max(ans, recurse(idx + 1, a[idx + 1][0], canUse - 1, 1, 1) + a[idx][1]);
    }
    else {
        ans = max(ans, recurse(idx, nrem, canUse - 1, 0, 1));
    }

    // Don't shoot
    ans = max(ans, recurse(idx, rem, canUse, 0, 1));
    
//    fprintf(stderr, "  -- answer for idx = %d, rem = %d, canUse = %d, first = %d, who = %d is: %d\n",
//        idx, rem, canUse, first, who, ans);

    return dyn[idx][rem][canUse][first][who] = ans;
}

void solve(int testNum) {
    memset(a, 0, sizeof(a));
    fscanf(in, "%d %d %d", &dmg1, &dmg2, &n);
    for (int i = 0; i < n; i++)
        fscanf(in, "%d %d", &a[i][0], &a[i][1]);
    
    memset(dyn, -1, sizeof(dyn));
    fprintf(out, "%d\n", recurse(0, a[0][0], 1, 1, 0));
//    system("pause");
}

int main(void) {
	unsigned sTime = clock();
	in = fopen("LastHit.in", "rt");
	out = fopen("LastHit.out", "wt");
	
	int numTests;
	fscanf(in, "%d", &numTests);
	for (int test = 1; test <= numTests; test++) {
		fprintf(stderr, "Currently executing testcase %d...\n", test);
		fprintf(out, "Case #%d: ", test);
		solve(test);
	}
	fprintf(stderr, "Total execution time %.3lf seconds.\n",
        (double)(clock() - sTime) / (double)CLOCKS_PER_SEC);
	return 0;
}
