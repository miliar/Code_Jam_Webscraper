#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <vector>
#include <queue>
#include <stack>
#include <list>
#include <string>
#include <memory.h>
#include <algorithm>

using namespace std;

const int MAXN = 1000010;

int n;
int myMote;
int motes[MAXN];

int solve() {
    scanf("%d %d", &myMote, &n);
    for (int i = 0; i < n; i++) {
        scanf("%d", &motes[i]);
    }
    long long sum = myMote;

    sort(motes, motes + n);
    long long res = n;

    int curMoves = 0;
    for (int i = 0; i < n; i++) {
        //cout << i << " " << sum << " " << res << endl;
        if (sum > motes[i]) {
            sum += motes[i];
        } else {
            while (sum <= motes[i] && sum - 1 > 0) {
                curMoves++;
                sum += sum - 1;
            }

            if (sum > motes[i]) {
                sum += motes[i];
            } else {
                break;
            }
        }
        //cout << curMoves << endl;
        if (curMoves + n - i - 1 < res) {
            res = curMoves + n - i - 1;
        }
    }

    return res;
}

int main() {
    int tests;
    scanf("%d", &tests);
    for (int test = 1; test <= tests; test++) {
        printf("Case #%d: %d\n", test, solve());
    }

    return 0;
}
