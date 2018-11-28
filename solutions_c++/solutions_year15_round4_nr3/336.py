// {{{
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cstring>
#include <cassert>
#include <algorithm>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <queue>
#include <stack>
#include <set>
#include <map>
#include <complex>
#include <numeric>
#define REP(i, n) for (int i = 0; i < (int) (n); ++i)
#define FOR(i, a, b) for (int i = (int) (a); i <= (int) (b); ++i)
#define FORD(i, a, b) for (int i = (int) (a); i >= (int) (b); --i)
#define FORE(it, c) for (__typeof((c).begin()) it = (c).begin(); it != (c).end(); ++it)
#define SIZE(x) ((int) ((x).size()))
#define DEBUG(x) { cerr << #x << ": " << (x) << endl; }
#define SQR(x) ((x) * (x))
#define INF 1023456789
using namespace std;

template<typename T, typename U> ostream& operator << (ostream& os, const pair<T, U>& p) {
    os << "(" << p.first << "," << p.second << ")"; return os;
}

template<typename T> ostream& operator << (ostream& os, const vector<T>& v) {
    os << "["; FORE(i, v) { if (i != v.begin()) os << ", "; os << *i; } os << "]"; return os;
}

typedef long long LL;
typedef pair<int, int> PI;
typedef pair<int, PI> TRI;
typedef vector<int> VI;
typedef vector<VI> VVI;
// }}}

map<string, int> M;
VVI A, B;

int word_index(const string& word) {
    if (M.count(word))
        return M[word];
    int res = SIZE(M);
    M[word] = res;
    B.push_back(VI());
    return res;
}

int main() {
    int t;
    cin >> t;
    FOR(ti, 1, t) {
        DEBUG(ti);
        M.clear();
        A.clear();
        B.clear();

        int n;
        cin >> n;
        A.resize(n);
        string line;
        getline(cin, line);
        REP(i, n) {
            getline(cin, line);
            stringstream ss(line);
            string word;
            while (ss >> word) {
                int w = word_index(word);
                A[i].push_back(w);
                B[w].push_back(i);
            }
        }

        int res = INF;
        for (int x = 2; x < (1 << n); x += 4) {
            int cnt = 0;
            REP(i, SIZE(B)) {
                bool w0 = false, w1 = false;
                FORE(j, B[i])
                    if (x & (1 << *j)) {
                        w1 = true;
                    } else {
                        w0 = true;
                    }
                cnt += w0 && w1;
            }
            res = min(res, cnt);
        }

        cout << "Case #" << ti << ": " << res << endl;
    }
}
