#include <array>
#include <cassert>
#include <cmath>
#include <cstdio>
#include <cstring>
#include <functional>
#include <string>
#include <vector>
#include <queue>
#include <map>
#include <set>
#include <algorithm>
#include <iostream>
#include <sstream>
using namespace std;

#define REP(i, n) for(int i = 0; i < (int)(n); ++ i)
#define FOR(i, b, e) for(auto i = b; i < e; ++ i)
#define all(x) (x).begin(), (x).end()

int n;
string s, target;

map<string, int> dist;

string flip(string t, int k) {
    std::reverse(t.begin(), t.begin() + k);
    for(int j=0; j<k; ++j) t[j] = (t[j] == '+' ? '-' : '+');
    return t;
}

int go() {
    dist.clear();
    target = string(n, '+');

    queue<string> Q;
    Q.push(s);
    dist[s] = 0;

    while(not Q.empty()) {
        s = Q.front(); Q.pop();
        int ds = dist[s];
        if(s == target) break;

        for(int flips = 1; flips <= n; ++ flips) {
            string t = flip(s, flips);
            if(dist.count(t)) continue;

            dist[t] = ds + 1;
            Q.emplace(t);
        }
    }

    return dist[target];
}

int main() {
    int T;
    int kase = 0;
    cin >> T;
    while(T-- > 0) {
        cin >> s;
        n = (int) s.size();
        printf("Case #%d: %d\n", ++kase, go());
    }
    return 0;
}

