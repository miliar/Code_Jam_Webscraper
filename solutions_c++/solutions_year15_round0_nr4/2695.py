//
//  Infinite House of Pancakes
//  Created by McKrisch on 11.04.15
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
#define SMALL

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
    int X = readInt(), R = readInt(), C = readInt();
    int r = min(R, C);
    int c = max(R, C);
    bool ret = false;
    if (X == 1) {
        ret = true;
    } else if (X == 2) {
        ret = !((r*c)&1);
    } else if (X == 3) {
        ret = (r == 2 && c == 3) ||
              (r == 3 && c == 3) ||
              (r == 3 && c == 4);
    } else if (X == 4) {
        ret = r >= 3 && c ==4;
    }
    puts(ret?"GABRIEL":"RICHARD");
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
