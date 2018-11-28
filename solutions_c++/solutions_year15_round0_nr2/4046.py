#include <bits/stdc++.h>
using namespace std;

#define INF 2000000000
#define maxN 1005


int TC;
int D;
int P[maxN];

int solve(vector <int> v, int step) {
    sort(v.begin(), v.end());

    if (v[v.size() - 1] == 0) return 0;

    if (step >= 9) return INF;

    vector<int> v1;
    for (int i = 0; i < v.size(); i++) {
        v1.push_back(v[i] - 1);
    }
    int res1 = solve(v1, step + 1) + 1;
    int haft = v[v.size() - 1] / 2;

    vector<int> v2;
    for (int i = 0; i < v.size() - 1; i++) {
        v2.push_back(v[i]);
    }

    int res2 = INF;
    if (haft >= 1) {
        v2.push_back(haft);
        v2.push_back(haft + (v[v.size() - 1] % 2 == 1));
        res2 = solve(v2, step + 1) + 1;
    }

    vector<int> v3;
    for (int i = 0; i < v.size() - 1; i++) {
        v3.push_back(v[i]);
    }

    int res3 = INF;
    int third = v[v.size() - 1] / 3;
    if (third >= 1) {
        v3.push_back(third + (v[v.size() - 1] % 3 == 1));
        v3.push_back(third + (v[v.size() - 1] % 3 == 2));
        v3.push_back(third);
        res3 = solve(v3, step + 1) + 2;
    }

    return (min(res1, min(res2, res3)));
}

int main() {
    #ifndef ONLINE_JUDGE
    freopen("B-small-attempt0.in", "r", stdin);
    freopen("test.out", "w", stdout);
    #endif // ONLINE_JUDGE

    cin >> TC;
    for (int cs = 0; cs < TC; cs++) {
        cin >> D;
        vector <int> v;
        for (int i = 0; i < D; i++) {
            cin >> P[i];
            v.push_back(P[i]);
        }
        cout << "Case #" << cs + 1 << ": " << solve(v, 0) << endl;
    }

    return 0;
}
