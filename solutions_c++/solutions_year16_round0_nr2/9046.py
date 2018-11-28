#include <iostream>
#include <string>
#include <stdio.h>
#include <fstream>
#include <algorithm>
#include <vector>
#include <map>
#include <set>
#include <queue>
#include <cmath>
#include <cassert>

using namespace std;
typedef long long ll;
typedef long double ld;
#define MOD (ld)1e9 + 7
#define PI (ld)3.14159265358979324
#define mp make_pair 
#define pb push_back
#define ft first
#define sd second
#define sz(a) (ll)a.size()
#define pii pair<int,int>
#define pll pair<ll,ll>
#define loop(i, n) for(int (i) = 0; (i) < (n) ; ++ (i))
#define forn(i, l, r) for(int (i) = (l); (i) < (r) ; ++ (i))
#define vec vector 
#define str string
#define vii vector<int> 

string update(const str & s) {
    string ns;
    ns.reserve(s.size());
    char last = '=';
    loop(i , s.size()) {
        if(last != s[i]) {
            ns.pb(s[i]);
            last = s[i];
        }
    }
    return ns;
}
int lastm(const str & s) {
    int ans = -1;
    loop(i,s.size()) {
        if(s[i] == '-') ans = i;
    }
    return ans;
}

void solve() {
    string s;
    cin >> s;
    int ans = 0;
    while(true) {
        s = update(s);
        int lm = lastm(s);
        if(lm == -1) break;
        if(s[0] == '+') {
            s[0] = '-';
            ++ans;
        }

        loop(j , lm + 1) {
            s[j] =  (s[j] == '-' ? '+' : '-');
        }
        ++ans;
        
    }

    cout << ans << endl;
}   

int main()
{
    freopen("in.txt","r", stdin);
    freopen("bout.txt","w", stdout);
    // cout << fixed;
    // cout.precision(3);
    ios_base::sync_with_stdio(false);   
    int t;
    cin >> t;
    loop(i,t) {
        cout << "Case #" << i + 1 << ": ";
        solve();
    }
    return 0;
}