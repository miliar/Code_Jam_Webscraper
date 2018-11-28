#include <map>
#include <set>
#include <stack>
#include <cmath>
#include <queue>
#include <vector>
#include <cstdio>
#include <string>
#include <cstring>
#include <cstdlib>
#include <iostream>
#include <algorithm>

using namespace std;

const int max_n = 55, inf = 1111111111;

int n, m, a[max_n];
vector<int> ans;

bool get_bit(int x, int poz) {
    return (bool) (x & (1 << poz));
}

bool is_prime(int q) {
    for (int i = 2; i <= 30; ++i) {
        long long x = 0, pw = 1;
        for (int j = n - 1; j >= 0; --j) {
            x += (pw * a[j]) % i;
            x %= i;
            pw *= q;
            pw %= i;
        }
        if (x == 0) {
            return false;
        }
    }
    return true;
}

bool ok() {
    for (int i = 2; i <= 10; ++i) {
        if (is_prime(i)) {
            return false;
        }
    }
    return true;
}

int main() {
    //freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    n = 32;
    m = 500;
    for (int i = 0; i < (1 << (n - 2)); ++i) {
        a[0] = 1;
        a[n - 1] = 1;
        for (int j = 0; j < n - 2; ++j) {
            a[j + 1] = get_bit(i, j);
        }
        if (ok()) {
            ans.push_back(i);
            //cout << ans.size() << endl;
        }
        if (ans.size() == m) {
            break;
        }
    }
    printf("Case #1:\n");
    for (int k = 0; k < ans.size(); ++k) {
        printf("1");
        a[0] = a[n - 1] = 1;
        for (int j = 0; j < n - 2; ++j) {
            a[j + 1] = get_bit(ans[k], j);
            printf("%d", a[j + 1]);
        }
        printf("1 ");
        for (int q = 2; q <= 10; ++q) {
            for (int i = 2; i <= 30; ++i) {
                long long x = 0, pw = 1;
                for (int j = n - 1; j >= 0; --j) {
                    x += (pw * a[j]) % i;
                    x %= i;
                    pw *= q;
                    pw %= i;
                }
                if (x == 0) {
                    printf("%d ", i);
                    break;
                }
            }
        }
        printf("\n");
    }
    return 0;
}
