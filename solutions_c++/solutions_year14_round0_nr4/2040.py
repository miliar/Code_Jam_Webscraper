//
//  D.cpp
//
//
//  Created by McKrisch on 30.03.13.
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
#define ForRev(it,c) for(__typeof(c.rbegin()) it=c.rbegin();it!=c.rend();++it)
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

//#define TEST
//#define SMALL

//#define COUT

#ifdef TEST
const char *kIn  = "D-test.in";
#else
#ifdef SMALL
const char *kIn  = "D-small.in";
const char *kOut = "D-small.out";
#else
const char *kIn  = "D-large.in";
const char *kOut = "D-large.out";
#endif
#endif

//struct Block {
//    double w;
//    bool used;
//    bool operator<(const Block &other) const {
//        return w > other.w;
//    }
//};
//
//Block a[1000];
//Block b[1000];

typedef set<double> cont;
typedef cont::iterator iter;
typedef cont::reverse_iterator riter;
typedef cont::const_iterator citer;
typedef cont::const_reverse_iterator criter;


void workCase() {
    cont a, b;
    int N;
    cin >> N;
    rep (i, N) {
        double v;
        cin >> v;
        a.insert(v);
    }
    rep (i, N) {
        double v;
        cin >> v;
        b.insert(v);
    }
    
    cont ta = a, tb = b;
    
    int dw = 0, w = 0;
    rep (i, N) {
        double besta = *a.rbegin(), bestb = *b.rbegin();
        if (besta > bestb) {
            a.erase(prev(a.end()));
            b.erase(b.begin());
            w++;
        } else {
            a.erase(prev(a.end()));
            b.erase(upper_bound(b.begin(), b.end(), besta));
        }
    }
    
    if (N == w) {
        dw = w;
    } else {
        a = ta; b = tb;
        rep (i, N) {
            double besta = *a.rbegin(), bestb = *b.rbegin();
            if (besta > bestb) {
                a.erase(prev(a.end()));
                b.erase(prev(b.end()));
                dw++;
            } else {
                a.erase(a.begin());
                b.erase(prev(b.end()));
            }
        }
    }
    cout << dw << " " << w << endl;
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
    int T;
    cin >> T;
    rep (i, T) {
        cout << "Case #" << i+1 << ": ";
        workCase();
    }
    return 0;
}
