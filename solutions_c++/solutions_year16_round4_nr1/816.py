#include <bits/stdc++.h>

using namespace std;
using LINT = long long int;
using PII = pair<int,int>;

#define PB push_back
#define FI first
#define SE second
#define REP(i,n) for(int i=0;i<(n);++i)
#define FOR(i, a, b) for(int i=(a);i<(b);++i)

int n,r,p,s;

string solve(char win, int level) {

    if(level == 0) {
        return string(1, win);
    }

    if(win == 'R') {
        string r1 = solve('S', level - 1);
        string r2 = solve('R', level - 1);
        if(r1 < r2)
            return move(r1) + move(r2);
        else
            return move(r2) + move(r1);
    }
    else if(win == 'S') {
        string r1 = solve('P', level - 1);
        string r2 = solve('S', level - 1);
        if(r1 < r2)
            return move(r1) + move(r2);
        else
            return move(r2) + move(r1);
    }
    else { // P
        string r1 = solve('P', level - 1);
        string r2 = solve('R', level - 1);
        if(r1 < r2)
            return move(r1) + move(r2);
        else
            return move(r2) + move(r1);
    }

}

int alph[26];
bool check(string & ss) {
    alph['R'-'A'] = 0;
    alph['P'-'A'] = 0;
    alph['S'-'A'] = 0;

    for(char c : ss) {
        // cout << c << endl;
        alph[c-'A']++;
    }

    // cout << alph['R'-'A'] << ' ' << r << endl;
    // cout << alph['S'-'A'] << ' ' << s << endl;
    // cout << alph['P'-'A'] << ' ' << p << endl;

    if(alph['R'-'A'] == r && alph['S'-'A'] == s && alph['P'-'A'] == p) return true;
    return false;
}

void process(int caseNum) {
    cin >> n >> r >> p >> s;

    string r1 = solve('R', n);
    string r2 = solve('P', n);
    string r3 = solve('S', n);

    string res;

    if(check(r1))
        res = r1;
    if(check(r2))
        if(res.size() == 0)
            res = r2;
        else if(res > r2)
            res = r2;

    if(check(r3))
        if(res.size() == 0)
            res = r3;
        else if(res > r3)
            res = r3;


    cout << "Case #" << caseNum << ": ";

    if(res.size())
        cout << res << endl;
    else
        cout << "IMPOSSIBLE" << endl;


}

int main() {
    int t;
    cin >> t;
    REP(i, t) process(i+1);

    return 0;
}
