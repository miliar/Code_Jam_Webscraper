#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <iterator>
#include <utility>
#include <algorithm>
#include <list>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <queue>

using namespace std;

#define pb push_back
#define sz(v) ((long long)v.size())
#define mp make_pair
#define FOR(i,n) for(long long i = 0;i < (n);++i)
#define MOD 1000000007

int erat[(1 << 15)];
vector<int> prime;

int N = 32;
int J = 500;
// int J = 1;

string to_binary(int v) {
    string res(N, '0');
    res[0] = res[N-1] = '1';
    for (size_t i = 0; i < N-2; ++i) {
        if ((v >> i) & 1) {
            res[N-2-i] = '1';
        }
    }
    return res;
}

int main() {
    for (size_t i = 2; i < (1 << 15); ++i) {
        if (!erat[i]) {
            prime.push_back(i);
            for (size_t j = 1; j * i < (1 << 15); ++j) {
                erat[j * i] = 1;
            }
        }
    }

    cerr << "Case #1:" << endl;
    int n_ans = 0;
    vector<int> ans;
    for (size_t v = 0; v < (1ll << (N - 2ll)) && n_ans < J; ++v) {
        bool ok = true;
        ans.clear();
        // cerr << "@@@@@@@@@@@@@@@@@@@@@@" << endl;
        for (size_t base = 2; base <= 10 && ok; ++base) {
            long long val = 1;
            long long p = base;
            for (size_t j = 0; (v >> j) != 0; ++j) {
                val += ((v >> j) & 1) * p;
                if (p * base < p) {
                    cerr << "OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO" << endl;
                    return 1;
                }
                p = p * base;
            }
            // cerr << "########## " << val << " ";
            ok = false;
            for (int d : prime) {
                long long mod = 1;
                for (size_t i = 0; i < N-1; ++i) {
                    mod = (mod * base) % d;
                }
                // cerr << mod << endl;
                if ((val + mod) % d == 0) {
                    ok = true;
                    ans.push_back(d);
                    break;
                }
            }
        }
        if (ok) {
            cout << to_binary(v);
            for (int a : ans) {
                cout << " " << a;
            }
            cout << endl;
            ++n_ans;
        }
    }
}