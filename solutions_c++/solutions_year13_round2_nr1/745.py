
#include <algorithm>
#include <cassert>
#include <climits>
#include <cmath>
#include <deque>
#include <iostream>
#include <limits>
#include <list>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <utility>
#include <vector>
#include <stack>
#include <cln/cln.h>

typedef int builtin_int;
#define int long long

using namespace std;
using namespace cln;

typedef cl_I Int;
typedef cl_RA Frac;

Int operator/(Int x, Int y) {
    return floor1(x, y);
}

void solve_test() {
    int s, n;
    cin >> s >> n;
    
    vector<int> v(n);
    for (int& x : v)
        cin >> x;
    
    sort(v.begin(), v.end());
    
    int best_sol = n;
    for (int n_deletions = 0; n_deletions < best_sol; n_deletions++) {
        
        int n_additions = 0;
        int current_size = s;
        for (int i = 0; i < (n - n_deletions); i++) {
            while (current_size <= v[i]) {
                if (current_size == 1)
                    goto try_another;
                current_size += (current_size - 1);
                ++n_additions;
            }
            current_size += v[i];
        }
        
        best_sol = min(best_sol, n_additions + n_deletions);
        
    try_another:
        ;
    }
    
    cout << best_sol << endl;
}

builtin_int main() {
    
    int n;
    cin >> n;
    for (int i = 0; i < n; i++) {
        cout << "Case #" << (i+1) << ": ";
        solve_test();
    }
    
    return 0;
}
