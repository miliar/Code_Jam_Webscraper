#include <cstdio>
#include <iostream>
#include <cstring>
#include <vector>
#include <algorithm>

using namespace std;

int N, D;
long long S[1000000];
long long M[1000000];
vector<int> children[1000000];
vector<pair<int, int> > mark;

void dfs(int v, long long l, long long h) {
    if (h - l > D) {
        return;
    }
    mark.push_back(make_pair(h - D, 1));
    mark.push_back(make_pair(l + 1, -1));
    for (auto iter = children[v].begin(); iter != children[v].end(); ++iter) {
        int child = *iter;
        dfs(child, min(l, S[child]), max(h, S[child]));
    }
}

int solve() {
//for (int i = 0; i < N; i++) {
//    cout << S[i] << ' ' << M[i] << endl;
//}
    for (int i = 0; i < N; i++) {
        children[i].clear();
    }
    mark.clear();
    for (int i = 1; i < N; i++) {
        children[M[i]].push_back(i);
    }
    dfs(0, S[0], S[0]);

//for (auto iter = mark.begin(); iter != mark.end(); ++iter) {
//    cout << iter->first << ' ' << iter->second << endl;
//}
    sort(mark.begin(), mark.end());
    int count = 0;
    int pos = 0;
    int ans = 0;
    for (auto iter = mark.begin(); iter != mark.end(); ++iter) {
        if (pos != iter->first) {
            if (ans < count) {
                ans = count;
            }
        }
        pos = iter->first;
        count += iter->second;
    }
    if (ans < count) {
        ans = count;
    }
    return ans;
}

int main() {
    int T;
    cin >> T;
    for (int testcase = 1; testcase <= T; testcase++) {
        int ans = 0;
        int As, Cs, Rs, Am, Cm, Rm;
        cin >> N >> D;
        cin >> S[0] >> As >> Cs >> Rs;
        cin >> M[0] >> Am >> Cm >> Rm;
        for (int i = 0; i < N - 1; i++) {
            S[i + 1] = (S[i] * As + Cs) % Rs;
            M[i + 1] = (M[i] * Am + Cm) % Rm;
        }
        for (int i = 1; i < N; i++) {
            M[i] %= i;
        }
        ans = solve();

        cout << "Case #" << testcase << ": ";
        cout << ans;
        cout << endl;
    }
    return 0;
}
