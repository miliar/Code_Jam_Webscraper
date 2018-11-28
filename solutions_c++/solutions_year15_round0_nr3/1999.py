#include <bits/stdc++.h>

using namespace std;

#define REP(i, from, to) for (int i = (from); i < (to); ++i)
#define FOR(i, n) REP(i, 0, (n))
#define ALL(x) x.begin(), x.end()
#define SIZE(x) (int)x.size()
#define PB push_back
#define MP make_pair

typedef long long i64;

typedef vector<int>    VI;
typedef vector<VI>     VVI;
typedef vector<string> VS;
typedef vector<VS>     VVS;
typedef pair<int, int> PII;

PII MUL_TABLE[4][4] = {
    {PII(0, 1), PII(1, 1), PII(2, 1), PII(3, 1)},
    {PII(1, 1), PII(0, -1), PII(3, 1), PII(2, -1)},
    {PII(2, 1), PII(3, -1), PII(0, -1), PII(1, 1)},
    {PII(3, 1), PII(2, 1), PII(1, -1), PII(0, -1)},
};

PII multiply(PII const& a, PII const& b) {
    PII res = MUL_TABLE[a.first][b.first];
    res.second *= a.second * b.second;
    if (!res.second) throw 10;
    return res;
}

PII findMul(PII const& a, PII const& c) {
    vector<PII> res;
    FOR (term, 4) for (int sign : {-1, 1}) {
        PII const b(term, sign);
        if (multiply(a, b) == c) {
            res.PB(b);
        }
    }

    if (SIZE(res) > 1) throw 10;
    return *res.begin();
}

int main() {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);

    ios_base::sync_with_stdio(false);

    int tests;
    cin >> tests;

    FOR (t, tests) {
        int l, x;
        cin >> l >> x;
        string s;
        cin >> s;

        string const copy = s;
        while (--x > 0) s += copy;

        int const n = SIZE(s);
        bool ok = false;
        vector<PII> partialLeft(n);
        VI iPos;

        //cout << "Left:\n";
        FOR (i, n) {
            PII const curTerm(s[i] - 'i' + 1, 1);
            if (i == 0)
                partialLeft[i] = curTerm;
            else
                partialLeft[i] = multiply(partialLeft[i - 1], curTerm);

            if (partialLeft[i] == PII(1, 1))
                iPos.PB(i);

            //cout << partialLeft[i].first << " " << partialLeft[i].second << endl;
        }

        vector<PII> partialRight(n);
        VI kPos;

        //cout << "Right:\n";
        FOR (i, n) {
            PII const curTerm(s[n - i - 1] - 'i' + 1, 1);
            if (i == 0)
                partialRight[n - i - 1] = curTerm;
            else
                partialRight[n - i - 1] = multiply(curTerm, partialRight[n - i]);

            if (partialRight[n - i - 1] == PII(3, 1))
                kPos.PB(n - i - 1);

            //cout << partialRight[n - i - 1].first << " " << partialRight[n - i - 1].second << endl;
        }

        FOR (a, SIZE(iPos)) {
            FOR (b, SIZE(kPos)) {
                int const i = iPos[a];
                int const j = kPos[b];
                if (j - i <= 1) continue;

                PII const middle = findMul(partialLeft[i], partialLeft[j - 1]);
                if (middle == PII(2, 1)) {
                    ok = true;
                    break;
                }
            }

            if (!ok) break;
        }

        cout << "Case #" << t + 1 << ": " << (ok ? "YES" : "NO") << endl;
    }

    return 0;
}
