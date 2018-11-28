#pragma comment(linker, "/STACK:16777216")
#include <cstdio>
#include <iostream>
#include <algorithm>
#include <vector>
#include <queue>
 #include <stack>
#include <set>
#include <map>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <string>
#include <memory.h>
#include <sstream>
 #include <complex>

#define REP(i,n) for(int i = 0, _n = (n); i < _n; i++)
#define REPD(i,n) for(int i = (n) - 1; i >= 0; i--)
#define FOR(i,a,b) for (int i = (a), _b = (b); i <= _b; i++)
#define FORD(i,a,b) for (int i = (a), _b = (b); i >= _b; i--)
 #define FORN(i,a,b) for(int i=a;i<b;i++)
#define FOREACH(it,c) for (__typeof((c).begin()) it=(c).begin();it!=(c).end();it++)
#define RESET(c,x) memset (c, x, sizeof (c))

#define sqr(x) ((x) * (x))
#define PB push_back
 #define MP make_pair
#define F first
#define S second
#define Aint(c) (c).begin(), (c).end()
#define SIZE(c) (c).size()
#define PII pair<int, int>

#define DEBUG(x) { cerr << #x << " = " << x << endl; }
#define PR(a,n) {cerr<<#a<<" = "; FOR(_,1,n) cerr << a[_] << ' '; cerr <<endl;}
#define PR0(a,n) {cerr<<#a<<" = ";REP(_,n) cerr << a[_] << ' '; cerr << endl;}
#define LL long long
#define mod 1000002013

using namespace std;

struct tInfor{
    int pos, enter, num;
};

vector<tInfor> infor;
multiset <PII > S;
int n, m;

bool callY(int n, long long p, long long index) {
    long long sum = (1LL << n) - index;


    int x = 0;
    while (sum >= 2) {
        sum /= 2;
        x ++;
    }

    long long res = 0;
    FOR (i, x + 1, n)
        res = (res * 2 + 1);

    return res < p;
}

bool callX(int n, long long p, long long index) {
    long long res = 0;
    int x = 0;
    index ++;
    while (index >= 2) {
        res = res * 2 + 1;
        x ++;
        index /= 2;
    }

    FOR (i, x + 1, n) res *= 2;

    return res < p;
}

int main() {
    freopen("B-large.in", "r", stdin);
    freopen("Blarge.out", "w", stdout);
    int nTest;
    cin >> nTest;

    FOR (test, 1, nTest) {
        cout << "Case #" << test << ": ";
        int n;
        long long p;
        cin >> n >> p;

        long long l, r, X, Y;
        l = 0; r = (1LL << n) - 1;

        while (l <= r) {
            long long mid = (l + r) / 2;
            if (callX(n, p, mid)) {
                X = mid;
                l = mid + 1;
            }
            else r = mid - 1;
        }

        l = 0; r = (1LL << n) - 1;
        while (l <= r) {
            long long mid = (l + r) / 2;
            if (callY(n, p, mid)) {
                Y = mid;
                l = mid + 1;
            }
            else r = mid - 1;
        }

        cout << X << " " << Y << endl;
    }
    return 0;
}



