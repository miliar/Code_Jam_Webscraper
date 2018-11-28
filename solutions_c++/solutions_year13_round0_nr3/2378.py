/**
 * Jerry Ma
 * C.cpp
 */

#include <assert.h>
#include <ctype.h>
#include <math.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include <algorithm>
#include <bitset>
#include <deque>
#include <fstream>
#include <iostream>
#include <list>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <stack>
#include <string>
#include <utility>
#include <vector>

using namespace std;

typedef long long int lli;
typedef pair<int, int> pii;

int gInt () {
    int i;
    scanf("%d", &i);
    return i;
}

lli gLong () {
    lli i;
    scanf("%lld", &i);
    return i;
}

double gDouble () {
    double i;
    scanf("%lf", &i);
    return i;
}

void quit () {
    fflush(stdout);
    exit(0);
}

map <lli, int> freqs;
char buf[20];

inline bool isPalin (lli num) {
    sprintf(buf, "%lld", num);
    int len = strlen(buf);
    for (int i = 0; i < len / 2; i ++) {
        if (buf[i] != buf[len - i - 1])
            return false;
    }
    return true;
}

int main (int argc, char ** argv) {
    int count = freqs[0] = 0;
    for (lli i = 1; i <= ((int) 1E7); i ++) {
        if (isPalin(i)) {
            lli sq = i * i;
            if (isPalin(sq)) {
                freqs[sq] = ++count;
                fprintf(stderr, "%lld %d\n", sq, count);
            }
        }
    }
    freqs[1LL << 60] = count;
    int nC = gInt();
    for (int i = 1; i <= nC; i ++) {
        lli a = gLong(), b = gLong();
        int upcount = (--freqs.upper_bound(b))->second;
        int downcount = (--freqs.lower_bound(a))->second;
        printf("Case #%d: %d\n", i, upcount - downcount);
    }
    quit();
}