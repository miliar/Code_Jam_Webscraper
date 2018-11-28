#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstring>
#include <algorithm>
#include <vector>
#include <queue>

#define FOR(i,a,b) for(int i = (a); i <= (b);i++)
#define FR(i,a) for(int i = 0; i < (a); i++)
#define DOWN(i,a,b) for(int i = (a); i >= (b); i--)

using namespace std;

int m,n;
string s[10];
int worst_node = 0, res = 0;
int a[10];
int compute(vector<string> ls) {
    sort(ls.begin(),ls.end());
    int total = ls[0].size();
    int k = ls.size();
    
    FOR(i,1,k-1) {//compare i and i-1
        int j = 0, matched = 0;
        while (j < ls[i].size() && j < ls[i-1].size() && ls[i][j] == ls[i-1][j]) matched++, j++;
        total += ls[i].size() - matched;
    }
    return total + 1;
}
void attempt(int cur) {
    if (cur > m) {
        int total = 0;
        bool ok = true;
        FOR(i,1,n) {
            vector<string> ls(0);
            FOR(j,1,m) if (a[j] == i) ls.push_back(s[j]);
            if (ls.size()) total += compute(ls);
            else {
                ok = false;
                break;
            }
        }
        if (ok) {
            if (total > worst_node) {
                worst_node = total;
                res = 1;
            } else if (total == worst_node) res = (res +1 ) % 1000000007;
        }
        return;
    }
    FOR(i,1,n) {
        a[cur] = i;
        attempt(cur+1);
    }
}
void solve() {
    worst_node = 0, res = 0;
    attempt(1);
    cout << worst_node << " " << res << endl;
}

int main() 
{
    freopen("DD.in","r",stdin);
    freopen("test.out","w",stdout);
    int ntest;
    cin >> ntest;
    FOR(test,1,ntest) {
        cout << "Case #" << test << ": ";
        cin >> m >> n;
        FOR(i,1,m) cin >> s[i];
        solve();
    }        
    return 0;
}

