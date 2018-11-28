#include <cstdio>
#include <string>
#include <algorithm>
#include <vector>
#include <iostream>
using namespace std;
const int NMAX = 505;
int tests, N, R, P, S;
char beats[NMAX];

bool ok(string& a) {
    int r = 0, s = 0, p = 0;
    for (size_t i = 0; i < a.size(); i++) {
        if (a[i] == 'R') {
            r++;
        } else if (a[i] == 'S') {
            s++;
        } else {
            p++;
        }
    }

    return r == R && s == S && p == P;
}

string get(int depth, char win) {
    if (depth == 0) {
        string s;
        s += win;

        return s; 
    }

    string a = get(depth - 1, win);
    string b = get(depth - 1, beats[win]);
    if (a.compare(b) < 0) {
        return a + b;
    }

    return b + a;
}

int main() {
    freopen("A.in", "r", stdin);
    freopen("A.out", "w", stdout);

    scanf("%d", &tests);
    beats['R'] = 'S';
    beats['S'] = 'P';
    beats['P'] = 'R';

    for (int test = 1; test <= tests; test++) {
        cout << "Case #" << test << ": ";
        scanf("%d%d%d%d", &N, &R, &P, &S);
        // P, R, S the alphabetical order

        string r = get(N, 'R');
        string s = get(N, 'S');
        string p = get(N, 'P');
        vector<string> sol;

        if (ok(r)) {
            sol.push_back(r);
        }
        if (ok(s)) {
            sol.push_back(s);
        }
        if (ok(p)) {
            sol.push_back(p);
        }
        sort(sol.begin(), sol.end());

        if (sol.empty()) {
            cout << "IMPOSSIBLE\n";
        } else {
            cout << sol[0] << "\n";
        }
    }
    return 0;
}