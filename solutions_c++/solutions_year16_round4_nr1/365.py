#include <iostream>
#include <vector>
#include <set>
#include <map>
#include <algorithm>

#define For(i,a,b) for(int i = a; i < b; i++)
#define rep(i,x) For(i,0,x)
#define foreach(i,c) for(typeof((c).begin()) i = (c).begin(); i != (c).end(); ++i)
#define sz(x) ((int)(x).size())
#define F first
#define S second
#define pb push_back
#define mp make_pair
#define TWO(x) (1LL<<(x))

using namespace std;

string solve(char top, int depth) {
    if(depth == 0) {
        return string(1, top);
    }
    map<char, char> bla = {{'P','R'},{'R','S'},{'S','P'}};
    string left = solve(top, depth-1);
    string right = solve(bla[top], depth-1);
    if(left < right) {
        return left + right;
    } else {
        return right + left;
    }
}


int main() {
    int np; cin>>np;
    rep(i, np){
        cout << "Case #"<<(i+1)<<": ";

        int n, r, p, s; cin>>n>>r>>p>>s;
        
        vector<char> bla = {'R','P','S'};
        map<char, int> inv = {{'R', 0},{'P',1},{'S',2}};
        vector<int> blabla = {r, p, s};
        string ans = "";
        for(char x : bla) {
            string res = solve(x, n);
            bool ok = true;
            rep(i, 3) {
                int cnt = 0;
                rep(k, int(res.size())) {
                    if(inv[res[k]] == i) {
                        cnt++;
                    }
                }
                ok &= (cnt == blabla[i]);
            }
            if(ok) {
                if(ans == "" || res < ans) {
                    ans = res;
                }
            }
        }
        if(ans == "") {
            cout << "IMPOSSIBLE" << endl;
        } else {
            cout << ans <<endl;
        }
                
    }
}
