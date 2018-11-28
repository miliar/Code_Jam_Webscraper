// Author : Mahesh

/* 1. Did u interpret the qns correctly ?
 2. Is your i/o correct ?
 3. Int overflow, double precesion
 4. Array size correct ?
 5. Clearing/resetting vector, map etc.
 6. Stack ovrflow
 7. Global/local conflict
 8. Check for obvious typo(most imp)
 */

#include <vector>
#include <string>
#include <map>
#include <set>
#include <queue>
#include <algorithm>
#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cctype>
#include <cstring>
#include <memory.h>
#include <cassert>

using namespace std;

#define ford(i, a, b, c)        for(int i=(a); i<(b); i+=(c))
#define fori(i, a, b)           ford(i,a,b,1)
#define rep(i, n)               fori(i,0,n)
#define ifor(i, a, b)           for(int i=(a); i>=(b); i--)
#define iter(i, a)              for(typeof((a).begin()) i=(a).begin(); i!=(a).end(); i++)
#define si(x)                   ((int)x.size())
#define SS                      ({int x;scanf("%d",&x);x;})
#define pb                      push_back
#define mp                      make_pair
#define all(a)                  a.begin(),a.end()
#define fill(a, v)              memset(a, v, sizeof(a))
#define inf                     (int)1e9
#define linf                    (long long)1e18
#define V                       vector
#define S                       string
#define XX                      first
#define YY                      second
#define P(v)                    rep(i, si(v)) cout<<v[i]<<" "; puts("")

typedef V<int> vi;
typedef V<S> vs;
typedef long long ll;
typedef pair<int,int> pii;

/* Program Body starts here */

S res[] ={"", "X", "O"};
S s[4];
int checkRow(int i) {
    int co = (int)count(all(s[i]), 'O');
    int cx = (int)count(all(s[i]), 'X');
    int ct = (int)count(all(s[i]), 'T');

    if (cx == 4 || (cx == 3 && ct == 1)) return 1;
    if (co == 4 || (co == 3 && ct == 1)) return 2;
    return 0;
}

int checkCol(int c) {
    int co = 0, cx = 0, ct = 0;
    rep(i, 4) {
        co += s[i][c] == 'O';
        cx += s[i][c] == 'X';
        ct += s[i][c] == 'T';
    }
    
    if (cx == 4 || (cx == 3 && ct == 1)) return 1;
    if (co == 4 || (co == 3 && ct == 1)) return 2;
    return 0;
}
int checkDiag(int anti) {
    int co = 0, cx = 0, ct = 0;
    rep(i, 4) {
        int p;
        if (anti) {
            p = 3-i;
        } else {
            p = i;
        }
        co += s[i][p] == 'O';
        cx += s[i][p] == 'X';
        ct += s[i][p] == 'T';
    }
    if (cx == 4 || (cx == 3 && ct == 1)) return 1;
    if (co == 4 || (co == 3 && ct == 1)) return 2;
    return 0;
}
int countDot() {
    rep(i, 4) {
        rep(j, 4) {
            if (s[i][j] == '.') return 1;
        }
    }
    return 0;
}


int main() {
    int T = SS;
    fori(t, 1, T+1) {
        int ans = 0;
        rep(i, 4) {
            cin>>s[i];
        }
        rep(i, 4) {
            if (!ans) ans = checkRow(i);
            if (!ans) ans = checkCol(i);
        }
        if (!ans) ans = checkDiag(0);
        if (!ans) ans = checkDiag(1);
        
        cout<<"Case #"<<t<<": ";
        if (ans) {
            cout<<res[ans]<<" won\n";
        }
        else if (countDot()) {
            cout<<"Game has not completed\n";
        }
        else {
            cout<<"Draw\n";
        }        
    }

}






