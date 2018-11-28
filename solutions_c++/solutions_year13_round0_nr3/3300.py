//
//  C.cpp
//  Problem C. Fair and Square
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
#define For(it,c) for(__typeof(c.begin()) it=c.begin();it!=c.end();++it)

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
#define SMALL

//#define COUT

#ifdef TEST
const char *kIn  = "C-test.in";
#else
#ifdef SMALL
const char *kIn  = "C-small.in";
const char *kOut = "C-small.out";
#else
const char *kIn  = "C-large.in";
const char *kOut = "C-large.out";
#endif
#endif

typedef list<uint64_t> cont;
typedef cont::iterator iter;
typedef cont::reverse_iterator riter;
typedef cont::const_iterator citer;
typedef cont::const_reverse_iterator criter;

cont dict;

inline bool isPalindrome(const string &s) {
    if (equal(s.begin(), s.begin() + s.size()/2, s.rbegin())) {
        return true;
    } else {
        return false;
    }
}

inline bool isPalindrome(uint64_t val) {
    stringstream iss;
    iss << val;
    string s = iss.str();
    return isPalindrome(s);
}

void workCase() {
    int A, B;
    cin >> A >> B;
    
    uint64_t res = 0;
    For (i, dict) {
        const uint64_t &v = *i;
        if (v < A) continue;
        if (v > B) break;
        res++;
    }
    cout << res << endl;
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
    
    uint64_t m = std::pow<uint64_t,uint64_t>(10, 14);
    
    for (uint64_t i = 1; ; i++) {
        if (!isPalindrome(i)) continue;
        uint64_t res = i*i;
        if (res > m) {
            break;
        }
        if (isPalindrome(res)) {
            dict.push_back(res);
        }
    }
    
    int N;
    cin >> N;
    rep (i, N) {
        cout << "Case #" << i+1 << ": ";
        workCase();
    }
    return 0;
}
