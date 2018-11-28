// (whispering) i like to look at their bodies
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
#include <iomanip>
using namespace std;
#define rep(i,a,n) for (int i=a;i<n;i++)
#define per(i,a,n) for (int i=n-1;i>=a;i--)
typedef long long ll;


void solve() {
    int n;
    cin >> n;
    vector<int> g(n);
    vector<int> sons[111];
    rep(i, 0, n) {
        cin >> g[i];
        g[i]--;
        if(g[i]>=0) sons[g[i]].push_back(i);
    }

    string s;
    cin >> s;
    int m;
    cin >> m;
    vector<string> c(m);
    vector<int> res(m);
    rep(i, 0, m)cin >> c[i];
    const int IT = 10000;
    rep(it, 0, IT) {


        string cur = "";
        vector<bool> done(n, false);
        rep(i,0,n){
            bool good = false;
            int ci;
            do{
                ci = rand() % n;
                while(g[ci]!=-1 && !done[g[ci]]) ci = g[ci];
                good = !done[ci];
            } while(!good);
            done[ci] = true;
            cur += s[ci];
        }


        rep(i,0,m){
            bool has = false;
            rep(j,0,cur.size()){
                if(cur.substr(j,c[i].size()) == c[i]){
                    has = true;
                    break;
                }
            }
            if(has) res[i]++;
        }
    }
    rep(i,0,m){
        cout<<((double)res[i])/IT<<" ";
    }
}

int main() {
    if(0) freopen("in.txt", "r", stdin);
    else {
        freopen("/home/vaclav/Downloads/B-small-attempt0.in", "r", stdin);
        freopen("out.txt", "w", stdout);
    }
    ios_base::sync_with_stdio(false);
    cout<<fixed<<setprecision(10);
    int q;
    cin >> q;
    rep(i, 0, q) {
        cout << "Case #" << (i + 1) << ": ";
        solve();
        cout << endl;
    }
    return 0;
}
