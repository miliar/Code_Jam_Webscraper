// Comics In Which T-Rex Gets A Ride Home By Me, Ryan
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


void solve() {
    string s;
    cin>>s;
    bool good = true;
    ll res = 0;
    while(good && s.size()){
        good = false;
        rep(i,0,s.size()-1){
            if(s[i]==s[i+1]){
                res += 10;
                good = true;
                if(s.size() == 2){
                    s = "";
                    break;
                }
                if(i == s.size() - 1){
                    s = s.substr(0, i);
                } else {
                    s = s.substr(0, i)+s.substr(i+2);
                }
            }
        }
    }
    res += (s.size() / 2) * 5;
    cout<<res;
}

int main() {
    if(0) !freopen("in.txt", "r", stdin);
    else {
        !freopen("/home/vaclav/Downloads/A-large.in", "r", stdin);
        !freopen("out.txt", "w", stdout);
    }
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
