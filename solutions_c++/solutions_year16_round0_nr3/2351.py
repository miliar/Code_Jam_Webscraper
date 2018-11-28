#include <vector>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <string>
#include <bitset>
#include <iostream>
#include <fstream>
#include <sstream>
#include <algorithm>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <climits>

using namespace std;

struct CoinJam {
    long long mask;
    int len;
    vector<long long> proof;

    CoinJam(long long mask, int len, vector<long long> proof): mask(mask), len(len), proof(proof) {}

    void out() {
        for (int i = len - 1; i >= 0; --i) {
            if (mask >> i & 1) {
                cout << 1;
            } else {
                cout << 0;
            }
        }
        for (int i = 0; i < 9; ++i) {
            cout << ' ' << proof[i];
        }
        cout << endl;
    }
};

vector<pair<int, long long> > ok(int mask) {
    vector<pair<int, long long> > ans;
    for (int base = 2; base <= 10; ++base) {
        long long p = 1;
        long long num = 0;
        for (int i = 0; i < 16; ++i) {
            if (mask >> i & 1) {
                num += p;
            }
            p *= base;
        }
//        cout << mask << ' ' << base << ' ' << num << endl;
        bool prime = true;
        for (int i = 2; i <= num / i; ++i) {
            if (num % i == 0) {
                ans.push_back(make_pair(i, num));
                prime = false;
                break;
            }
        }
        if (prime) {
            ans.clear();
            break;
        }
    }
    return ans;
}

int main() {
    vector<vector<pair<int, long long> > > lefts, rights;
    for (int mask = 1; mask < 1 << 16; mask += 2) {
        vector<pair<int, long long> > divisors = ok(mask);
        if (divisors.size() == 9) {
            //for (int i = 0; i < 9; ++i) cout << divisors[i].first << "," << divisors[i].second << " "; cout << endl;
            rights.push_back(divisors);
            if (mask >= (1 << 15)) {
                lefts.push_back(divisors);
            }
        }
    }
    vector<CoinJam> ans16, ans32;
    int cnt = 0;
    for (int j = 0; j < lefts.size(); ++j) {
        for (int i = 0; i < rights.size(); ++i) {
            vector<long long> proof;
            for (int k = 0; k < 9; ++k) {
                long long g = __gcd(rights[i][k].second, lefts[j][k].second);
                if (g > 1) {
                    proof.push_back(g);
                } else {
                    proof.clear();
                    break;
                }
            }
            if (proof.size() == 9) {
                ans32.push_back(CoinJam(lefts[j][0].second * (1LL << 16) + rights[j][0].second, 32, proof));
            }
        }
        vector<long long> nproof;
        for (int i = 0; i < 9; ++i) {
            nproof.push_back(lefts[j][i].first);
        }
        ans16.push_back(CoinJam(lefts[j][0].second, 16, nproof));
    }
//    cout << ans16.size() << ' ' << ans32.size() << endl;
    int n;
    cin >> n;
    if (n == 16) {
        cout << "Case #1:" << endl;
        for (int i = 0; i < 50; ++i) {
            ans16[i].out();
        }
    } else {
        cout << "Case #1:" << endl;
        for (int i = 0; i < 500; ++i) {
            ans32[i].out();
        }
    }
}

