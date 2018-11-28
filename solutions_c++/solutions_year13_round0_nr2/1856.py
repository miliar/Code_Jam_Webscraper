#include <vector>
#include <list>
#include <queue>
#include <map>
#include <set>
#include <algorithm>
#include <cmath>
#include <cstdio>
#include <iostream>

#define NMAX 101
#define MMAX 101
#define p(i, j) (i * m + j)

using namespace std;

int test_count;
int n, m;
int a[NMAX * MMAX];
bool hLines[NMAX];
set<int> lvls;

bool test(int c) {
    //cout << "Testing level " << c << ": " << endl;
    for (int i = 0; i < n; i++) {
        if (a[p(i, 0)] == c) {
            hLines[i] = true;
            for (int j=1; j < m; j++) {
                if (a[p(i, j)] != c) {
                    hLines[i] = false;
                    break;
                }
            }
        } else {
            hLines[i] = false;
        }
    }
    for (int j=0; j < m; j++) {
        bool vLine = true;
        bool wouldFail = false;
        for (int i=0; i < n; i++) {
            if (a[p(i, j)] == c) {
                if (vLine) {
                    wouldFail = wouldFail || (!hLines[i]);
                } else if (!hLines[i]) {
                    return false;
                }
            } else {
                vLine = false;
                if (wouldFail) {
                    return false;
                }
            }
        }
    }
    //cout << "" << endl;
    return true;
}

void fill(int lvl) {
    for (int i=0; i < n * m; i++) {
        if (a[i] < lvl) {
            a[i] = lvl;
        }
    }
}

int main(int argc, char *argv[]) {
    scanf("%d", &test_count);
    for (int t=0; t < test_count; t++) {
        scanf("%d%d", &n, &m);
        bool failed = false;
        lvls.clear();
        lvls.insert(100);
        for (int i=0; i < n * m; i++) {
            scanf("%d", &a[i]);
            lvls.insert(a[i]);
        }
        for (set<int>::iterator it=lvls.begin(); *it != 100;) {
            if (!test(*it++)) {
                failed = true;
                break;
            }
            fill(*it);
        }
        cout << "Case #" << (t + 1) << ": " << (failed?"NO":"YES") << endl;
    }
    return 0;
}
