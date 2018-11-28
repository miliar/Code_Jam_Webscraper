#include <iostream>
#include <cmath>
#include <cstring>
#include <cstdio>
#include <vector>
#include <algorithm>
#include <string>
using namespace std;

class BigInteger {
public:
    const static int N = 20;
    const static int MOD = 10000;
    int len;
    int data[N];

    BigInteger() {
        len = 0;
        memset(data, 0, sizeof(data));
    }

    BigInteger(int val) {
        memset(data, 0, sizeof(data));
        data[0] = val;
        len = 1;
    }

    BigInteger operator*(const int val) {
        BigInteger res(0);
        int g = 0;
        for (int i = 0; i < len + 1; i++) {
            res.data[i] = data[i] * val + g;
            g = res.data[i] / MOD;
            res.data[i] %= MOD;
        }
        res.len = len + 1;
        while (res.len > 0 && res.data[res.len - 1] == 0) --res.len;
        return res;
    }

    BigInteger operator+(const BigInteger b) {
        BigInteger res(0);
        int g = 0;
        for (int i = 0; i < max(b.len, len) + 1; i++) {
            res.data[i] = data[i] + b.data[i] + g;
            g = res.data[i] / MOD;
            res.data[i] %= MOD;
        }
        res.len = max(b.len, len) + 1;
        while (res.len > 0 && res.data[res.len - 1] == 0) --res.len;
        return res;
    }

    int mod(int val) {
        int res = 0;
        for (int i = len; i > 0; i--) {
            res = (res * MOD + data[i - 1]) % val;
        }
        return res;
    }

    void print() {
        printf("%d", data[len - 1]);
        for (int i = len - 1; i > 0; i--) printf("%04d", data[i - 1]);
        printf("\n");
    }
};

BigInteger power[11][100];

bool isPrime(BigInteger n) {
    for (int i = 2; i <= 1000; i++) if (n.mod(i) == 0) return false;
    return true;
}

BigInteger calc(int n, int bit, int base) {
    BigInteger res(1);
    for (int i = 1; bit > 0; i++) {
        if (bit % 2) {
            res = res + power[base][i];
        }
        bit /= 2;
    }
    res = res + power[base][n - 1];
    return res;
}

string getBinaryString(long long n) {
    string res = "";
    while (n) {
        res += '0' + n % 2;
        n /= 2;
    }
    reverse(res.begin(), res.end());
    return res;
}

void solve(int n, int m) {
    vector<long long> vec;
    for (long long i = 0; i < (1LL << (n - 2)) && vec.size() < m; i++) {
        bool flag = true;
        BigInteger val;
        for (int j = 2; j <= 10 && flag; j++) {
            val = calc(n, i, j);
            if (isPrime(val)) {
                flag = false;
            }
        }
        if (flag) {
            vec.push_back(i);
        }
    }
    for (int i = 0; i < vec.size(); i++) {
        long long binary = (1LL << (n - 1)) + (vec[i] << 1) + 1;
        printf("%s ", getBinaryString(binary).data());
        for (int j = 2; j <= 10; j++) {
             BigInteger val = calc(n, vec[i], j);
             for (long long k = 2; k <= 1000; k++) if (val.mod(k) == 0) {
                 cout << k << ' ';
                 break;
             }
        }
        cout << endl;
    }
}

int main() {
    for (int i = 2; i <= 10; i++) {
        power[i][0] = BigInteger(1);
        for (int j = 1; j <= 65; j++) {
            power[i][j] = power[i][j - 1] * i;
        }
    }
    freopen("C.in", "r", stdin);
    int ca, n, m;
    cin >> ca;
    for (int i = 0; i < ca; i++) {
        cin >> n >> m;
        printf("Case #%d:\n", i + 1);
        solve(n, m);
    }
    return 0;
}
