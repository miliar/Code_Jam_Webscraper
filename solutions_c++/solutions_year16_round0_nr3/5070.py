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

string toBin(int n) {
    string str = "";
    while (n > 0) {
        if (n % 2 == 1) {
            str += "1";
        } else {
            str += "0";
        }
        n /= 2;
    }
    reverse(begin(str), end(str));
    return str;
}

int findDiv(int64 v) {
    int sr = sqrt(v);
    for (int d = 2; d <= sr; d++) {
        if (v % d == 0) {
            return d;
        }
    }
    return -1;
}

bool isJamCoin(int n, int N, vector<int64>& divs) {
    for (int base = 2; base <= 10; base++) {
        int64 v = 0;
        for (int i = N - 1; i >= 0 ; i--) {
            v = v * base;
            if (n & (1 << i)) {
                v += 1;
            }
        }
        int div = findDiv(v);
        if (div == -1) {
            return false;
        }
        //divs.push_back(v);
        divs.push_back(div);
    }
    return true;
}


int main() {
    int T;
    cin >> T;
    for (int tc = 1; tc <= T; tc++) {
        int J, N;
        cin >> N >> J;
        vector<int64> jamcoins;
        vector<vector<int64>> divisors;
        for (int x = 0; x < (1 << (N - 2)); x++) {
            int n = 1 | (x << 1) | (1 << (N - 1));
            vector<int64> divs;
            if (isJamCoin(n, N, divs)) {
                jamcoins.push_back(n);
                divisors.push_back(divs);
            }
            if (int(jamcoins.size()) == J) {
                break;
            }
        }
        printf("Case #%d:\n", tc);
        for (int i = 0; i < int(jamcoins.size()); i++) {
            cout << toBin(jamcoins[i]) << " ";
            for (int j = 0; j < 9; j += 1) {
                cout << divisors[i][j] << " ";
            }
            cout << endl;
        }
    }
    return EXIT_SUCCESS;
}

