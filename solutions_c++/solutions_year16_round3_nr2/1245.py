#include <cctype>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <algorithm>
#include <bitset>
#include <deque>
#include <iostream>
#include <limits>
#include <map>
#include <memory>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <utility>
#include <valarray>
#include <vector>
#include <unordered_map>
#define log(...) fprintf(stderr, __VA_ARGS__)
using namespace std;
typedef long long ll;
typedef pair<int, int> ip;
typedef pair<ll, ll> lp;
int a[51][51];
int T, N, M;
int c;
bool f;
void print_adj() {
    f = true;
    printf("POSSIBLE\n");
    for ( int i = 1; i <= N; i++ ) 
        for ( int j = 1; j <= N; j++) printf("%d%s", a[i][j], j == N ? "\n" : "");
}

void dfs(int x) {
    if ( x == N ) { c++; return; }
    for ( int i = 1; i <= N; i++ ) if ( a[x][i] ) dfs(i);
}

void bf(int x, int y) {
    if ( x == N-1 && y == N ) {
        a[x][y] = 1, a[x][y] = 0, c = 0, dfs(1);
        if ( c == M ) { print_adj(); return; }
        a[x][y] = 0, a[x][y] = 1, c = 0, dfs(1);
        if ( c == M ) { print_adj(); return; }
        a[x][y] = 0, a[x][y] = 0, c = 0, dfs(1);
        if ( c == M ) { print_adj(); return; }
        return;
    }
    a[x][y] = 1, a[x][y] = 0;
    if ( y == N ) bf(x+1, x+2); else bf(x, y + 1);
    if ( f ) return;
    a[x][y] = 0, a[x][y] = 1;
    if ( y == N ) bf(x+1, x+2); else bf(x, y + 1);
    if ( f ) return;
    a[x][y] = 0, a[x][y] = 0;
    if ( y == N ) bf(x+1, x+2); else bf(x, y + 1);
    if ( f ) return;
    return;
}



int main() {
    scanf("%d", &T);
    for ( int t = 1; t <= T; t++ ) {
        scanf("%d %d", &N, &M);
        memset(a, 0, sizeof(a));
        f = false;
        printf("Case #%d: ", t);
        bf(1, 2);
        if ( !f ) printf("IMPOSSIBLE\n");
    }
    return 0;
}
