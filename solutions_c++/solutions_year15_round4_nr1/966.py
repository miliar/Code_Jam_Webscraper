/*
ID: iamquan2
PROG: test
LANG: C++
*/

// Author: QCC
#include <bits/stdc++.h>

using namespace std;

//Loop
#define FOR(i,a,b) for( int i=(a),_b=(b);i<=_b;i++)
#define REP(i,a,b) for( int i=(a),_b=(b);i<_b;++i)
#define DOW(i,b,a) for( int i=(b),_a=(a);i>=_a;i--)
#define FOREACH(it,c) for (__typeof((c).begin()) it=(c).begin(); it!=(c).end(); it++)
//Debugging
#define DEBUG(x) { cout << #x << " = " << x << endl; }
#define DEBUGARR(a,n) {cout << #a << " = " ; FOR(_,1,n) cout << a[_] << ' '; cout <<endl;}
#define CHECK printf("OK\n");
//Read and init
#define RI(X) scanf("%d", &(X))
#define RII(X, Y) scanf("%d%d", &(X), &(Y))
#define RIII(X, Y, Z) scanf("%d%d%d", &(X), &(Y), &(Z))
#define DRI(X) int (X); scanf("%d", &X)
#define DRII(X, Y) int X, Y; scanf("%d%d", &X, &Y)
#define DRIII(X, Y, Z) int X, Y, Z; scanf("%d%d%d", &X, &Y, &Z)
#define RC(X) scanf("%c", &(X))
#define DRC(X) char (X); scanf("%c", &X)
#define FILL(a, b) memset((a), (b), sizeof((a)))
//Shorten keyword
#define pb push_back
#define mp make_pair
#define st first
#define nd second

int gcd(int a, int b) { int r; while (b != 0) { r = a % b; a = b; b = r; } return a; }
int lcm(int a, int b) { return a / gcd(a, b) * b; }
int getBit(int s, int i) { return (s >> i) & 1; }
int onBit(int s, int i) { return s | (int(1) << i); }
int offBit(int s, int i) { return s & (~(int(1) << i)); }
int cntBit(int s) { return __builtin_popcount(s); }
int sqr(int x) {return x*x; };


typedef pair< int, int > PII;
typedef long long LL;

const int MOD = 1e9+7;
const int SIZE = 1e6+10;
const int DX[4] = {-1, 1, 0, 0};
const int DY[4] = {0, 0, 1, -1};

int r, c;
int a[111][111];

bool inside(int x, int y) {
    return (x >= 0) && (x < r) && (y >= 0) && (y < c);
}

bool outside(int x, int y) {
    if (a[x][y] == -1) return false;
    bool res = true;
    int k = a[x][y];
    while (inside(x, y)) {
        x += DX[k];
        y += DY[k];
        if (!inside(x, y)) break;
        if (a[x][y] != -1) {
            res = false;
            break;
        }
    }
    return res;
}

bool check(int x, int y) {
    if (a[x][y] == -1)
        return false;
    FOR(k, 0, 3) {
        a[x][y] = k;
        if (!outside(x, y)) return false;
    }
    return true;
}



int main() {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    DRI(nTest);
    FOR(test, 1, nTest) {
        scanf("%d %d\n", &r, &c);
        REP(i, 0, r) {
            REP(j, 0, c) {
                char ch;
                scanf("%c", &ch);
                int k = 0;
                if (ch == '^') k = 0;
                if (ch == 'v') k = 1;
                if (ch == '>') k = 2;
                if (ch == '<') k = 3;
                if (ch == '.') k = -1;
                a[i][j] = k;
            }
            scanf("\n");
        }
        int res = 0;
        bool tt = true;
        REP(i, 0, r) {
            REP(j, 0, c)
                if (a[i][j] != -1 && outside(i, j)) {
                    if (check(i, j)) tt = false;
                    res++;
                }
        }
        printf("Case #%d: ", test);
        if (tt)
            printf("%d\n", res);
        else
            printf("IMPOSSIBLE\n");

    }
    return 0;

}
