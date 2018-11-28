//
//  B.cpp
//  Cookie Clicker Alpha
//  Created by McKrisch on 12.04.13.
//

#include <iostream>
#include <cstring>
#include <string.h>
#include <map>
#include <deque>
#include <queue>
#include <stack>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <algorithm>
#include <vector>
#include <set>
#include <complex>
#include <list>
#include <assert.h>

using namespace std;

#define pb push_back
#define all(v) v.begin(),v.end()
#define rall(v) v.rbegin(),v.rend()
#define sz size()
#define rep(i,m) for(int i=0;i<(int)(m);i++)
#define rep2(i,n,m) for(int i=n;i<(int)(m);i++)
#define For(it,c) for(__typeof(c.begin()) it=c.begin();it!=c.end();++it)
#define mem(a,b) memset(a,b,sizeof(a))
#define mp make_pair
#define dot(a,b) ((conj(a)*(b)).X)
#define length(V) (hypot((V).X,(V).Y))
#define vect(a,b) ((b)-(a))
#define cross(a,b) ((conj(a)*(b)).imag())
#define normalize(v) ((v)/length(v))
#define rotate(p,about,theta) ((p-about)*exp(point(0,theta))+about)
#define pointEqu(a,b) (comp(a.X,b.X)==0 && comp(a.Y,b.Y)==0)

typedef stringstream ss;
typedef pair<int, int> pii;
typedef vector<pii> vpii;
typedef vector<string> vs;
typedef vector<int> vi;
typedef vector<double> vd;
typedef vector<vector<int> > vii;
typedef long long ll;
typedef long double ld;
typedef complex<double> point;
typedef pair<point, point> segment;
typedef pair<double, point> circle;
typedef vector<point> polygon;

const double PI = 2 * acos(0);
const double eps = 1e-9;

inline int comp(const double &a, const double &b) {
    if (fabs(a - b) < eps)
        return 0;
    return a > b ? 1 : -1;
}

inline void cinclean() {
    string s;
    getline(cin, s, '\n');
}

inline int digits(int n, int &fac) {
    int retVal = 0;
    fac = 1;
    while (n /= 10) retVal++, fac*=10;
    return retVal;
}

class Timer {
public:
    Timer():begin(clock()) { }
    ~Timer() {
        printf("%g sec\n", double(clock() - begin) / CLOCKS_PER_SEC);
    }
    clock_t begin;
};

map<ll, ll> mp;

inline int readInt() {
    int num = 0;
    int c;
    while ((c = getchar_unlocked()) < '0');
    while (c >= '0' && c <= '9') {
        num = 10*num + (c - '0');
        c = getchar_unlocked();
    }
    return num;
}

//#define TEST
//#define SMALL

//#define COUT

#ifdef TEST
const char *kIn  = "B-test.in";
#else
#ifdef SMALL
const char *kIn  = "B-small.in";
const char *kOut = "B-small.out";
#else
const char *kIn  = "B-large.in";
const char *kOut = "B-large.out";
#endif
#endif

void workCase() {
    double farmCost, gain, wanted, lastSec;
    cin >> farmCost >> gain >> wanted;
    double sec = wanted/2.0;
    double r1 = 0.0;
    double cps = 2.0;
    do {
        lastSec = sec;
        r1 += farmCost/cps;
        cps += gain;
        sec = r1 + wanted/cps;
    } while (lastSec > sec);
    cout << fixed << setprecision(7) << lastSec << endl;
}

int main(int argc, const char * argv[]) {
    if (!freopen(kIn, "rt", stdin)) {
        return 1;
    }
#if !defined(COUT) && !defined(TEST)
    if (!freopen(kOut, "wt", stdout)) {
        return 2;
    }
#endif
    int N;
    cin >> N;
    rep (i, N) {
        cout << "Case #" << i+1 << ": ";
        workCase();
    }
    return 0;
}
