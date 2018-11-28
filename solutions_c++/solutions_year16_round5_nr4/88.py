// you decide to dig into the virtual ground, but it's just old keyboards.  miles and miles of keyboards
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
    int n, l;
    cin >> n >> l;
    string _s;
    bool good = true;
    rep(i, 0, n) {
        cin >> _s;
        bool ok = false;
        rep(i, 0, _s.size()) if(_s[i] == '0') ok = true;

        if(!ok) {
            cout << "IMPOSSIBLE";
            good = false;
        }
    }
    cin >> _s;
    if(!good) return;
    if(l == 1){
        cout << "? 0";
        return;
    }
    string a = "", b = "";
    rep(i, 0, l - 1) a.push_back('?');
    rep(i, 0, l) b.push_back('1'), b.push_back('0');
    b += "?1";
    cout << a << " " << b;
}

int main() {
    if(0) freopen("in.txt", "r", stdin);
    else {
        freopen("/home/vaclav/Downloads/D-small-attempt1.in", "r", stdin);
        freopen("out.txt", "w", stdout);
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
