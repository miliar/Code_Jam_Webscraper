#include<iostream>
#include<cmath>
#include<vector>
#include<algorithm>

using namespace std;

class Solution {
public:
    Solution(int n, vector<vector<long long>> & p): n(n), p(p) {}
    void solve(int j) {
        for (unsigned i = (1 << (n - 1)) + 1; i < (1 << n); i = i + 2) {
            vector<int> d;
            for (int k = 2; k <= 10; ++k) {
                long long x = base(k, i);
                int y = factor(x);
                if (y == -1) {
                    break;
                } else {
                    d.push_back(y);
                }
            }

            if (d.size() == 9) {
                --j;
                cout << bin(i);
                for (auto & k : d) {
                    cout << " " << k;
                }
                cout << "\n";
                if (j == 0) {
                    break;
                }
            }
        }
    }

    string bin(int x) {
        string res = "";
        while (x != 0) {
            res.push_back((x & 1) + '0');
            x >>= 1;
        }
        reverse(res.begin(), res.end());
        return res;
    }

    long long base(int b, int m) {
        if (b == 2) {
            return m;
        }
        long long res = 0;
        for (int i = 0; i < n; ++i) {
            res += (m & 1) * p[b - 3][i];
            m >>= 1;
        }
        return res;
    }

    int factor(long long x) {
        for (long long i = 2; i <= sqrt(x); ++i) {
            if (x % i == 0) {
                return i;
            }
        }

        return -1;
    }

private:
    int n;
    vector<vector<long long>> & p;
};


int main() {
    vector<vector<long long>> p;
    for (int i = 3; i <= 10; ++i) {
        vector<long long> tmp(16, 1);
        for (int j = 1; j < 16; ++j) {
            tmp[j] = tmp[j - 1] * i;
        }
        p.push_back(tmp);
    }
    int t;
    cin >> t;
    for (int i = 1; i <= t; ++i) {
        cout << "Case #" << i << ":\n";
        int n, j;
        cin >> n >> j;
        Solution sol(n, p);
        sol.solve(j);
    }

    return 0;
}