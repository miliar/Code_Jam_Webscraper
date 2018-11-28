#include <iostream>
#include <vector>
#include <map>
#include <algorithm>
#include <cassert>
using namespace std;

const int zero = 2000;

struct A {
    int d, w, e, s;
    A(int d, int w, int e, int s): d(d), w(w), e(e), s(s) {}

    friend bool operator<(const A &a, const A &b) {
        return a.d < b.d;
    }
};

int solve(vector< A > &as) {
    vector< int > w(2 * zero + 1);
    int res = 0;
    int d = 0;
    vector< pair< int, int > > patches;
    for (auto &a : as) {
        if (a.d != d) {
            for (auto &p : patches)
                w[p.first] = max(w[p.first], p.second);
            patches.clear();
            d = a.d;
        }
        bool success = false;
        for (int i = a.w + zero; i <= a.e + zero; i++)
            if (w[i] < a.s) {
                success = true;
                patches.push_back(make_pair(i, a.s));
            }
        if (success)
            res++;
        //cerr << d << "	" << a.w << " " << a.e << ": " << success + 0 << endl;
    }
    return res;
}

int main() {
    int T;
    cin >> T;
    for (int i = 1; i <= T; i++) {
        cout << "Case #" << i << ": ";
        int N;
        cin >> N;
        vector< A > as;
        for (int t = 0; t < N; t++) {
            int d, n, w, e, s, dd, dp, ds;
            cin >> d >> n >> w >> e >> s >> dd >> dp >> ds;
            for (int k = 0; k < n; k++)
                as.push_back(A(d + dd * k, 2 * (w + dp * k), 2 * (e + dp * k),
                            s + ds * k));
        }
        sort(as.begin(), as.end());
        cout << solve(as);
        cout << "\n";
    }
    return 0;
}
