#include <bits/stdc++.h>

using namespace std;

const int N = 222;

int n, k;
double p[N];

double eval(vector<double> a) {
    map<int, double> prob;
    prob[0] = 1;
    for (auto p : a) {
        map<int, double> new_prob;
        for (auto it : prob) {
            new_prob[it.first + 1] += it.second * p;
            new_prob[it.first - 1] += it.second * (1 - p);
        }
        prob = new_prob;
    }
    return prob[0];
}

double naive() {
    double ans = 0;
    for (int mask = 0; mask < (1 << n); ++mask) if (__builtin_popcount(mask) == k) {
        vector<double> a;
        for (int i = 1; i <= n; ++i) if (mask >> (i - 1) & 1)
            a.push_back(p[i]);
        ans = max(ans, eval(a));
    }
    return ans;
}

int main() {
    //freopen("input.txt", "r", stdin);
    freopen("B-small-attempt0.in", "r", stdin);
    freopen("output.txt", "w", stdout);
    int ntest; cin >> ntest;
    for (int it = 1; it <= ntest; ++it) {
        cout << "Case #" << it << ": ";
        cin >> n >> k;
        for (int i = 1; i <= n; ++i) cin >> p[i];
        cout << setprecision(6) << fixed << naive() << endl;
    }
    return 0;
}
