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

int test;
double c, f, x, res;

double solve(int n) {
    int cnt = 0;
    double res = 0.0;
    double cur = 0.0;
    double cps = 2.0;
    while (true) {
        if (cnt == n) {
            res += (x-cur)/cps;
            return res;
        }
        res += c/cps;
        cps += f;
        cnt++;
    }
}

int main() {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    read(test);
    FOR(TEST, 1, test) {
        printf("Case #%d: ", TEST);
        cin >> c >> f >> x;
        res = 1000000000.0;
        int cntDaoChieu = 0;
        FOR(numberOfFactory, 0, 10000) {
            double cntTime = solve(numberOfFactory);
            res = min(res, cntTime);
            if (cntDaoChieu == 0 && cntTime < res) cntDaoChieu++;
            if (cntDaoChieu == 1 && cntTime > res) break;
            //cout << numberOfFactory << " " << cntTime << endl;
        }
        printf("%.7lf\n", res);
    }
    return 0;
}

