//
//  The Last Word
//  Created by McKrisch on 30.04.16
//

#include <stdio.h>
#include <string.h>
#include <algorithm>
#include <math.h>
#include <set>
#include <vector>
#include <iostream>
#include <list>

using namespace std;

#define rep(i,m) for(int i=0;i<(int)(m);i++)
#define rep1(i,m) for(int i=1;i<=(int)(m);i++)
#define For(it,c) for(__typeof(c.begin()) it=c.begin();it!=c.end();++it)

typedef unsigned long long ll;

//#define TEST
//#define SMALL

//#define COUT

#ifdef TEST
const char *kIn  = "A-test.in";
#else
#ifdef SMALL
const char *kIn  = "A-small.in";
const char *kOut = "A-small.out";
#else
const char *kIn  = "A-large.in";
const char *kOut = "A-large.out";
#endif
#endif

inline int readInt() {
    int num, c;
    while ((c = getchar_unlocked()) < '-');
    num = c - '0';
    while ((c = getchar_unlocked()) >= '0') {
        num = (num<<3) + (num<<1) + (c-'0');
    }
    return num;
}

int a[255];
char A[2009];
int ai;

void removeWord(string w, int len, char c) {
    if (len)
    rep (i, w.length()) {
        a[w[i]] -= len;
    }
    rep (i, len) {
        A[ai++] = c;
    }
}

void workCase() {
    string S;
    cin >> S;
    memset(a, 0, sizeof a);
    memset(A, 0, sizeof A);
    ai = 0;
    rep (i, S.length()) a[S[i]]++;
    removeWord("ZERO", a['Z'], '0');
    removeWord("TWO", a['W'], '2');
    removeWord("SIX", a['X'], '6');
    removeWord("SEVEN", a['S'], '7');
    removeWord("FIVE", a['V'], '5');
    removeWord("FOUR", a['U'], '4');
    removeWord("THREE", a['R'], '3');
    removeWord("EIGHT", a['G'], '8');
    removeWord("NINE", a['I'], '9');
    removeWord("ONE", a['O'], '1');
    sort(A,A+ai);
    A[ai]=0;
    cout << A << endl;
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
    rep1 (i, T) {
        cout << "Case #" << i << ": ";
        workCase();
    }
    return 0;
}
