#include <algorithm>
#include <cassert>
#include <cctype>
#include <cmath>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <ctime>
#include <fstream>
#include <functional>
#include <iostream>
#include <iterator>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <string>
#include <utility>
#include <vector>

using namespace std;

typedef pair<int, int> pii;
const int inf = 1234567890;
int sol;
int n;
vector<pii> A;
void upd(vector<pii> v, const vector<pii> &R) {
    v.push_back(A.back());
    copy(R.rbegin(), R.rend(), back_inserter(v));

    vector<int> cur(n);
    for (int i=0; i<n; ++i) {
        cur[i] = i;
    }
    int cand = 0;
    for (int i=0; i<n; ++i) {
        int what = v[i].second;
        int j = i;
        while (cur[j] != what) {
            ++j;
        }
        if (j > i) {
            cand += j-i;
            for (int k=j; k>i; --k) {
                cur[k] = cur[k-1];
            }
            cur[i] = what;
        }
    }
    sol = min(sol, cand);
}
void go(int at, vector<pii> &L, vector<pii> &R) {
    if (at + 1 == int(A.size())) {
        upd(L, R);
        return;
    }
    L.push_back(A[at]);
    go(at+1, L, R);
    L.pop_back();
    R.push_back(A[at]);
    go(at+1, L, R);
    R.pop_back();
}
int solve() {
    cin >> n;
    A.clear();
    for (int i=0; i<n; ++i) {
        int x;
        cin >> x;
        A.push_back(pii(x, i));
    }

    sort(begin(A), end(A));
    sol = inf;
    vector<pii> l, r;
    go(0, l, r);
    return sol;
}

int main() {
    int T;
    cin >> T;
    cerr << T << " cases total\n";
    for (int t=1; t<=T; ++t) {
        int sol = solve();
        cout << "Case #" << t << ": " << sol << '\n';
        cerr << "Case #" << t << ": " << sol << '\n';
    }
	return 0;
}
