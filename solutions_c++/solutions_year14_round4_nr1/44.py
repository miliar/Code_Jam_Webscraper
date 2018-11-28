// another fine solution by misof
// #includes {{{
#include <algorithm>
#include <numeric>

#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <stack>

#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cctype>
#include <cassert>

#include <cmath>
#include <complex>
using namespace std;
// }}}

/////////////////// PRE-WRITTEN CODE FOLLOWS, LOOK DOWN FOR THE SOLUTION ////////////////////////////////

// pre-written code {{{
#define FOR(i,a,b) for(int i=(int)(a);i<=(int)(b);++i)
// }}}

/////////////////// CODE WRITTEN DURING THE COMPETITION FOLLOWS ////////////////////////////////

int main() {
    int T; cin >> T;
    FOR(test,1,T) {
        int N, X;
        cin >> N >> X;
        multiset<int> MS;
        for (int n=0; n<N; ++n) { int x; cin >> x; MS.insert(x); }
        int answer = 0;
        while (!MS.empty()) {
            multiset<int>::iterator it;
            it = MS.end();
            --it;
            int largest = *it;
            MS.erase(it);
            int remains = X - largest;
            it = MS.upper_bound(remains);
            if (it != MS.begin()) {
                --it;
                MS.erase(it);
            }
            ++answer;
        }
        cout << "Case #" << test << ": " << answer << endl;
    }
}
// vim: fdm=marker:commentstring=\ \"\ %s:nowrap:autoread
