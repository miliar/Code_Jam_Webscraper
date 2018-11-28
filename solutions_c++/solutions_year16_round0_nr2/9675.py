/* Copyright 2015 Rafael Rendón Pablo <rafaelrendonpablo@gmail.com> */
// region Template
#include <bits/stdc++.h>
using namespace std;
typedef long long           int64;
typedef unsigned long long  uint64;
const double kEps   = 10e-8;
const int kMax      = 1 << 12;
const int kInf      = 1 << 30;
// endregion

bool visited[kMax];
int solve(int state, int n, int goal) {
    queue<int> Q;
    queue<int> S;
    Q.push(state);
    S.push(0);
    memset(visited, false, sizeof visited);
    bool bits[16];
    while (!Q.empty()) {
        int value = Q.front();
        Q.pop();
        int steps = S.front();
        S.pop();
        if (value == goal) {
            return steps;
        }
        visited[value] = true;
        for (int pos = 0; pos < n; pos++) {
            for (int i = 0; i < n; i++) {
                if (value & (1 << i)) {
                    bits[i] = true;
                } else {
                    bits[i] = false;
                }
            }
            for (int i = pos; i < n; i++) {
                bits[i] = !bits[i];
            }
            reverse(bits + pos, bits + n);
            int newMask = 0;
            for (int i = 0; i < n; i++) {
                if (bits[i]) {
                    newMask |= (1 << i);
                }
            }
            if (!visited[newMask]) {
                Q.push(newMask);
                S.push(steps + 1);
            }
        }
    }
    return -1;
}

int main() {
    int T;
    cin >> T;
    for (int tc = 1; tc <= T; tc++) {
        string str;
        cin >> str;
        int mask = 0;
        int n = str.length();
        reverse(begin(str), end(str));

        // init
        memset(visited, false, sizeof visited);

        for (int i = 0; i < n; i++) {
            if (str[i] == '+') {
                mask |= (1 << i);
            }
        }
        printf("Case #%d: %d\n", tc, solve(mask, n, (1 << n) - 1));
    }
    return EXIT_SUCCESS;
}

