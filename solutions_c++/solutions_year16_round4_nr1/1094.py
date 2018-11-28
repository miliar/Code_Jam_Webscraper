#include <string>
#include <vector>
#include <algorithm>
#include <map>
#include <set>
#include <stack>
#include <queue>
#include <math.h>
#include <iostream>
#include <fstream>
#include <stdio.h>
#include <stdlib.h>
#include <cassert>
#include <string.h>
using namespace std;
#define ll long long

string solve(ll N, ll R, ll P, ll S) {
    
    if (N == 1) {
        if (R && P)
            return "PR";
        if (R && S)
            return "RS";
        return "PS";
    }
    
    
    if (R == P) {
        if (S > R) {
            return solve(N-1, R/2, P/2+1, S/2) + solve(N-1, R/2+1, P/2, S/2);
        }
        else {
            return solve(N-1, R/2, P/2+1, S/2) + solve(N-1, R/2+1, P/2, S/2);
        }

    }
    else if (R == S) {
        if (P > R) {
            return solve(N-1, R/2+1, P/2, S/2) + solve(N-1, R/2, P/2, S/2+1);
        }
        else {
            return solve(N-1, R/2+1, P/2, S/2) + solve(N-1, R/2, P/2, S/2+1);
        }
    }
    else {
        if (R > S) {
            return solve(N-1, R/2, P/2+1, S/2) + solve(N-1, R/2, P/2, S/2+1);
        }
        else {
            return solve(N-1, R/2, P/2+1, S/2) + solve(N-1, R/2, P/2, S/2+1);
        }
    }
}


int main() {
    std::ios::sync_with_stdio(false);
    cin.tie(0);

    ll t;
    cin >> t;
    
    for (ll z = 0; z < t; z++) {
     
        ll N, R, P, S;
        cin >> N >> R >> P >> S;
        
        ll maxi = max(max(R, P), S);
        ll mini = min(min(R, P), S);
        
        string res;
        if (maxi - mini > 1) {
            res = "IMPOSSIBLE";
        }
        else
            res = solve(N, R, P, S);
        
        cout << "Case #" << z+1 << ": " << res << endl;
    }
}