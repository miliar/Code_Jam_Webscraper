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
// BEGIN CUT HERE
#define DEBUG(var) { cout << #var << ": " << (var) << endl; }
template <class T> ostream& operator << (ostream &os, const vector<T> &temp) { os << "[ "; for (unsigned int i=0; i<temp.size(); ++i) os << (i?", ":"") << temp[i]; os << " ]"; return os; } // DEBUG
template <class T> ostream& operator << (ostream &os, const set<T> &temp) { os << "{ "; for(__typeof((temp).begin()) it=(temp).begin();it!=(temp).end();++it) os << ((it==(temp).begin())?"":", ") << (*it); os << " }"; return os; } // DEBUG
template <class T> ostream& operator << (ostream &os, const multiset<T> &temp) { os << "{ "; for(__typeof((temp).begin()) it=(temp).begin();it!=(temp).end();++it) os << ((it==(temp).begin())?"":", ") << (*it); os << " }"; return os; } // DEBUG
template <class S, class T> ostream& operator << (ostream &os, const pair<S,T> &a) { os << "(" << a.first << "," << a.second << ")"; return os; } // DEBUG
template <class S, class T> ostream& operator << (ostream &os, const map<S,T> &temp) { os << "{ "; for(__typeof((temp).begin()) it=(temp).begin();it!=(temp).end();++it) os << ((it==(temp).begin())?"":", ") << (it->first) << "->" << it->second; os << " }"; return os; } // DEBUG
// END CUT HERE
#define FOR(i,a,b) for(int i=(int)(a);i<=(int)(b);++i)
// }}}

/////////////////// CODE WRITTEN DURING THE COMPETITION FOLLOWS ////////////////////////////////

long long N, p, q, r, s;
vector<long long> A, P;

inline long long segsum(int l, int r) { 
    if (r<l) return 0;
    return P[r]-P[l]; 
}

inline void improve(long long &least_solveig, int l, int r) {
    //cout << "improve " << l << " " << r << endl;
    if (l<0) return;
    if (r<l) return;
    if (N<r) return;
    long long cur = segsum(l,r);
    if (l>0) cur = max( cur, segsum(0,l) );
    if (r<N) cur = max( cur, segsum(r,N) );
    least_solveig = min( least_solveig, cur );
    // cout << "improve " << l << " " << r << " cur= " << cur << " least_solveig=" << least_solveig << endl;
}

int main() {
    int T; cin >> T;
    FOR(test,1,T) {
        cin >> N >> p >> q >> r >> s;
        A.clear(); A.resize(N);
        for (long long n=0; n<N; ++n) A[n] = ( (n*p+q) % r + s );
        P.clear(); P.resize(N+1);
        for (long long n=0; n<N; ++n) P[n+1] = P[n] + A[n];
        //DEBUG(A);
        //DEBUG(P);
        long long least_solveig = P[N];
        int r=0;
        for (int l=0; l<=N; ++l) {
            if (r<l) r=l;
            while (r<N && segsum(l,r) < segsum(r,N)) ++r;
            improve(least_solveig,l,r-2);
            improve(least_solveig,l,r-1);
            improve(least_solveig,l,r);
            improve(least_solveig,l,r+1);
            improve(least_solveig,l,r+2);
        }
        printf("Case #%d: %.10f\n",test,1.*(P[N]-least_solveig)/P[N]);
    }
}
// vim: fdm=marker:commentstring=\ \"\ %s:nowrap:autoread
