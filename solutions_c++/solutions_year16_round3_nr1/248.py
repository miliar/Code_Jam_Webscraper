#include <bits/stdc++.h>

using namespace std;

int cnt[300], id[300];

int T, N;

bool cmp(int a, int b) { return cnt[a] > cnt[b]; }

vector <string> res;

int main() {
    freopen("A-large.in", "r", stdin);
    freopen("output.txt", "w", stdout);
    cin >> T;
    for (int t = 1; t <= T; ++t) {
        cin >> N;
        for (int i = 0; i < N; ++i)
            cin >> cnt[i], id[i] = i;
        res.clear();

        while (1) {
            sort(id, id + N, cmp);
            if (cnt[id[0]] == 0) break;
            if (cnt[id[1]] == 0) {
                if (cnt[id[1]] > 1)
                    res.push_back(string(1, 'A' + id[0]) + string(1, 'A' + id[0])), cnt[id[0]] -= 2;
                else
                    res.push_back(string(1, 'A' + id[0])), cnt[id[0]]--;
            }
            else {
                res.push_back(string(1, 'A' + id[0]) + string(1, 'A' + id[1]));
                cnt[id[0]]--;
                cnt[id[1]]--;
            }
        }
        cout << "Case #" << t << ": ";
        if (res[res.size() - 1].size() == 1) {
            cout << res[res.size() - 1] << " ";
            res.pop_back();
        }
        for (int i = 0; i < res.size(); ++i)
            cout << res[i] <<" ";
        cout << endl;
    }
}
