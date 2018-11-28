#define _USE_MATH_DEFINES

#include <algorithm>
#include <deque>
#include <iostream>
#include <iterator>
#include <set>
#include <string>
#include <map>
#include <vector>
#include <queue>

#include <cassert>
#include <cstdio>
#include <cstdlib>
#include <ctime>
#include <cmath>
#include <climits>
#include <cstring>

using namespace std;

typedef long long ll;

int const INF = 1000 * 1000 * 1000 + 11;
ll const LINF = (ll)INF * INF;


void recalc(map<int, double> &res, double p) {
    map<int, double> next;
    
    for (auto it = res.begin(); it != res.end(); ++it) {
        next[it->first + 1] += it->second * p;
        next[it->first - 1] += it->second * (1 - p);
    }
    
    res = next;
}

double solve(int n, int k, vector<double> const &_p) {
    auto p = _p;
    
    sort(p.begin(), p.end());
    
    int idx = 0;
    
    map<int, double> res;
    res[0] = 1;
    
    
    while (idx < k / 2 && p[idx] <= 0.5 && p[n - idx - 1] >= 0.5) {
        recalc(res, p[idx]);
        recalc(res, p[n - idx - 1]);
        
        ++idx;
    }
    
    if (idx < k / 2) {
        if (p[idx] < 0.5) {
            for (int i = 0; i != k - idx * 2; ++i) {
                recalc(res, p[n - idx - 1 - i]);
            }
        } else {
            for (int i = 0; i != k - idx * 2; ++i) {
                recalc(res, p[idx + i]);
            }
        }
        
    }
    
    return res[0];
}


double choose(int n, int k, vector<double> const &p, map<int, double> &res) {
    if (p.size() - n < k) {
        return 0;
    }
    if (n == p.size()) {
        return res[0];
    }
    
    map<int, double> temp = res;
    recalc(temp, p[n]);
    double first = choose(n + 1, k - 1, p, temp);
    
    return max(first, choose(n + 1, k, p, res));
}

double stupid(int n, int k, vector<double> const &p) {
    map<int, double> res;
    res[0] = 1;
    
    return choose(0, k, p, res);
}


int main() {
    //freopen("/Users/iskhakovt/Downloads/A-small-attempt0.in", "r", stdin);
    //freopen("/Users/iskhakovt/out.txt", "w", stdout);
    
    int tests;
    cin >> tests;
    
    cout.precision(20);
    
    for (int t = 0; t != tests; ++t) {
        int n, k;
        cin >> n >> k;
        vector<double> p(n);
        for (auto &elem : p) cin >> elem;
        
        cout << "Case #" << t + 1 << ": " << fixed << stupid(n, k, p) << "\n";
    }
    
    return 0;
}
