/*
ID: iamquang95
PROG: test
LANG: C++
*/

// Author: QCC
#include <bits/stdc++.h>
#include <unordered_map>

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

unordered_map<string, int> visited;
queue<string> fringe;

char opposite(char x) {
    return (x == '+') ? '-':'+';
}

string rev(string cur, int last) {
    string res = "";
    for(int i = last; i >= 0; --i) {
        res += opposite(cur[i]);
    }
    for(int i = last+1; i < cur.length(); ++i)
        res += cur[i];
    return res;
}

void solutionSmall() {
    string s;
    getline(cin, s);
    string destination = "";
    for(int i = 0; i < s.length(); ++i)
        destination += "+";
    //BFS
    visited.clear();
    while(!fringe.empty())
        fringe.pop();

    fringe.push(s);
    visited[s] = 0;
    //cout << endl;
    while (!fringe.empty()) {
        string cur = fringe.front(); fringe.pop();
        //cout << cur << endl;
        if (cur == destination) {
            printf("%d\n", visited[cur]);
            return;
        }
        for(int i = 0; i < cur.length(); ++i) {
            string next = rev(cur, i);
            //cout << "   " << next << endl;
            if (visited.find(next) == visited.end()) {
                visited[next] = visited[cur] + 1;
                fringe.push(next);
            }
        }
    }
}

void solutionLarge() {
    string s;
    getline(cin, s);
    string destination = "";
    for(int i = 0; i < s.length(); ++i)
        destination += "+";

    int step = 0;
    while (true) {
        if (s == destination) {
            printf("%d\n", step);
            return;
        }
        int lastPos = 0;
        while (lastPos < s.length() && s[lastPos] == s[0])
            lastPos++;
        lastPos--;
        s = rev(s, lastPos);
        step++;
    }
}


int main() {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int nTest;
    scanf("%d\n", &nTest);
    for(int test = 1; test <= nTest; ++test) {
        printf("Case #%d: ", test);
        //solutionSmall();
        solutionLarge();
    }
    return 0;
}
