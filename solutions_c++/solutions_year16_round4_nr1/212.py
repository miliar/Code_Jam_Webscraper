// * You barely lifted your hand and Lesser Dog got excited.
#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm>
#include <string>
#include <set>
#include <map>
#include <queue>
#include <stack>
#include <cstring>
#include <cassert>
using namespace std;
#define rep(i,a,n) for (int i=a;i<n;i++)
#define per(i,a,n) for (int i=n-1;i>=a;i--)
typedef long long ll;
const int N = 15;
const vector<string> RPS = {"R","P","S"};

bool has[3][N];
string dp[3][N];


string get(int type, int depth) {
    if(depth == 0) {
        return RPS[type];
    } else {
        if(has[type][depth]) return dp[type][depth];
        has[type][depth] = true;
        string s1 = get(type, depth-1);
        string s2 = get((type+2)%3, depth-1);
        return dp[type][depth] = min(s1+s2, s2+s1);
    }
}

void solve() {
    int n, r, p, s;
    cin >> n >> r >> p >> s;
    string x[3];
    string best = "Z";
    rep(i,0,3) {
        string cur = get(i, n);
        int rr=0,pp=0,ss=0;
        rep(j,0,cur.size()){
            if(cur[j]=='R')rr++;
            if(cur[j]=='P')pp++;
            if(cur[j]=='S')ss++;
        }
        if(rr==r&&pp==p&&ss==s){
            best = min(best, cur);
        }
    }

    if(best=="Z"){
        cout << "IMPOSSIBLE";
    } else cout << best;
}

int main() {
    freopen("large.in", "r", stdin);
    freopen("outl.txt", "w", stdout);
    ios_base::sync_with_stdio(false);
    int q;
    cin >> q;
    rep(i, 0, q) {
        cout << "Case #" << (i + 1) << ": ";
        solve();
        cout << endl;
    }
    return 0;
}
