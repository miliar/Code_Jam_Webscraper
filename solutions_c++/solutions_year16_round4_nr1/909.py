#include <bits/stdc++.h>

using namespace std;

const int outcome[][3] = {
    {
        0, 1, -1
    },
    {
        -1, 0, 1
    },
    {
        1, -1, 0
    }
};

int N, R, P, S;
int a[5000];

bool gen(int c) {
    vector <int> v;
    v.push_back(c);
    for (int i = 0; i < N; ++i) {
        vector <int> tmp;
        for (int j = 0; j < v.size(); ++j)
            if (v[j] == 0)
                tmp.push_back(0), tmp.push_back(1);
            else if (v[j] == 1)
                tmp.push_back(1), tmp.push_back(2);
            else
                tmp.push_back(2), tmp.push_back(0);
        v = tmp;
    }
    int cnt[3];
    cnt[0] = cnt[1] = cnt[2] = 0;
    for (int i = 0; i < v.size(); ++i)
        ++cnt[v[i]];
//    cout << endl;
    if (cnt[0] != P || cnt[1] != R || cnt[2] != S) return false;
    for (int i = 0; i < (1 << N); ++i)
        a[i] = v[i];
    return true;
}

string sortRes(int L, int R) {
    if (L == R) {
        if (a[L] == 0)
            return "P";
        else if (a[L] == 1)
            return "R";
        else
            return "S";
    }
    int pivot = (R + L) >> 1;
    string leftR = sortRes(L, pivot), rightR = sortRes(pivot + 1, R);
    if (leftR < rightR)
        return leftR + rightR;
    else
        return rightR + leftR;
}

int main() {
    freopen("A-large.in", "r", stdin);
    freopen("output.txt", "w", stdout);
    ios_base::sync_with_stdio(0);
    int T;
    cin >> T;
    for (int t = 1; t <= T; ++t) {
        cin >> N >> R >> P >> S;
        bool found = 0;

        for (int i = 0; i < 3; ++i) {
            if (!gen(i)) continue;
            string res = sortRes(0, (1 << N) - 1);
            cout << "Case #" << t << ": " << res << endl;
            found = 1;
        }
        if (!found)
            cout << "Case #" << t << ": IMPOSSIBLE" << endl;
    }
}
