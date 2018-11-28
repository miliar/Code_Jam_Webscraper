#include <iostream>
#include <vector>
#include <string>
#include <set>
#include <map>

using namespace std;

typedef long long li;

li isPrime(li n) {
    if (n == 1)
        return 0;
    for (li i = 2; i*i <= n; ++i)
        if (n % i == 0)
            return i;
    return 0;
}

int getBit(li c, int i) {
    return (c >> i) & 1;
}

int getBit(li c, size_t i) {
    return (c >> i) & 1;
}

li getVal(int n, li c, li base) {
    li ans = 0;
    li mul = 1;

    for (int i = 0; i < n; ++i) {
        ans += mul * getBit(c, i);
        mul *= base;
    }

    return ans;
}

bool check(int n, li c, vector<li>& ans) {
    ans.clear();
    if (getBit(c, 0) == 0 || getBit(c, n - 1) == 0)
        throw;

    for (li base = 2; base <= 10; ++base) {
        li d = isPrime(getVal(n, c, base));
        if (d == 0)
            return false;
        ans.push_back(d);
    }

    return true;
}

int main() {
    int tests;
    cin >> tests;

    for (int test = 1; test <= tests; ++test) {
        cout << "Case #" << test << ":" << endl;

        int n, count;
        cin >> n >> count;

        vector<li> ans;
        for (li x = ((1LL << (n - 1)) | 1); x < (1LL << n); x += 2) {
            if (check(n, x, ans)) {
                for (int i = n - 1; i >= 0; --i)
                    cout << getBit(x, i);
                for (size_t i = 0; i < ans.size(); ++i)
                    cout << " " << ans[i];
                cout << endl;

                count--;
                if (count == 0)
                    break;
            }
        }
    }
    return 0;
}
