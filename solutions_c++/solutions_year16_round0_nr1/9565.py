/* Copyright 2015 Rafael Rendón Pablo <rafaelrendonpablo@gmail.com> */
// region Template
#include <bits/stdc++.h>
using namespace std;
typedef long long           int64;
typedef unsigned long long  uint64;
const double kEps   = 10e-8;
const int kMax      = 1000;
const int kInf      = 1 << 30;
// endregion
const int kGoal = 1023;
string f(int n) {
    if (n == 0) {
        return "INSOMNIA";
    }
    int mask = 0;
    int p = 0;
    int count = 0;
    do {
        p += n;
        int v = p;
        while (v > 0) {
            mask |= (1 << (v % 10));
            v /= 10;
        }
        count++;
    } while (mask != kGoal);

    char str[16];
    sprintf(str, "%d", p);
    return string(str);
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int T;
    cin >> T;
    for (int tc = 1; tc <= T; tc++) {
        int N;
        cin >> N;
        printf("Case #%d: %s\n", tc, f(N).c_str());
    }
    return EXIT_SUCCESS;
}

