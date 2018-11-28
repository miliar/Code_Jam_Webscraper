// Author: QCC
#include <iostream>
#include <cstdlib>
#include <cstdio>
#include <cstring>
#include <ctime>
#include <cmath>
#include <algorithm>
#include <sstream>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <vector>
#include <list>
#include <utility>
#include <bitset>
#include <memory.h>
#define FOR(i,a,b) for( int i=(a),_b=(b);i<=_b;i++)
#define DOW(i,b,a) for( int i=(b),_a=(a);i>=_a;i--)
#define FOREACH(it,c) for (__typeof((c).begin()) it=(c).begin(); it!=(c).end(); it++)
#define DEBUG(x) { cout << #x << " = " << x << endl; }
#define DEBUGARR(a,n) {cout << #a << " = " ; FOR(_,1,n) cout << a[_] << ' '; cout <<endl;}
#define CHECK printf("OK\n");
#define FILL(a, b) memset((a), (b), sizeof((a)))
#define pb push_back
#define mp make_pair
#define st first
#define nd second
#define read(a) scanf("%d", &(a))
#define write(a) printf("%d ", a);

using namespace std;

template<class T> T gcd(T a, T b) { T r; while (b != 0) { r = a % b; a = b; b = r; } return a; }
template<class T> T lcm(T a, T b) { return a / gcd(a, b) * b; }
template<class T> T sqr(T x) { return x * x; }
template<class T> T cube(T x) { return x * x * x; }
template<class T> int getbit(T s, int i) { return (s >> i) & 1; }
template<class T> T onbit(T s, int i) { return s | (T(1) << i); }
template<class T> T offbit(T s, int i) { return s & (~(T(1) << i)); }
template<class T> int cntbit(T s) { return __builtin_popcount(s); }


typedef pair< int, int > pii;
typedef long long LL;

//const int MAXINT = 2147483647;
//const LL MAXLL = (long long)9223372036854775807;

int test, r, c, m;

//solve small test case
bool found = false;
int x[55][55];
int a[55][55];
bool visited[55][55];

const int dx[8] = {-1, -1, -1, 0, 0, 1, 1, 1};
const int dy[8] = {-1, 0, 1, -1, 1, -1, 0, 1};

void printRes() {
    FOR(i, 1, r) {
        FOR(j, 1, c) {
            if (x[i][j] == 0) printf(".");
            if (x[i][j] == 1) printf("*");
            if (x[i][j] == 2) printf("c");
        }
        printf("\n");
    }
    found = true;
}

bool inSide(int x, int y) {
    return (1 <= x && x <= r && 1 <= y && y <= c);
}

void dfs(int x, int y) {
    visited[x][y] = true;
    if (a[x][y] != 0) return;
    FOR(k, 0, 7) {
        int xx = x + dx[k];
        int yy = y + dy[k];
        if (!visited[xx][yy] && inSide(xx, yy))
            dfs(xx, yy);
    }
}

void bfs(int X, int y) {
    memset(visited, false, sizeof(visited));
    dfs(X, y);
    int correct = 1;
    FOR(i, 1, r)
    FOR(j, 1, c)
        if (visited[i][j] == false && x[i][j] == 0)
            correct = 0;
    if (correct == 1) {
        x[X][y] = 2;
        printRes();
    }
}

void check() {
    memset(a, 0, sizeof(a));
    FOR(i, 1, r)
    FOR(j, 1, c)
        if (x[i][j] == 1) {
            FOR(k, 0, 7)
                a[i+dx[k]][j+dy[k]]++;
        }
    FOR(i, 1, r)
    FOR(j, 1, c)
        if (x[i][j] == 0) {
            if (found) break;
            bfs(i, j);
        }
}

void attempt(int i, int j, int mines) {
    //cout << i << " " << j << " " << mines << endl;
    if (found) return;
    if ((i > r && mines == 0) || mines == 0) {
        //cout << "wwww";
        check();
        return;
    }
    if (i > r) {return;}
    FOR(k, 0, 1) {
        x[i][j] = k;
        if (j == c) attempt(i+1, 1, mines-k);
        else
            attempt(i, j+1, mines-k);
        x[i][j] = 0;
    }
}

int main() {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    read(test);
    FOR(TEST, 1, test) {
        memset(x, 0, sizeof(x));
        memset(a, 0, sizeof(a));
        printf("Case #%d:\n", TEST);
        scanf("%d %d %d", &r, &c, &m);
        found = false;
        attempt(1, 1, m);
        if (!found) printf("Impossible\n");
    }
    return 0;
}

