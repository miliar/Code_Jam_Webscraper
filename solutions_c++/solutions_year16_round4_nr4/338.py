#include <iostream>
#include <iomanip>
#include <stdio.h>
#include <set>
#include <vector>
#include <map>
#include <cmath>
#include <algorithm>
#include <memory.h>
#include <string>
#include <sstream>
#include <cstdlib>
#include <ctime>
#include <cassert>

using namespace std;

typedef long long LL;
typedef pair<int,int> PII;

#define MP make_pair
#define PB push_back
#define FF first
#define SS second

#define FORN(i, n) for (int i = 0; i <  (int)(n); i++)
#define FOR1(i, n) for (int i = 1; i <= (int)(n); i++)
#define FORD(i, n) for (int i = (int)(n) - 1; i >= 0; i--)
#define FOREACH(i, c) for (typeof((c).begin()) i = (c).begin(); i != (c).end(); i++)

#define MOD 1000000007
#define INF 2000000000

int T, N; string row;

const int MAXN = 4;
int op[MAXN][MAXN], top[MAXN][MAXN], order[MAXN], morder[MAXN], used[MAXN];

bool check() {
    FORN(i, N) order[i] = i; // worker order

    do {
        FORN(i, N) morder[i] = i;

        do {
            memset(used, 0, sizeof used);

            FORN(i, N) {
                if (top[order[i]][morder[i]] == 1) {
                    used[morder[i]] = 1;
                }
                else {
                    int canuse = 0;

                    FORN(j, N) {
                        if (top[order[i]][j] == 1 && used[j] == 0) canuse++;
                    }

                    if (canuse == 0) {
                        return false;
                    }
                    else {
                        break;
                    }
                }
            }
        }
        while (next_permutation(morder, morder + N));
    } 
    while (next_permutation(order, order + N));

    return true;
}

int main() {
    scanf("%d", &T);

    for (int tc = 1; tc <= T; tc++) {
        printf("Case #%d: ", tc);

        scanf("%d", &N);

        memset(op, 0, sizeof op);

        FORN(i, N) {
            cin >> row;
            FORN(j, N) op[i][j] = row[j] - '0';
        }

        int res = INF;

        FORN(i, (1 << (N*N))) {
            memcpy(top, op, sizeof op); int extra = 0;

            FORN(j, N*N) {
                if (op[j/N][j%N] == 0 && i & (1 << j)) {
                    extra++;
                    top[j/N][j%N] = 1;
                }
            }

            if (check()) res = min(res, extra);
        }

        cout << res << "\n";
    }
    
    return 0;
}
