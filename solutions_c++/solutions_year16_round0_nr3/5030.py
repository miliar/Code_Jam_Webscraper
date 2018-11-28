#include <iostream>
#include <fstream>
#include <vector>

using namespace std;

long long isPrime(long long k) {
    for (long long s = 2; s * s <= k; ++s) {
        if (k % s == 0)
            return s;
    }
    return 1;
}

vector<int> getVector(long long k, int n) {
    vector<int> v(n);
    for (int i = n - 1; i >= 0; --i) {
        v[i] = (k & 1);
        k >>= 1;
    }
    return v;
}

long long getNumber(const vector<int> &v, long long d) {
    long long n = 0, s = 1;
    for (int i = v.size() - 1; i >= 0; --i) {
        n += (long long)v[i] * s;
        s *= d;
    }
    return n;
}

void showVector(const vector<int> &v) {
    for (int i = 0; i < v.size(); ++i)
        cout << v[i];
}

void solve() {
    long long n, j;
    cin >> n >> j;

    for (long long k = (1ll << (n - 1)) + 1; j > 0 && k < (1ll << n); k += 2) {
        vector<int> v = getVector(k, n);
        bool ok = true;
        for (long long d = 2; d <= 10; ++d)
            ok &= (isPrime(getNumber(v, d)) != 1);
        if (ok) {
            showVector(v);
            cout << " ";
            for (long long d = 2; d <= 10; ++d)
                cout << isPrime(getNumber(v, d)) << " ";
                //cout << "(" << getNumber(v, d) << ", " << isPrime(getNumber(v, d)) << ") ";
            cout << "\n";
            --j;
        }
    }
}

int main()
{
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);

    int T, test;
    for (cin >> T, test = 1; test <= T; ++test) {
        cout << "Case #" << test << ":\n";
        solve();
        cout << "\n";
    }
    return 0;
}
