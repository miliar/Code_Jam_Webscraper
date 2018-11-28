#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;

int solve_p(const vector<int>& p, int d) {
    int res = 0;
    for (int i = 0 ;i < p.size(); ++i) {
        if (p[i] > d) {
            if (p[i] % d == 0) {
                res += p[i]/d - 1;
            } else {
                res += p[i]/d;
            }
        }
    }
    return res;
}

int solve() {
    int D;
    vector<int> p;
    
    cin >> D;
    
    for (int i = 0; i < D; ++i) {
        int tt;
        cin >> tt;
        p.push_back(tt);
    }
    
    int res = 1000000;
    for (int d = 1; d <= 2000; ++d) {
        res = min(res, solve_p(p, d) + d);
    }
    return res;
}


int main() {
    
    int t;
    cin >> t;
    
    for (int i = 1; i <= t; ++i) {
        cout << "Case #" << i << ": " << solve() << endl;
    }
    
    return 0;
}
