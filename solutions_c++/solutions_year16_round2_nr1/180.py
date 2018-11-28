#include <bits/stdc++.h>

#define forn(i, n) for (int i = 0; i < (int)(n); ++i)
#define forr(i, f, t) for (int i = (int)(f); i < (int)(t); ++i)
#define fornr(i, n) for (int i = (int)(n) - 1; i >= 0; --i)
#define forrr(i, f, t) for (int i = (int)(t)-1; i >= (int)(f); --i)
#define printvec(v) for (auto e : v) cout << e << ", "; cout << endl;
#define all(x) (x).begin(), (x).end()

using namespace std;
template<class C> void mini(C&a4, C b4){a4=min(a4, b4); }
template<class C> void maxi(C&a4, C b4){a4=max(a4, b4); }

void del(map<char, int> &ccnts, string w) {
    for (char c : w) ccnts[c]--;
}

int main()
{
    int T;
    cin >> T;
    cout.precision(8);
    for (int casenum = 1; casenum <= T; ++casenum) {
        string s;
        cin >> s;
        map<char, int> ccnts;
        vector<int> ncnts(10);

        for (char c : s) ccnts[c]++;
        while (ccnts['Z']) {
            del(ccnts, "ZERO");
            ++ncnts[0];
        }
        while (ccnts['X']) {
            del(ccnts, "SIX");
            ++ncnts[6];
        }
        while (ccnts['W']) {
            del(ccnts, "TWO");
            ++ncnts[2];
        }
        while (ccnts['G']) {
            del(ccnts, "EIGHT");
            ++ncnts[8];
        }
        while (ccnts['H']) {
            del(ccnts, "THREE");
            ++ncnts[3];
        }
        while (ccnts['S']) {
            del(ccnts, "SEVEN");
            ++ncnts[7];
        }
        while (ccnts['V']) {
            del(ccnts, "FIVE");
            ++ncnts[5];
        }
        while (ccnts['F']) {
            del(ccnts, "FOUR");
            ++ncnts[4];
        }
        while (ccnts['O']) {
            del(ccnts, "ONE");
            ++ncnts[1];
        }
        while (ccnts['N']) {
            del(ccnts, "NINE");
            ++ncnts[9];
        }
        for (auto p : ccnts) assert(p.second == 0);
        cout << "Case #" << casenum << ": ";
        forn(i, 10) forn(j, ncnts[i]) cout << i;
        cout << endl;
    }
    return 0;
}

