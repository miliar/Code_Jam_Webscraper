//
// Created by 冯斯聪 on 16/4/8.
//
#include <string>
#include <unordered_map>
#include <iostream>
using namespace std;

void countOneNumber(long x, unordered_map<int, int> &m, int &res) {
    while (x != 0) {
        long d = x%10;
        x = x/10;
        res |= m[d];
    }
}

int countSheep(long N) {
    if (N==0) {
        return 0;
    }

    int res = 0;
    unordered_map<int, int> m;
    int add = 1;
    for (int i = 0; i < 10; ++i) {
        m[i] = add<<i;
    }
    int all = 0b1111111111;
    long acc = N;
    countOneNumber(acc, m, res);
    while (res != all) {
        acc += N;
        countOneNumber(acc, m, res);
    }
    return acc;
}

int main(void) {
    int T;
    cin >> T;
    for (int i = 0; i < T; ++i) {
        int N;
        cin >> N;
        int ret = countSheep(N);
        cout << "Case #" << i+1 << ": ";
        if (N==0) cout << "INSOMNIA" << endl;
        else cout << ret << endl;
    }
    return 1;
}
