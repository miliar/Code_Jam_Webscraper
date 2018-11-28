#include <bits/stdc++.h>
using namespace std;

int winners[20];
int tree[4 * 4096];

// bool solve(int no) {
// }

int n, r, p, s;
int bas;

void solveprob() {
    cin >> n >> r >> p >> s;
    // special cases!

    bas = 1;
    for (int i = 0; i < n; ++i)
        bas *= 2;

    for (int i = 0; i < 4 * 4096; ++i)
        tree[i] = -1;
}

char winner(char a, char b) {
    if (a == 'R' && b == 'S')
        return 'R';
    if (a == 'R' && b == 'P')
        return 'P';
    if (a == 'S' && b == 'P')
        return 'S';
    if (a == 'S' && b == 'R')
        return 'R';
    if (a == 'P' && b == 'S')
        return 'S';
    if (a == 'P' && b == 'R')
        return 'P';
    return '0';
}

bool check(string s) {
    if (s.size() == 1)
        return true;
    string s2;
    for (int i = 0; i < s.size(); i += 2) {
        if (s[i] == s[i + 1])
            return false;
        s2.push_back(winner(s[i], s[i + 1]));
    }
    return check(s2);
}

void solveprob2() {
    cin >> n >> r >> p >> s;
    string v;
    for (int i = 0; i < r; ++i)
        v.push_back('R');
    for (int i = 0; i < p; ++i)
        v.push_back('P');
    for (int i = 0; i < s; ++i)
        v.push_back('S');
    sort(v.begin(), v.end());

    do {
        if (check(v)) {
            cout << v << endl;
            return;
        }
    } while (next_permutation(v.begin(), v.end()));
    cout << "IMPOSSIBLE" << endl;
}

int main() {
    int ts;
    cin >> ts;
    for (int t = 1; t <= ts; ++t) {
        cout << "Case #" << t << ": ";
        solveprob2();
    }
}
