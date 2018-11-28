#include <iostream>
#include <algorithm>
#include <vector>
#include <queue>
#include <map>
#include <set>
#include <stdio.h>
using namespace std;

int T;

struct my {
    int pans, eaters;
    explicit my(int _pans) : pans(_pans), eaters(1) {}
    my inc() const {
        my x = *this;
        x.eaters++;
        return x;
    }
    int getTime() const {
        return (pans / eaters) +
            ((pans % eaters) ? 1 : 0);
    }
};

bool operator<(const my& x, const my& y) {
    return x.pans * y.eaters < y.pans * x.eaters;
}

int solve(priority_queue<my>& p) {
    int minTime = p.top().getTime();
    int addTime = 0;
    while (true) {
        my res = p.top();
        minTime = min(minTime, addTime + res.getTime());
        if (res.pans <= 2 * res.eaters)
            break;
        p.pop();
        p.push(res.inc());
        ++addTime;
    }
    return minTime;
}

int solve() {
    int D;
    cin >> D;
    priority_queue<my> P;
    for (int i = 0; i < D; ++i) {
        int item;
        cin >> item;
        P.push(my(item));
    }
    return solve(P);
}

int main(int argc, char* argv[]) {
    cin >> T;
    for (int t = 0; t != T; ++t) {
        int s = solve();
        if (s == -1)
            printf("Case #%d: I don't know.\n", t + 1);
        else
            printf("Case #%d: %d\n", t + 1, s);
    }
    return 0;
}

