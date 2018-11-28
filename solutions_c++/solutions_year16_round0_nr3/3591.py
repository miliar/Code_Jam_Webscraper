#include <iostream>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <vector>
using namespace std;

long long mypow[11][17];

void calcMypow() {
    for (int base = 2; base <= 10; base++) {
        long long res = 1;
        for (int pot = 0; pot < 16; pot++) {
            mypow[base][pot] = res;
            res *= base;
        }
    }
}

long long getNumber(int mask, int base) {
    long long ret = 0;
    for (int i = 0; i < 16; i++) {
        if (mask & (1 << i)) {
            ret += mypow[base][i];
        }
    }
    return ret;
}
vector <int> ans;
bool checkPrime(long long num) {
    bool ret = true;
    for (long long i = 2; i < min(1955555550000000000LL, (long long)(sqrt(num) + 5)); i++) {
        if (num % i == 0) {
            ret = false;
            ans.push_back(i);
            break;
        }
    }
    return ret;
}

void ispis(int num) {
//    cout << num << " ";
//    cout << (num & (1 << 16)) << " ";
    for (int i = 15; i >= 0; i--) {
        if (num & (1 << i))
            cout << '1';
        else
            cout << '0';
    }
    cout << " ";
}

int main () {
    int n = 16;
    int koliko = 50;
    int nasao = 0;
    int a, b, c;
    cin >> a >> b >> c;
                cout << "Case #1:" << endl;
    calcMypow();
    for (int i = (1 << 15) + 1; i < (1 << 16); i += 2) {
        bool valid = 1;
        ans.clear();
        for (int base = 2; base <= 10; base++) {
            if (checkPrime(getNumber(i, base)))
                valid = 0;
        }
        if (valid) {
            nasao++;
            ispis(i);
            for (int i = 0; i < 9; i++)
                cout << ans[i] << " ";
            cout << endl;
        }
        if (nasao == koliko)
            break;

    }
    return 0;
}
