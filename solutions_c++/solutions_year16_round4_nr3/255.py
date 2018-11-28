#include <bits/stdc++.h>

#define rep(i,n) for(int i=0;i<(int)(n);i++)
#define each(it,n) for(__typeof((n).begin()) it=(n).begin();it!=(n).end();++it)

using namespace std;

int conv(int i, int j, int R, int C) {
    return C * i + j;
}

// 0: /, 1: \
// 0:top, 1:right, 2:bottom, 3:left

int movi[2][4] = {{0, 1, 0, -1}, {0, -1, 0, 1}};
int movj[2][4] = {{-1, 0, 1, 0}, {1, 0, -1, 0}};
int stat[2][4] = {{1, 0, 3, 2}, {3, 2, 1, 0}};

void output(int bit, int R, int C) {
    cout << endl;
    rep(i, R) {
        rep(j, C) {
            cout << (((bit >> conv(i, j, R, C)) & 1) ? "\\" : "/");
        }
        cout << endl;
    }
}


bool doit(int bit, int R, int C, map<int, int>& pairs) {
    map<int, pair<int, int> > start;
    map<pair<pair<int, int>, int>, int> goal;
    int it = 0;
    rep(i, C) {
        start[it] = {conv(0, i, R, C), 0};
        goal[{{-1, i}, 2}] = it;
        it++;
    }
    rep(i, R) {
        start[it] = {conv(i, C - 1, R, C), 1};
        goal[{{i, C}, 3}] = it;
        it++;
    }
    rep(i, C) {
        start[it] = {conv(R - 1, C - 1 - i, R, C), 2};
        goal[{{R, C - 1 - i}, 0}] = it;
        it++;
    }
    rep(i, R) {
        start[it] = {conv(R - 1 - i, 0, R, C), 3};
        goal[{{R - 1 - i, -1}, 1}] = it;
        it++;
    }

    //output(bit, R, C);
    rep(i, it) {
        pair<int, int> pos = start[i];
        pair<pair<int, int>, int> g;
        do {
            int pi = pos.first / C, pj = pos.first % C;
            int st = pos.second;
            int dir = (bit >> pos.first) & 1; 
            //cerr << i << ": " << " " << pi << " " << pj << " " << st << endl;
            //cerr << "pos: " << pos.first << endl;
            //cerr << "next: " << pi + movi[dir][st] << " " << pj + movj[dir][st] << " " << stat[dir][st] << endl;            
            pos = {conv(pi + movi[dir][st], pj + movj[dir][st], R, C), stat[dir][st]};
            //cerr << "pos: " << pos.first << endl;
            g = {{pi + movi[dir][st], pj + movj[dir][st]}, stat[dir][st]};
        } while (goal.find(g) == goal.end());
        if (goal[g] != pairs[i]) return false;
    }
    
    return true;
}

void solve() {
    int R, C;
    cin >> R >> C;
    int N = 2 * (R + C);
    map<int, int> pairs;
    rep(i, N / 2) {
        int a, b;
        cin >> a >> b;
        a--, b--;
        pairs[a] = b;
        pairs[b] = a;
    }
    rep(i, 1 << (R * C)) {
        if (doit(i, R, C, pairs)) {
            output(i, R, C);
            return;
        }
    }
    cout << endl << "IMPOSSIBLE" << endl;
}

int main() {
    int T;
    cin >> T;
    rep(i, T) {
        cout << "Case #" << i + 1 << ": ";
        solve();
    }
    return 0;
}
