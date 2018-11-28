#include <iostream>
#include <algorithm>
#include <cstdio>
#include <vector>
#include <queue>

#define REP(i,a) for(int i=0;i<(a);i++)
#define FOR(i,a,b) for(int i=(a);i<(b);i++)
#define SZ size()
#define PB push_back

using namespace std;

typedef vector<int> vi;
typedef pair<int,int> pii;
typedef pair<int, pii> pip;

int solve(priority_queue<pair<int, pii> > &q) {
    int steps = 0;
    int best = 1000000;
    while (true) {
        pip plate = q.top(); q.pop();
        int bigsection = plate.first;
        best = min(best, steps + bigsection);
        if (bigsection<=1) return best;
        pii stuff = plate.second;
        int orig = stuff.first;
        int pegs = stuff.second;
        steps += 1;
        pegs += 1;
        q.push(make_pair((orig+pegs)/(pegs+1), pii(orig,pegs)));
    }
}

int main() {
    int T, D;
    cin >> T;
    REP(cas,T) {
        priority_queue<pip> q;
        cin >> D;
        REP(d,D) {
            int x;
            cin >> x;
            q.push(make_pair(x, pii(x,0)));
        }
        printf("Case #%d: %d\n", cas+1, solve(q));
    }
    return 0;
}
