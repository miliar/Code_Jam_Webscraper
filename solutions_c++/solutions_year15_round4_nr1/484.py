#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cmath>
#include <vector>
#include <string>
#include <cstring>
#include <cstdlib>
#include <map>
#include <set>
#include <queue>
#include <stack>

#define mp make_pair

using namespace std;

typedef long long ll;

char v[128][128];
bool u[128][128];
int r, c;

bool checkCell(int x, int y) {
    int i;
    for(i=y-1; i>=0; --i) {
        if (v[x][i] != '.') return true;
    }
    for(i=y+1; i<c; ++i) {
        if (v[x][i] != '.') return true;
    }
    for(i=x-1; i>=0; --i) {
        if (v[i][y] != '.') return true;
    }
    for(i=x+1; i<r; ++i) {
        if (v[i][y] != '.') return true;
    }
    return false;
}

bool checkPossible() {
    int i, j, k;
    for(i=0; i<r; ++i) {
        for(j=0; j<c; ++j) {
            if (v[i][j] != '.' && !checkCell(i, j)) {
                return false;
            }
        }
    }
    return true;
}

int main() {
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
    int T, NT;
    cin>>NT;
    int i, j, n, m;

    for(T=1; T<=NT; ++T) {
        cin>>r>>c;
        for(i=0; i<r; ++i) {
            cin>>v[i];
        }
        if (!checkPossible()) {
            printf("Case #%d: IMPOSSIBLE\n", T);
            continue;
        }
        int res=0;
        memset(u, 0, sizeof(u));
        for(i=0; i<r; ++i) {
            for(j=0; j<c; ++j) {
                if (v[i][j] != '.') {
                    if (v[i][j] == '<') {
                        res++;
                        u[i][j] = true;
                    }
                    break;
                }
            }
            for(j=c-1; j>=0; --j) {
                if (v[i][j] != '.') {
                    if (v[i][j] == '>' && !u[i][j]) {
                        res++;
                        u[i][j] = true;
                    }
                    break;
                }
            }
        }
        for(j=0; j<c; ++j) {
            for(i=0; i<r; ++i) {
                if (v[i][j] != '.') {
                    if (v[i][j] == '^' && !u[i][j]) {
                        res++;
                        u[i][j] = true;
                    }
                    break;
                }
            }
            for(i=r-1; i>=0; --i) {
                if (v[i][j] != '.') {
                    if (v[i][j] == 'v' && !u[i][j]) {
                        res++;
                        u[i][j] = true;
                    }
                    break;
                }
            }
        }
        printf("Case #%d: %d\n", T, res);
    }
    return 0;
}
