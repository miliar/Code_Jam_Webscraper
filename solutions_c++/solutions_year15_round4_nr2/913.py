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

int n;
double r[111], c[111];
double v, x;

const double eps = 0.0000000001;

int main() {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    DRI(nTest);
    FOR(test, 1, nTest) {
        printf("Case #%d: ", test);
        scanf("%d %lf %lf", &n, &v, &x);
        FOR(i, 1, n)
            scanf("%lf %lf", &r[i], &c[i]);
        /*if (test == 59) {
            cerr << r[1] << " " << c[1] << endl;
            cerr << r[2] << " " << c[2] << endl;
            cerr << v << " " << x << endl;
            cerr << endl;
        }*/
        bool tt = true;
        if (abs(c[1] - c[2]) < eps) {
            r[1] += r[2];
            n = 1;
            tt = false;
        }
        if (abs(c[1] - x) < eps && tt) {
            n = 1;
        }
        if (abs(c[2] - x) < eps && tt) {
            r[1] = r[2];
            c[1] = c[2];
            n = 1;
        }
        /*if (test == 59) {
            cerr << r[1] << " " << c[1] << endl;
            cerr << r[2] << " " << c[2] << endl;
            cerr << v << " " << x << endl;
            cerr << n << endl;
        }*/
        if (n == 1) {
            if (x != c[1])
                printf("IMPOSSIBLE\n");
            else {
                double res = v*1.0/r[1];
                printf("%.9f\n", res);
            }
        } else {
            if ((c[1] > x && c[2] > x) || (c[1] < x && c[2] < x)) {
                printf("IMPOSSIBLE\n");
                continue;
            }
            double a1 = r[1];
            double b1 = r[2];
            double c1 = v;
            double a2 = r[1]*c[1];
            double b2 = r[2]*c[2];
            double c2 = x*v;

            /*if (abs(a1*b2 - b1*a2) < eps) {
                if (test == 59) cerr << "vcl" << printf("%.7f", a1*b2 - b1*a2);
                printf("IMPOSSIBLE\n");
                continue;
            }*/

            double res1 = (c1*b2 - b1*c2)/(a1*b2 - b1*a2);
            double res2 = (a1*c2 - c1*a2)/(a1*b2 - b1*a2);
            double res = max(res1, res2);

            if (res1 < 0 || res2 < 0)
                printf("IMPOSSIBLE\n");
            else
                printf("%.9f\n", res);
        }
    }
    return 0;

}
