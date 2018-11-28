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

int main() {
    int T;
    cin >> T;
    for (int tc = 1; tc <= T; tc++) {
        string S;
        cin >> S;
        string best = "";
        for (char c : S) {
            string x = "";
            x += c;
            string a = best + x;
            string b = x + best;
            best = max(a, b);
        }
        cout << "Case #" << tc << ": " << best << endl;
    }
    return EXIT_SUCCESS;
}

