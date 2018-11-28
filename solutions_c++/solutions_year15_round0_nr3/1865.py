#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

vector< vector< pair<char, int> > > dp(256, vector< pair<char, int> > (256));

inline pair<char, int> Prod(char l, char r) {
    if (l == '1') {
        if (r == '1')
            return make_pair('1', 1);
        if (r == 'i')
            return make_pair('i', 1);
        if (r == 'j')
            return make_pair('j', 1);
        if (r == 'k')
            return make_pair('k', 1);
    }
    if (l == 'i') {
        if (r == '1')
            return make_pair('i', 1);
        if (r == 'i')
            return make_pair('1', -1);
        if (r == 'j')
            return make_pair('k', 1);
        if (r == 'k')
            return make_pair('j', -1);
    }
    if (l == 'j') {
        if (r == '1')
            return make_pair('j', 1);
        if (r == 'i')
            return make_pair('k', -1);
        if (r == 'j')
            return make_pair('1', -1);
        if (r == 'k')
            return make_pair('i', 1);
    }
    if (l == 'k') {
        if (r == '1')
            return make_pair('k', 1);
        if (r == 'i')
            return make_pair('j', 1);
        if (r == 'j')
            return make_pair('i', -1);
        if (r == 'k')
            return make_pair('1', -1);
    }

    return make_pair(' ', 0);
}

void FillDp() {
    vector< char > v;
    v.push_back('1');
    v.push_back('i');
    v.push_back('j');
    v.push_back('k');
    for (int i = 0; i < v.size(); ++i)
        for (int j = 0; j < v.size(); ++j)
            dp[v[i]][v[j]] = Prod(v[i], v[j]);
}

inline pair<char, int> Mul(pair<char, int> l, char r) {
    pair<char, int> prod = dp[l.first][r]; // <letter, sign>
    prod.second *= l.second;
    return prod;
}

inline pair<char, int> Get(const vector< vector< pair<char, int> > >& v, int i, int j) {
    if (i > j)
        return make_pair('x', 0);
    return v[i][j];
}

void Solve(const string& s) {
    int n = s.size();
    vector< vector< pair<char, int> > > v(n, vector< pair<char, int> >(n));
    for (int i = 0; i < n; ++i)
        for (int j = i; j < n; ++j) {
            if (i == j)
                v[i][j] = make_pair(s[i], 1);
            else
                v[i][j] = Mul(v[i][j - 1], s[j]);
        }

    static const pair<char, int> ii = make_pair('i', 1);
    static const pair<char, int> jj = make_pair('j', 1);
    static const pair<char, int> kk = make_pair('k', 1);

    for (int i = 0; i < n; ++i) {
        // [0, i]
        // [i + 1, j]
        // [j + 1, n - 1]
        if (Get(v, 0, i) != ii)
            continue;
        for (int j = i; j < n; ++j) {
            if (Get(v, i + 1, j) != jj)
                continue;
            if (Get(v, j + 1, n - 1) != kk)
                continue;
            cout << "YES" << endl;
            return;
        }
    }
    cout << "NO" << endl;
}

void Solve() {
    int n, rep;
    cin >> n >> rep;
    string tmp;
    getline(cin, tmp, '\n');
    getline(cin, tmp, '\n');
    string s;
    for (int i = 0; i < rep; ++i)
        s = s + tmp;
    Solve(s);
}

int main() {
    // ijk:
    //cout << Mul("j", Mul("i", "j"));
    //cout << Mul("i", Mul("j", "i"));
    //cout << Mul("j", Mul("i", Mul("j", Mul("i", Mul("j", "i")))));

    FillDp();
    int t;
    cin >> t;
    for (int i = 1; i <= t; ++i) {
        cout << "Case #" << i << ": ";
        Solve();
    }
    return 0;
}
