#include <stdio.h>
#include <iostream>
#include <sstream>
#include <iomanip>
#include <cstring>
#include <cmath>
#include <algorithm>
#include <climits>
#include <vector>
#include <stack>
#include <queue>
#include <set>
#include <unordered_set>
#include <map>
#include <unordered_map>
#include <cassert>

#define SHOW(...) {;}
#define REACH_HERE {;}

#ifdef JUDGE
#include "judge.h"
#endif

using namespace std;

double solve(vector<double> d) {
    int n = d.size();
    SHOW(n)
    if (n == 0) return 0;
    int half = d.size() / 2;
    int choices[n];
    for (int i = 0; i < n; i++) choices[i] = 0;
    for (int i = n - half; i < n; i++) choices[i] = 1;
    double ans = 0;
    // SHOW(ans)
    do {
        double cur = 1.0;
        vector<double> points;
        for (int i = 0; i < n; i++) {
            if (choices[i]) {
                cur *= d[i];
            } else {
                cur *= 1 - d[i];
            }
        }
        ans += cur;
    } while ( next_permutation(choices,choices+n) );
    return ans;
}


int main() {
    ios::sync_with_stdio(false);

    int t;
    cin >> t;
    SHOW(t);

    for (int tt = 1; tt <= t; tt++) {
        SHOW(tt)
        int n, k;
        cin >> n >> k;
        double department[n];
        for (int i = 0; i < n; i++) {
            cin >> department[i];
        }
        int choices[n];
        for (int i = 0; i < n; i++) choices[i] = 0;
        for (int i = n - k; i < n; i++) choices[i] = 1;
        double ans = 0;
        do {
            SHOW(choices[0])
            vector<double> points;
            for (int i = 0; i < n; i++) {
                if (choices[i]) {
                    SHOW(i, department[i])
                    points.push_back(department[i]);
                }
            }
            ans = max(ans, solve(points));
        } while ( next_permutation(choices,choices+n) );
        cout << "Case #" << tt << ": " << ans << endl;
    }
}


