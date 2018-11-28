#include <cmath>
#include <iomanip>
#include <iostream>
#include <algorithm>
#include <vector>
#include <utility>
#include <tuple>
#include <set>
#include <cctype>

using namespace std;

#define fs first
#define sc second

typedef long double ld;
typedef long long ll;

ll
readInt()
{
    cin >> noskipws;
    char c;
    int res = 0;
    do {
        cin >> c;
    } while (isspace(c));
    while (c != '.' && !isspace(c)) {
        res = res * 10 + (c - '0');
        cin >> c;
    }
    int add = 0;
    if (c == '.') {
        cin >> c;
        int mult = 1000;
        while (isdigit(c)) {
            add += mult * (c - '0');
            cin >> c;
            mult /= 10;
        }
    }
    return res * 10000 + add;
}

void
process(int id)
{
    cout << "Case #" << id << ": ";
    vector< pair< ll, ll > > pnt;
    int n;
    cin >> n;
    ll v = readInt(), x = readInt();
    x *= v;
    pnt.clear();
    for (int i = 0; i < n; ++i) {
        ll a = readInt(), b = readInt();
        b *= a;
        int ind = 0;
        while (ind < int(pnt.size()) && pnt[ind].sc / pnt[ind].fs != b / a) ++ind;
        if (ind == int(pnt.size())) {
            pnt.push_back({a, b});
        } else {
            pnt[ind] = make_pair(pnt[ind].fs + a, pnt[ind].sc + b);
        }
    }
    sort(pnt.begin(), pnt.end(), [&](const pair< ll, ll > &a, const pair< ll, ll > &b) -> bool
            {
            return a.sc / a.fs < b.sc / b.fs;
            });
    const auto fst = pnt.front(), lst = pnt.back();
    if (fst.sc / fst.fs > x / v || lst.sc / lst.fs < x / v) {
        cout << "IMPOSSIBLE\n";
        return;
    }
    if (fst.sc / fst.fs == x / v) {
        cout << (v + ld(0)) / (fst.fs + ld(0)) << '\n';
        return;
    } else if (lst.sc / lst.fs == x / v) {
        cout << (v + ld(0)) / (lst.fs + ld(0)) << '\n';
        return;
    }
    bool find_pos = false;
    int cnt = pnt.size();
    auto pp = pnt[0];
    pair< ll, ll > fp, sp;
    for (int i = 1; i < cnt && !find_pos; ++i) {
        auto cp = make_pair(pp.fs + pnt[i].fs, pp.sc + pnt[i].sc);
        if (cp.fs * (x / v) < cp.sc) {
            find_pos = true;
            fp = pp, sp = cp;
        } else if (cp.fs * (x / v) == cp.sc) {
            cout << (v + ld(0)) / (cp.fs + ld(0)) << '\n';
            return;
        }
        pp = cp;
    }
    pp = pnt[cnt - 1];
    for (int i = cnt - 2; i >= 0 && !find_pos; --i) {
        auto cp = make_pair(pp.fs + pnt[i].fs, pp.sc + pnt[i].sc);
        if (cp.fs * (x / v) > cp.sc) {
            find_pos = true;
            fp = cp, sp = pp;
        } else if (cp.fs * (x / v) == cp.sc) {
            cout << (v + ld(0)) / (cp.fs + ld(0)) << '\n';
            return;
        }
        pp = cp;
    }
    auto diff = make_pair(fp.fs - sp.fs, fp.sc - sp.sc);
    ld det = ld(v) * ld(diff.sc) - ld(x) * ld(diff.fs);
    ld det1 = ld(fp.fs) * ld(diff.sc) - ld(fp.sc) * ld(diff.fs);
    cout << det / det1 << '\n';
}

int
main()
{
    ios_base::sync_with_stdio(false);
    cout << fixed << setprecision(20);
    int t;
    cin >> t;
    for (int i = 1; i <= t; ++i) {
        process(i);
    }
    return 0;
}
