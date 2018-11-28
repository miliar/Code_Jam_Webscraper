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
#define DEBUGARR(a,n) {cout << #a << " = " ; REP(_,0,n) cout << a[_] << ' '; cout <<endl;}
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
template <typename T> string NumberToString ( T Number ) { stringstream ss; ss << Number; return ss.str();}
int StringToNumber ( const string &Text ) { stringstream ss(Text); int result; return ss >> result ? result : 0; }


typedef pair< int, int > PII;
typedef long long LL;

const int MOD = 1e9+7;
const int SIZE1 = 1e5+10;
const int SIZE2 = 1e6+10;
const int DX[4] = {-1, 1, 0, 0};
const int DY[4] = {0, 0, 1, -1};

int n, r, p, s, m;
int x[5000];
bool found;

const int ROCK = 1;
const int PAPPER = 2;
const int SCISS = 3;

int winner(int x, int y) {
    if (x == y) return -1;
    if (x == ROCK && y == SCISS) return x;
    if (x == PAPPER && y == ROCK) return x;
    if (x == SCISS && y == PAPPER) return x;
    return y;
}

void check() {
    vector<int> current;
    vector<int> next;
    for(int i = 1; i <= m; ++i) {
        current.pb(x[i]);
        //cout << x[i] << " ";
    }
    //cout << endl;
    while (current.size() > 1) {
        int i = 0;
        while (i < current.size()) {
            if (winner(current[i], current[i+1]) == -1) return;
            next.pb(winner(current[i], current[i+1]));
            i += 2;
        }
        current = next;
        next.clear();
        //REP(i, 0, current.size())
        //    cout << current[i] << " ";
        //cout << endl;
    }
    found = true;
    for(int i = 1; i <= m; ++i) {
        if (x[i] == 1) printf("R");
        else if (x[i] == 2) printf("P");
        else printf("S");
    }
}

void attempt(int pos, int _r, int _p, int _s) {
    if (pos > m) {
        check();
        return;
    }
    if (_p) {
        x[pos] = PAPPER;
        attempt(pos+1, _r, _p-1, _s);
        x[pos] = 0;
    }
    if (found) return;
    if (_r) {
        x[pos] = ROCK;
        attempt(pos+1, _r-1, _p, _s);
        x[pos] = 0;
    };
    if (found) return;
    if (_s) {
        x[pos] = SCISS;
        attempt(pos+1, _r, _p, _s-1);
        x[pos] = 0;
    }
    if (found) return;
}

void solve() {
    RII(n, r);
    RII(p, s);
    found = false;
    m = r+p+s;
    attempt(1, r, p, s);
    if (!found)
        printf("IMPOSSIBLE");
    printf("\n");
}

int main() {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    DRI(nTest);
    for(int test = 1; test <= nTest; ++test) {
        printf("Case #%d: ", test);
        solve();
    }
    return 0;
}

