//
//  B.cpp
//  Problem B. Lawnmower
//
//  Created by McKrisch on 2013-04-13.
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

#define rep(i,m) for(int i=0;i<(int)(m);i++)

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

typedef set<int> cont;
typedef cont::iterator iter;
typedef cont::reverse_iterator riter;
typedef cont::const_iterator citer;
typedef cont::const_reverse_iterator criter;

int N, M;
int a[100][100];

class PatternChecker {
public:
    inline void initMaximums(int val, int i, int j) {
        rb[i].init(val);
        cb[j].init(val);
    }

    inline bool check(int val, int i, int j) const {
        if (rb[i].check(val)) return true;
        if (cb[j].check(val)) return true;
        return false;
    }
    
    bool isPossible() const {
        rep(i, N) {
            rep(j, M) {
                if (!check(a[i][j], i, j)) return false;
            }
        }
        return true;
    }
    
private:
    struct Bounds {
        int _max;
        Bounds():_max(0) { }
        inline void init(int val) {
            _max = max(_max, val);
        }
        inline bool check(int val) const {
            return  val >= _max?true:false;
        }
    } rb[100], cb[100];
};

void workCase() {
    cin >> N >> M;
    PatternChecker hc;
    rep(i, N) {
        rep(j, M) {
            cin >> a[i][j];
            hc.initMaximums(a[i][j], i, j);
        }
    }
    bool res = hc.isPossible();
    cout << (res?"YES":"NO") << endl;
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
