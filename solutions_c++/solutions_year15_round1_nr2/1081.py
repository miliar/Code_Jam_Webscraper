#include <stdio.h>
#include <math.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>
#include <iostream>
#include <algorithm>
#include <vector>
#include <stack>
#include <queue>
#include <set>
#include <map>
#include <string>
#include <functional>
using namespace std;

#define lli long long int

const int N = (int)(3e5 + 20);

int testsCount;
int n, s;
lli a[N];

lli bestTime = -1;

lli countOf(lli time, int i) {
    lli total = (time / a[i]) + (time % a[i] ? 1 : 0);
    return total * a[i];
}

lli check(lli time) {
    int countInQueue = 0;
    lli total = 0;
    for (int i = 0; i < n; ++i) {
        total += time / a[i];
        countInQueue += (time % a[i]) > 0;
    }
    total += countInQueue;
    if (total < s) {
        bestTime = max(bestTime, time);
        return total;
    }
    return -1;
}

int firstAvailable(lli time) {
    set<pair<lli, int> > sAvailable;
    for (int i = 0; i < n; ++i) {
        sAvailable.insert(make_pair(countOf(time, i), i));
    }
    lli total = check(time);
    while (total < s - 1) {
        pair<lli, int> cur = *sAvailable.begin();
        sAvailable.erase(sAvailable.begin());
        sAvailable.insert(make_pair(cur.first + a[cur.second], cur.second));
        ++total;
    }
    return sAvailable.begin()->second;
}

int main() {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);

    scanf("%d", &testsCount);
    for (int testNumber = 1; testNumber <= testsCount; testNumber++) {
        cin >> n >> s;
        for (int i = 0; i < n; ++i) cin >> a[i];

        lli l = 0;
        __int64 r = (1LL << 61);
        bestTime = l;
        while (r - l > 1) {
            lli m = (l + r) / 2;
            if (check(m) > -1) l = m;
            else r = m;
        }
        check(l); check(r);

        printf("Case #%d: ", testNumber);

        cout << firstAvailable(bestTime) + 1;

        cout << endl;
    }
}