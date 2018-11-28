#include <iostream>
#include <vector>
#include <cstdio>
#include <cstring>
#include <map>
#include <set>
#include <algorithm>
using namespace std;

int N, K;
double A[205], ans;
double B[205];
double f[205][205];
double get(vector<double> &C) {
    for (int i = 1; i <= K; i++)
        B[i] = C[i-1];
    memset(f, 0, sizeof f);
    f[0][0] = 1;
    for (int i = 0; i < K; i++)
        for (int j = 0; j <= i; j++) {
            f[i+1][j+1] += f[i][j] * B[i+1];
            f[i+1][j] += f[i][j] * (1-B[i+1]);
        }
    return f[K][K/2];
}

int main() {
    freopen("B-large.in", "r", stdin);
    freopen("B-l.out", "w", stdout);
    int testcase;
    cin >> testcase;
    for (int o = 1; o <= testcase; o++) {
        printf("Case #%d: ", o);
        cin >> N >> K;
        for (int i = 1; i <= N; i++)
            cin >> A[i];
        sort(A, A + N + 1);
        vector<double> tmp;
        ans = 0;
        for (int x = 0; x <= K; x++) {
            tmp.clear();
            for (int i = 1; i <= x; i++)
                tmp.push_back(A[i]);
            for (int j = N - (K-x)+1; j <= N; j++)
                tmp.push_back(A[j]);
            ans = max(ans, get(tmp));
        }
        printf("%.8f\n", ans);
    }
}
