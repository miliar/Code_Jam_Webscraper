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
#define REP(i,n) for(int i=0;i<(int)(n);++i)
// }}}

/////////////////// CODE WRITTEN DURING THE COMPETITION FOLLOWS ////////////////////////////////

struct key {
    int lo, lives_left, saved_shots, may_use_saved;
    key(int lo, int lives_left, int saved_shots, int may_use_saved) : lo(lo), lives_left(lives_left), saved_shots(saved_shots), may_use_saved(may_use_saved) {};
};

bool operator< (const key &A, const key &B) {
    if (A.lo != B.lo) return A.lo < B.lo;
    if (A.lives_left != B.lives_left) return A.lives_left < B.lives_left;
    if (A.saved_shots != B.saved_shots) return A.saved_shots < B.saved_shots;
    if (A.may_use_saved != B.may_use_saved) return A.may_use_saved < B.may_use_saved;
    return false;
}

int N, P, Q;
vector<int> H, G;
map<key,long long> memo, memo2;

long long solve(int lo, int lives_left, int saved_shots, int may_use_saved);

long long solve2(int lo, int lives_left, int saved_shots, int may_use_saved) {
    // tower goes first
    key K(lo,lives_left,saved_shots,may_use_saved);
    if (memo2.count(K)) return memo2[K];
    long long &res = memo2[K];
    res = 0;
    
    // if there are no more monsters, we are done
    if (lo==N) return res=0;

    // if she has saved shots and may use them, she may use one on the current monster
    if (saved_shots > 0 && may_use_saved) {
        if (lives_left <= P) res = max( res, G[lo] + solve2(lo+1, H[lo+1], saved_shots-1, 1) );
        else res = max( res, solve2(lo, lives_left-P, saved_shots-1, 1) );
    }
    //cout << "solve2 " << lo << " " << lives_left << " " << saved_shots << " " << may_use_saved << " after saved return " << res << endl;

    // she may let the tower shoot
    {
        if (lives_left <= Q) res = max( res, solve(lo+1, H[lo+1], saved_shots, 1) );
        else res = max( res, solve(lo, lives_left-Q, saved_shots, 0) );
    }
    //cout << "solve2 " << lo << " " << lives_left << " " << saved_shots << " " << may_use_saved << " return " << res << endl;
    return res;
}

long long solve(int lo, int lives_left, int saved_shots, int may_use_saved) {
    key K(lo,lives_left,saved_shots,may_use_saved);
    if (memo.count(K)) return memo[K];
    long long &res = memo[K];
    res = 0;

    // if there are no more monsters, we are done
    if (lo==N) return res=0;

    // if she has saved shots and may use them, she may use one on the current monster
    if (saved_shots > 0 && may_use_saved) {
        if (lives_left <= P) res = max( res, G[lo] + solve(lo+1, H[lo+1], saved_shots-1, 1) );
        else res = max( res, solve(lo, lives_left-P, saved_shots-1, 1) );
    }
    //cout << "solve " << lo << " " << lives_left << " " << saved_shots << " " << may_use_saved << " after saved return " << res << endl;

    // she may pause and let the tower shoot, saving a shot for later
    {
        if (lives_left <= Q) res = max( res, solve(lo+1, H[lo+1], saved_shots+1, 1) );
        else res = max( res, solve(lo, lives_left-Q, saved_shots+1, 0) );
    }
    //cout << "solve " << lo << " " << lives_left << " " << saved_shots << " " << may_use_saved << " after pause return " << res << endl;

    // she may shoot the current monster
    {
        if (lives_left <= P) {
            long long curr = G[lo];
            if (lo+1 == N) {
                res = max( res, curr );
            } else {
                /*
                if (H[lo+1] <= Q) {
                    res = max( res, curr + solve(lo+2, H[lo+2], saved_shots, 1) );
                } else {
                    res = max( res, curr + solve(lo+1, H[lo+1]-Q, saved_shots, 1) );
                }
                */
                //cout << "solve " << lo << " " << lives_left << " " << saved_shots << " " << may_use_saved << " call solve2 " << lo+1 << " " << H[lo+1] << " " << saved_shots << " " << 1 << endl;
                res = max( res, curr + solve2(lo+1, H[lo+1], saved_shots, 1) );
            }
        }
        if (lives_left > P && lives_left <= P+Q) {
            res = max( res, solve(lo+1, H[lo+1], saved_shots, 1) );
        }
        if (lives_left > P+Q) {
            res = max( res, solve(lo, lives_left-P-Q, saved_shots, may_use_saved) );
        }
    }
    //cout << "solve " << lo << " " << lives_left << " " << saved_shots << " " << may_use_saved << " return " << res << endl;
    return res;
}

int main() {
    int T; cin >> T;
    FOR(test,1,T) {
        cin >> P >> Q >> N;
        H.clear(); H.resize(N+1,0);
        G.clear(); G.resize(N+1,0);
        REP(n,N) cin >> H[n] >> G[n];
        memo.clear();
        memo2.clear();
        cout << "Case #" << test << ": " << solve(0, H[0], 0, 1) << endl;
    }
}
// vim: fdm=marker:commentstring=\ \"\ %s:nowrap:autoread
