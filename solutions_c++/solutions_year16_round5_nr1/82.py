// another fine solution by misof
// #includes {{{
#include <algorithm>
#include <iostream>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <tuple>
#include <unordered_map>
#include <unordered_set>
#include <utility>
#include <vector>

#include <cassert>
#include <cctype>
#include <cstdio>
#include <cstdlib>
#include <cstring>

#include <cmath>
#include <complex>
using namespace std;
// }}}

/////////////////// PRE-WRITTEN CODE FOLLOWS, LOOK DOWN FOR THE SOLUTION ////////////////////////////////

// pre-written code {{{
#define FOR(i,a,b) for(int i=(int)(a);i<=(int)(b);++i)
// }}}

/////////////////// CODE WRITTEN DURING THE COMPETITION FOLLOWS ////////////////////////////////

int solve(const string &S) {
    int answer = 0;
    vector<char> stack;
    for (char c : S) {
        stack.push_back(c);
        if (stack.size() < 2u) continue;
        if (stack[ stack.size()-1 ] == stack[ stack.size()-2 ]) {
            answer += 2;
            stack.pop_back();
            stack.pop_back();
        }
    }
    answer += stack.size()/2;
    return answer;
}

int main() {
    int T; cin >> T;
    FOR(test,1,T) {
        //string TC; cin >> TC; cout << "Case #" << test << ": " << TC << " " << (5*solve(TC)) << endl;
        string TC; cin >> TC; cout << "Case #" << test << ": " << (5*solve(TC)) << endl;
    }
}
// vim: fdm=marker:commentstring=\ \"\ %s:nowrap:autoread
