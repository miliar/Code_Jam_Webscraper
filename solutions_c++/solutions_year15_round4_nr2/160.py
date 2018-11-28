#include <cassert>
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
#define FOR(i,n) for(int i = 0;i < (n);++i)

long long MOD = 1000000007;

int T;
vector<pair<long double, long double>> r;

int main() {
    cin >> T;
    FOR(itest, T) {
        r.clear();
        int n;
        long double v,x;
        cin >> n >> v >> x;
        FOR(i, n) {
            pair<long double, long double> t;
            cin >> t.second >> t.first;
            r.push_back(t);
        }
        sort(r.begin(), r.end());
        bool bbb = true;
        if (r[0].first > x + 1e-6 || r[n-1].first < x - 1e-6) {
            n = 0;
            bbb = false;
        }

        long double sum_v = 0;
        while (bbb) {
            if (n == 0) {
                break;
            }
            long double sum_t = 0;
            long double sum = 0;
            FOR(i, n) {
                sum_t += r[i].first * r[i].second;
                sum += r[i].second;
            }
            long double t = sum_t / sum;
            if (abs(x - t) < 1e-8) {
                sum_v = sum;
                break;
            }
            if (t > x) {
                auto it = r.end();
                --it;
                long double t1 = it->first;
                long double dv = abs((sum_t - sum * x) / (x - t1));
                // cerr << t << " " << dv << " " << it->second << endl;
                if (dv > it->second){
                    r.erase(it);
                    --n;
                }
                else {
                    sum_v = sum - dv;
                    break;
                }
            } else {
                auto it = r.begin();
                long double t1 = it->first;
                long double dv = abs((sum_t - sum * x) / (x - t1));
                if (dv > it->second) {
                    r.erase(it);
                    --n;
                }
                else {
                    sum_v = sum - dv;
                    break;
                }
            }
        }

        if (n == 0 || abs(sum_v) < 1e-12)
            cout << "Case #" << (itest + 1) << ": " << "IMPOSSIBLE" << endl;
        else
            cout  << std::fixed << std::setprecision(9) << "Case #" << (itest + 1) << ": " << v / sum_v << endl;
    }
}