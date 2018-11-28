//
//  Revenge of the Pancakes
//  Created by McKrisch on 09.04.15
//

#include <stdio.h>
#include <string.h>
#include <algorithm>
#include <math.h>
#include <set>
#include <vector>
#include <iostream>
#include <list>
#include <map>

using namespace std;

#define rep(i,m) for(int i=0;i<(int)(m);i++)
#define rep1(i,m) for(int i=1;i<=(int)(m);i++)
#define For(it,c) for(__typeof(c.begin()) it=c.begin();it!=c.end();++it)
#define ForRev(it,c) for(__typeof(c.rbegin()) it=c.rbegin();it!=c.rend();++it)

typedef unsigned long long ll;

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

int readInt() {
    int num, c;
    while ((c = getchar_unlocked()) < '-');
    num = c - '0';
    while ((c = getchar_unlocked()) >= '0') {
        num = (num<<3) + (num<<1) + (c-'0');
    }
    return num;
}

void workCase() {
    int ret = 0;
    string s;
    cin >> s;
    rep1 (i, s.length()-1) {
        ret += s[i] != s[i-1];
    }
    ret += s[s.length()-1]=='-';
    printf("%d\n", ret);
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
    int T = readInt();
    rep (i, T) {
        cout << "Case #" << i+1 << ": ";
        workCase();
    }
    return 0;
}
