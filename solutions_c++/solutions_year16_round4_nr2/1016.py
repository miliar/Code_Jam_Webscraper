#include <iostream>
#include <cassert>
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

long double res[250][250];

int main() {
    int T;
    cin >> T;
    FOR(iter, T) {
        cout << "Case #" << iter + 1 << ": ";
        int n, k;
        cin >> n >> k;
        vector<double> v(n);
        FOR(i, n) {
            cin >> v[i];
        }
        sort(v.begin(), v.end());

        long double best = 0.0;
        for (size_t i = 0; i < (1 << v.size()); ++i) {
            vector<double> p;
            FOR(j, v.size()) {
                if (i & (1 << j)) {
                    p.push_back(v[j]);
                }
            }
            if (p.size() != k) {
                continue;
            }

            res[0][0] = 1.0;
            FOR(i, p.size()) {
                res[i+1][0] = 0;
                FOR(j, 210) {
                    res[i+1][j+1] = 0;
                    res[i+1][j] += res[i][j] * (1 - p[i]);
                    res[i+1][j+1] += res[i][j] * p[i];
                }
            }
            best = max(best, res[k][k/2]);
        }

        // FOR(i, p.size()) {
        //     cout << p[i] << endl;
        // }

        cout << std::fixed << std::setprecision(9) << best << endl;

    }
  
}