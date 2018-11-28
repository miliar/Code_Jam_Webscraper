#include <iostream>
#include <cstdio>
#include <vector>
#include <set>
#include <algorithm>
#include <deque>
#include <cmath>
#include <ctime>

using namespace std;

long long pow(long long n, long long m) {
    if (m == 0) return 1L;
    long long a = pow(n, m / 2);
    if (m % 2 == 0) {
        return a * a;
    } else {
        return a * a * n;
    }
}

void printMask(int mask) {
    vector<int> pr_mask;
    while (mask != 0) {
        if (mask % 2 == 0) {
            pr_mask.push_back(0);
        } else {
            pr_mask.push_back(1);
        }
        mask = mask / 2;
    }
    for (int i = pr_mask.size() - 1; i > -1; i--) {
        cout << pr_mask[i];
    }
}

int main() {
    freopen("C-small-attempt0.in", "r", stdin);
    freopen("output.txt", "w", stdout);
    int tests;
    cin >> tests;
    for (int test = 0; test < tests; test++) {
        cout << "Case #" << test + 1 << ": \n";
        long long n, j;
        cin >> n >> j;
        for (int mask = 65536 / 2 + 1; mask < 131072 / 2; mask = mask + 2) {
            long long div[9];
            for (int i = 0; i < 9; ++i) {
                div[i] = 0;
            }
            for (long long base = 2; base < 11; base++) {
                long long res = 0;
                for (int i = 0; i < 16; ++i) {
                    if ((mask & (1 << i)) != 0) {
                        res += pow(base, i);
                    }
                }
                for (long long d = 2; d * d <= res; d++) {
                    if (res % d == 0) {
                        div[base - 2] = d;
                        break;
                    }
                }
                int flag = 0;
                for (int i = 0; i < 9; ++i) {
                    if (div[i] == 0) {
                        flag = 1;
                    }
                }
                if (flag == 1) {
                    continue;
                } else {
                    printMask(mask);
                    cout << " ";
                    for (int i = 0; i < 9; ++i) {
                        cout << div[i] << " ";
                    }
                    cout << "\n";
                    j--;
                }
                if (j == 0) {
                    return 0;
                }
            }
        }
        cout << "\n";
    }
    return 0;
}