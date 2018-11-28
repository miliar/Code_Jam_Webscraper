// vudduu - codejam 2016 Round 1A
// Problem B
#include <iostream>
#include <sstream>
#include <utility>
#include <cstdlib>
#include <cstdio>
#include <cctype>
#include <cmath>
#include <functional>
#include <algorithm>
#include <numeric>
#include <string>
#include <vector>
#include <queue>
#include <stack>
#include <list>
#include <map>
#include <set>
#include <stdio.h>
#include <string.h>
using namespace std;

#define FOR(i,a,b)  for(int i=(a),_##i=(b);i<_##i;++i)
#define F(i,a)      FOR(i,0,a)
#define ALL(x)      x.begin(),x.end()
#define PB          push_back
#define MP          make_pair
#define S           size()
typedef long long   LL;

int N;
bool P0[55]; // 0
bool P1[55]; // 1
vector<vector<int> > v;
vector<int> selection, posi;
bool flag, nega;
int ma[55][55];

void dfs(int it) {
    if(flag) return;
    if(it >= v.S) {
        F(i, N) {
            if(!P0[i]) {
                if(nega) {
                    for(int j=N-1; j>=0 ;j--) {
                        if(j!=N-1) printf(" ");
                        printf("%d", -ma[j][i]);
                    }
                }
                else {
                    F(j, N) {
                        if(j) printf(" ");
                        printf("%d", ma[j][i]);
                    }
                }
            }
        }
        F(i, N) {
            if(!P1[i]) {
                if(nega) {
                    for(int j=N-1; j>=0 ;j--) {
                        if(j!=N-1) printf(" ");
                        printf("%d", -ma[i][j]);
                    }
                }
                else {
                    F(j, N) {
                        if(j) printf(" ");
                        printf("%d", ma[i][j]);
                    }
                }
            }
        }
        printf("\n");
        flag = true;
    }
    if(flag) return;
    bool isValid = true;
    // 0
    F(i, N) {
        if(v[0][i] == v[it][0] && (!P0[i])) {
            isValid = true;
            vector<int> old(N);
            F(j, N) {
                old[j] = ma[j][i];
                if(ma[j][i] == 0) continue;
                if(ma[j][i] != v[it][j])
                    isValid = false;
            }
            if(isValid) {
                F(j, N) ma[j][i] = v[it][j];
                selection[it] = 0;
                P0[i] = true;
                dfs(it+1);

                P0[i] = false;
                F(j, N) ma[j][i] = old[j];
            }
        }
    }
    // 1
    F(i, N) {
        if(v[1][i] == v[it][0] && (!P1[i])) {
            isValid = true;
            vector<int> old(N);
            F(j, N) {
                old[j] = ma[i][j];
                if(ma[i][j] == 0) continue;
                if(ma[i][j] != v[it][j])
                    isValid = false;
            }
            if(isValid) {
                F(j, N) ma[i][j] = v[it][j];
                selection[it] = 1;
                P1[i] = true;
                dfs(it+1);

                P1[i] = false;
                F(j, N) ma[i][j] = old[j];
            }
        }
    }
}

void solve() {
    cin >> N;
    int n = N*2 - 1;
    v.resize(n);
    selection.resize(n);
    posi.resize(n);
    F(i, n) {
        v[i].resize(N);
        F(j, N) {
            cin >> v[i][j];
        }
    }
    memset(ma, 0, sizeof(ma));
    nega = flag = false;
    sort(ALL(v));
    if(v[0][0] != v[1][0]) {
        F(i, n) {
            F(j, N) {
                v[i][j] = -v[i][j];
            }
            reverse(ALL(v[i]));
        }
        nega = true;
        sort(ALL(v));
    }

    memset(P0, 0, sizeof(P0));
    memset(P1, 0, sizeof(P1));
    P0[0] = P1[0] = true;
    posi[0] = posi[1] = 0;
    selection[0] = 1;
    selection[1] = 0;

    F(i, N) {
        ma[0][i] = v[0][i];
        ma[i][0] = v[1][i];
    }

    dfs(2);
}

int main() {
	// freopen("in.txt", "r", stdin);
	freopen("B-small-attempt2.in", "r", stdin);
	// freopen("B-large.in", "r", stdin);
	freopen("out.txt", "w", stdout);
	int T;
    scanf("%d", &T);
    for(int cas=1; cas<=T ;cas++) {
        printf("Case #%d: ", cas);
        solve();
    }
}
