//
// Created by Дмитрий Новик on 09.04.16.
//

#include <iostream>
#include <set>
#include <vector>

using namespace std;

vector<long long> create(long long mask, int n) {
    vector<long long> res(static_cast<size_t >(n), 0);

    for (int i = 0; i < n; ++i) {
        res[n - 1 - i] = mask % 2;
        mask /= 2;
    }

    return res;
}

inline long long find_devider(long long num) {
    for (long long i = 2; i * i <= num; ++i) {
        if (num % i == 0) {
            return i;
        }
    }
    return -1;
}

long long create_num(vector<long long>& mask, int base) {
    long long res = 1;
    for (size_t i = 0; i < mask.size(); ++i) {
        res *= base;
        res += mask[i];
    }
    res *= base;
    res++;
//    cerr << base << " " << res << "\n";
    return find_devider(res);
}

int main() {
    freopen("main.in", "r", stdin);
    freopen("main.out", "w", stdout);

    int t;
    cin >> t;

    for (int test = 0; test < t; ++test) {
        int n, j;
        cin >> n >> j;

        cout << "CASE #" << test + 1 << ":\n";
        int ans = 0;

        for (long long i = 0; i < (1LL << (n - 2)); ++i) {
            vector<long long> mask = create(i, n - 2);
            vector<long long> deviders;

            for (int k = 2; k < 11; ++k) {
                long long tmp = create_num(mask, k);
                if (tmp != -1) {
                    deviders.push_back(tmp);
                }
            }

            if (deviders.size() == 9) {
                ans++;
                cout << 1;
                for (size_t k = 0; k < mask.size(); ++k)
                    cout << mask[k];
                cout << 1;

                for (size_t k = 0; k < deviders.size(); ++k) {
                    cout << " " << deviders[k];
                }
                cout << "\n";

                if (ans == j)
                    goto finish;
            }
        }
    }
    finish:
    return 0;
}