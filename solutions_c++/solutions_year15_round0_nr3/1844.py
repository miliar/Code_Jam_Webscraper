#include <iostream>
#include <map>
#include <string>
#include <vector>

using namespace std;

pair<char, bool> mult(pair<char, bool> c1, pair<char, bool> c2) {
    static map<char, map<char, pair<char, bool> > > m;
    if (m.size() == 0) {
        m['1']['1'] = make_pair('1', true);
        m['i']['1'] = make_pair('i', true);
        m['j']['1'] = make_pair('j', true);
        m['k']['1'] = make_pair('k', true);

        m['1']['i'] = make_pair('i', true);
        m['i']['i'] = make_pair('1', false);
        m['j']['i'] = make_pair('k', false);
        m['k']['i'] = make_pair('j', true);

        m['1']['j'] = make_pair('j', true);
        m['i']['j'] = make_pair('k', true);
        m['j']['j'] = make_pair('1', false);
        m['k']['j'] = make_pair('i', false);

        m['1']['k'] = make_pair('k', true);
        m['i']['k'] = make_pair('j', false);
        m['j']['k'] = make_pair('i', true);
        m['k']['k'] = make_pair('1', false);
    }

    pair<char, bool> c = m[c1.first][c2.first];
    if (c1.second == c2.second)
        return c;

    c.second = !c.second;

    return c;
}

pair<char, bool> pow(pair<char, bool> c, long long n) {
    pair<char, bool> res = make_pair('1', true);
    long long power = n;
    pair<char, bool> value = c;

    while (power > 0) {
        if (power % 2 != 0)
            res = mult(res, value);
        value = mult(value, value);
        power >>= 1;
    }

    return res;
}

string toChar(pair<char, bool> c) {
    string s = (!c.second ? "-" : "");
    s.append(1, c.first);
    return s;
}

#define MAXL 10000
pair<char, bool> mults[MAXL][MAXL];

bool valid(int X, string s) {
    string r = s;
    for (int i = 1; i < X; i++)
        s.append(r);
    int N = s.size();

    for (int i = 0; i < N; i++) {
        mults[i][i] = make_pair(s[i], true);
        for (int j = i + 1; j < N; j++)
            mults[i][j] = mult(mults[i][j - 1], make_pair(s[j], true));
    }

    for (int i = 1; i <= N - 2; i++) {
        for (int j = 1; i + j <= N - 1; j++) {
            pair<char, bool> currentI = mults[0][i - 1];
            pair<char, bool> currentJ = mults[i][s.size() - 1 - j];
            pair<char, bool> currentK = mults[s.size() - 1 - (j - 1)][s.size() - 1];

            if (currentI == make_pair('i', true) && currentJ == make_pair('j', true) && currentK == make_pair('k', true))
                return true;
        }
    }

    return false;
}

int main() {
    int T;
    cin >> T;

    for (int i = 1; i <= T; i++) {
        int L, X;
        cin >> L >> X;

        string s;
        cin >> s;

        cout << "Case #" << i << ": " << (valid(X, s) ? "YES" : "NO") << endl;
    }

    return 0;
}
