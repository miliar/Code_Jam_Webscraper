#include <iostream>
#include <cstdlib>
#include <iomanip>
#include <cstring>
#include <string>
#include <algorithm>
#include <queue>
#include <map>
#include <set>
#include <stack>
#include <vector>
#include <ctime>
#include <fstream>
#include <cmath>

using namespace std;

#define y1 ym37s62rw
#define x1 xm2ash4ad
#define pb push_back
#define mp make_pair
#define F first
#define S second

const int INF = 1000000007;
const long long INFll = 1000000007000000007ll;
const int MOD = 1000000007;

inline string tr(string e, int r, int p, int s, int n) {
    for (int i = 0; i < n; ++i) {
        string t = "";
        for (int i = 0; i < e.size(); ++i) {
            if (e[i] == 'S') {
                t += "PS";
            }
            if (e[i] == 'R') {
                t += "RS";
            }
            if (e[i] == 'P') {
                t += "PR";
            }
        }
        e = t;
    }
    for (int i = 0; i < e.size(); ++i) {
        if (e[i] == 'P')
            p--;
        if (e[i] == 'R')
            r--;
        if (e[i] == 'S')
            s--;
    }
    if (p != 0 || s != 0 || r != 0) {
        for (int i = 0; i < e.size(); ++i)
            e[i] = 'Z';
    }
    return e;
}

inline void srt(string& s, int n) {
    if (n <= 0)
        return;
    string s1 = "";
    string s2 = "";
    for (int i = 0; i < s.size() / 2; ++i) {
        s1 += s[i];
    }
    for (int i = s.size() / 2; i < s.size(); ++i) {
        s2 += s[i];
    }
    srt(s1, n - 1);
    srt(s2, n - 1);
    if (s1 > s2)
        swap(s1, s2);
    s = s1 + s2;
}

int main() {

    ios_base::sync_with_stdio(0);

#ifdef DEBUG
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
#else
#endif
    int n;
    cin >> n;

    for (int i = 0; i < n; ++i) {
        int n, r, p, s;
        cin >> n >> r >> p >> s;
        cout << "Case #" << i + 1 << ": ";
        vector<string> v(3);
        v[0] = tr("P", r, p, s, n);
        v[1] = tr("R", r, p, s, n);
        v[2] = tr("S", r, p, s, n);
        srt(v[0], n);
        srt(v[1], n);
        srt(v[2], n);
        sort(v.begin(), v.end());
        if (v[0][0] == 'Z') {
            cout << "IMPOSSIBLE" << endl;
        }
        else
            cout << v[0] << endl;
    }

    return 0;
}
