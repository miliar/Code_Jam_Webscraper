#include <iostream>
#include <vector>
#include <cstdio>
#include <algorithm>
#include <set>

using namespace std;

int best_ans;
set<pair<vector<int>, int> > z;

void brute(vector<int> a, int step) {
    if (step > 9) return;
    if (step >= best_ans) return;
    bool flag = true;
    for (int i = 0; i < a.size(); ++i)
        if (a[i] != 0)
            flag = false;
    if (flag) {
        best_ans = min(step, best_ans);
        return;
    }

    sort(a.rbegin(), a.rend());
    if (z.find({a, step}) != z.end()) return;
    z.insert({a, step});

    vector<int> tmp = a;
    for (int i = 0; i < tmp.size(); ++i)
        if (tmp[i] != 0) --tmp[i];
    brute(tmp, step + 1);

    for (int i = 0; i < a.size(); ++i) {
        if (a[i] <= 1) continue;
        for (int j = 1; j < a[i]; ++j) {
            vector<int> tmp = a;
            tmp[i] = j;
            tmp.push_back(a[i] - j);
            brute(tmp, step + 1);
        }
    }
}

int main() {
    int tests;
    cin >> tests;
    for (int test = 1; test <= tests; ++test) {
        int D;
        cin >> D;
        vector<int> a(D);
        for (int i = 0; i < D; ++i)
            cin >> a[i];
        best_ans = 1e9;
        z.clear();
        brute(a, 0);
        printf("Case #%d: %d\n", test, best_ans);
    }
}
