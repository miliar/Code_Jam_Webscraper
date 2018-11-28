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
        int N; cin >> N;
        vector<int> A(N);
        for (int &a:A) cin >> a;
        int answer = 0;
        vector<int> B = A;
        sort( B.begin(), B.end() );
        reverse( B.begin(), B.end() );
        for (int b:B) {
            int i=0; 
            while (A[i] != b) ++i;
            int vlavo = 0;
            for (int j=0; j<i; ++j) if (A[j] > b) ++vlavo;
            int vpravo = 0;
            for (int j=i+1; j<N; ++j) if (A[j] > b) ++vpravo;
            answer += min( vlavo, vpravo );
        }
        cout << "Case #" << test << ": " << answer << endl;
    }
}
// vim: fdm=marker:commentstring=\ \"\ %s:nowrap:autoread
