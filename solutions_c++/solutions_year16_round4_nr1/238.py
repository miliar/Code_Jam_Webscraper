#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
string f(int x, int n) {
    if(n == 1) {
        if(x == 0) return "P";
        if(x == 1) return "R";
        if(x == 2) return "S";
    }
    string a,b;
    if(x == 0) {
        a = f(1, n/2);
        b = f(0, n/2);
    }
    if(x == 1) {
        a = f(2, n/2);
        b = f(1, n/2);
    }
    if(x == 2) {
        a = f(0, n/2);
        b = f(2, n/2);
    }
    if(a < b) {
        a.insert(a.end(), b.begin(), b.end());
        return a;
    }
    else {
        b.insert(b.end(), a.begin(), a.end());
        return b;
    }

}
int f2(string s, int r, int p, int ss) {
    for(int i = 0; i < s.size(); ++i) {
        if(s[i] == 'R') --r;
        if(s[i] == 'P') --p;
        if(s[i] == 'S') --ss;
    }
    if(ss == 0 && p == 0 && r == 0) return 1;
    return 0;
}
int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    int tt;
    cin>>tt;
    for(int xx = 0; xx < tt; ++xx) {
        cout<<"Case #"<<xx+1<<':'<<' ';
        int n,rr,pp,ss;
        cin>>n>>rr>>pp>>ss;
        n = 1<<n;
        string s;
        for(int i = 0; i < n; ++i) {
            s.push_back('Z');
        }
        string a = f(0, n);
        if(f2(a, rr, pp, ss)) {
            s = min(s, a);
        }
        a = f(1, n);
        if(f2(a, rr, pp, ss)) {
            s = min(s, a);
        }
        a = f(2, n);
        if(f2(a, rr, pp, ss)) {
            s = min(s, a);
        }
        if(s[0] == 'Z') {
            cout<<"IMPOSSIBLE\n";
        }
        else {
            cout<<s<<'\n';
        }
    }
}
