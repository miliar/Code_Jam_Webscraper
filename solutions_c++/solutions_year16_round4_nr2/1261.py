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

int n, k;
double p[222];
int x[222];
vector<vector<int>> votes;
double result;

void calculateProb() {
    vector<double> prob;
    for(int i = 1; i <= n; ++i)
        if (x[i] == 1) {
            prob.pb(p[i]);
            //cout << p[i] << " ";
        }
    //cout << endl;
    double sum = 0;
    for(int t = 0; t < votes.size(); ++t) {
        double cur = 1;
        for(int i = 0; i < votes[t].size(); ++i)
            cur *= (votes[t][i] == 0) ? (1-prob[i]):(prob[i]);
        sum += cur;
    }
    //cout << sum << endl;
    result = max(result, sum);
}

void attempt(int pos, int remain) {
    if (pos > n) {
        if (remain == 0)
            calculateProb();
        return;
    }
    if (remain == 0) {
        attempt(pos+1, remain);
        return;
    }
    for(int i = 0; i <= 1; ++i) {
        x[pos] = i;
        if (i == 0)
            attempt(pos+1, remain);
        else
            attempt(pos+1, remain-1);
    }
}

int vote[222];

void addVotes() {
    vector<int> _vote;
    for(int i = 1; i <= k; ++i) {
        _vote.pb(vote[i]);
        //cout << vote[i] << " ";
    }
    //cout << endl;
    votes.pb(_vote);
}

void preVotes(int pos, int remain) {
    //cout << "           " << pos << " " << remain << endl;
    if (pos > k) {
        if (remain == 0)
            addVotes();
        return;
    }
    if (remain == 0) {
        preVotes(pos+1, remain);
        return;
    }
    for(int i = 0; i <= 1; ++i) {
        vote[pos] = i;
        if (i == 0)
            preVotes(pos+1, remain);
        else
            preVotes(pos+1, remain-1);
        vote[pos] = 0;

    }
}

void solve() {
    //cout << " VVVVVVVLLLLLLLL " << endl;
    RII(n, k);
    for(int i = 1; i <= n; ++i)
        cin >> p[i];
    votes.clear();
    preVotes(1, k/2);
    //cout << votes.size();
    result = 0;
    attempt(1, k);
    cout.precision(8);
    cout << fixed << result << endl;
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

