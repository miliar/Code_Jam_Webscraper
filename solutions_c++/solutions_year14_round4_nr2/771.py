#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>

using namespace std;

const int INF = (int)1e6;

vector <int> A;
vector <int> B;
vector <int> S;

int ans;

void update() {
    int cnt = 0, i, j, n = S.size();
    vector <int> C(A.begin(), A.end());
    for (j = n - 1; j >= 0; --j) {
        for (i = 0; C[i] != B[j]; ++i);
        if (i < j) {
            for (; i != j; ++i) {
                swap(C[i], C[i + 1]);
                cnt++;
            }
        }
        if (i > j) {
            for (; i != j; --i) {
                swap(C[i], C[i - 1]);
                cnt++;
            }
        }
    }
    if (cnt < ans)
        ans = cnt;
}

void gen(int v, int l, int r) {
    if (v == S.size()) {
        update();
        return;
    }
    B[l] = S[v];
    gen(v + 1, l + 1, r);
    if (l != r) {
        B[r] = S[v];
        gen(v + 1, l, r - 1);
    }
}

void solve_slow() {
    ans = INF;
    int n, i;
    cin >> n;
    A.resize(n);
    B.resize(n);
    S.resize(n);
    for (i = 0; i < n; ++i) {
        cin >> A[i];
        S[i] = A[i];
    }
    sort(S.begin(), S.end());
    gen(0, 0, n - 1);
    cout << ans << endl;
}

void mmove(int i, int j) {
    if (i < j) {
        for (; i != j; ++i) {
            swap(A[i], A[i + 1]);
        }
    }
    if (i > j) {
        for (; i != j; --i) {
            swap(A[i], A[i - 1]);
        }
    }
}

void solve_fast() {
    ans = 0;
    int n, i, j;
    cin >> n;
    A.resize(n);
    S.resize(n);
    for (i = 0; i < n; ++i) {
        cin >> A[i];
        S[i] = A[i];
    }
    sort(S.begin(), S.end());
    int l, r;
    l = 0;
    r = n - 1;
    for (j = 0; j < n; ++j) {
        for (i = l; A[i] != S[j]; ++i);
        if (abs(i - l) < abs(i - r)) {
            ans += abs(i - l);
            for (; i != l; --i) {
                swap(A[i], A[i - 1]);
            }
            l++;
        }
        else {
            ans += abs(i - r);
            for (; i != r; ++i) {
                swap(A[i], A[i + 1]);
            }
            r--;
        }
    }
    cout << ans << endl;
}

int main() {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);

    int t, T;
    cin >> T;
    for (t = 1; t <= T; ++t) {
        printf("Case #%d: ", t);
        solve_fast();
    }
    return 0;
}