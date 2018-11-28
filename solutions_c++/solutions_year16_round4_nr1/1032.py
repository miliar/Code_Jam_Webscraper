#include <bits/stdc++.h>

#define forn(i, n) for (int i = 0; i < (int)(n); ++i)
#define forr(i, f, t) for (int i = (int)(f); i < (int)(t); ++i)
#define fornr(i, n) for (int i = (int)(n) - 1; i >= 0; --i)
#define forrr(i, f, t) for (int i = (int)(t)-1; i >= (int)(f); --i)
#define all(x) (x).begin(), (x).end()

const int PS = 0;
const int PR = 1;
const int RS = 2;

using namespace std;
template<class C> void mini(C&a4, C b4){a4=min(a4, b4); }
template<class C> void maxi(C&a4, C b4){a4=max(a4, b4); }

int main()
{
    int T;
    cin >> T;
    cout.precision(8);
    for (int casenum = 1; casenum <= T; ++casenum) {
        int N, P, S, R; cin >> N >> R >> P >> S;
        assert(R+P+S == 1 << N);
        vector<string> res;
        forn(i, 3) {
            vector<int> xs = {i};
            forn(j, N-1) {
                vector<int> ts;

                for (auto x : xs) {
                    switch (x) {
                        case PR:
                            ts.push_back(PR);
                            ts.push_back(RS);
                            break;
                        case PS:
                            ts.push_back(PR);
                            ts.push_back(PS);
                            break;
                        case RS:
                            ts.push_back(PS);
                            ts.push_back(RS);
                            break;
                    }
                }
                xs = ts;
            }
            int p = 0, s = 0, r = 0;
            for (auto x : xs) {
                switch (x) {
                    case PR:
                        ++p; ++r;
                        break;
                    case PS:
                        ++p; ++s;
                        break;
                    case RS:
                        ++r; ++s;
                        break;
                }
            }
            if (r == R && s == S && p == P) {
                vector<string> rs;
                for (auto x : xs) {
                    switch (x) {
                        case PR:
                            rs.push_back("PR");
                            break;
                        case PS:
                            rs.push_back("PS");
                            break;
                        case RS:
                            rs.push_back("RS");
                            break;
                    }
                }
                while (rs.size() > 1) {
                    vector<string> ts;
                    for (int j = 1; j < (int)rs.size(); j += 2) {
                        if (rs[j] > rs[j-1]) {
                            ts.push_back(rs[j-1] + rs[j]);
                        } else {
                            ts.push_back(rs[j] + rs[j-1]);
                        }
                    }
                    rs = ts;
                }
                res.push_back(rs[0]);
            }
        }

        if (res.size() > 0) {
            sort(all(res));
            cout << "Case #" << casenum << ": " << res[0] << endl;
        } else {
            cout << "Case #" << casenum << ": IMPOSSIBLE" << endl;
        }
    }
    return 0;
}

