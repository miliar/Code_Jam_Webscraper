#include <iostream>
#include <ctime>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int isprime(long long n) {
    for (long long i = 2; i * i <= n; i++) {
        if (n % i == 0)return i;
    }
    return -1;
}

bool ok(string s) {
    for (int base = 2; base <= 10; base++) {
        long long n = 0;
        for (char c : s) {
            n *= base;
            n += c - '0';
        }
        if (isprime(n) == -1)return false;
    }
    return true;
}


int main() {
//    freopen("input.txt", "r", stdin);
//    freopen("output.txt", "w", stdout);
    int n;
    cin >> n;
    cin >> n;
    int j;
    cin >> j;
    vector<string> res;
    for (int i = 1 + (1 << (n - 1)); ; i += 2) {
        string bin = "";
        int k = i;
        while (k) {
            if (k % 2) {
                bin = "1" + bin;
            } else {
                bin = "0" + bin;
            }
            k /= 2;
        }
        if (ok(bin)) {
            res.push_back(bin);
        }
        if (res.size() == j)break;
    }

    for (string s: res) {
        cout << s << " ";
        for (int base = 2; base <= 10; base++) {
            long long n = 0;
            for (char c : s) {
                n *= base;
                n += c - '0';
            }
//            cout << n << " " << isprime(n) << endl;
            cout << isprime(n) << " ";

        }
        cout << endl;
    }

    return 0;
}