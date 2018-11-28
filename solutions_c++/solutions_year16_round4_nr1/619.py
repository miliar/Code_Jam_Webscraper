#include<bits/stdc++.h>
using namespace std;

int pows[30];
int n, p, r, s;
int myp, myr, mys;

string solve(int l, int r, char win) {

    if (l==r) {
        string ret;
        if (win=='P') {
            ret.push_back('P');
            myp++;
        }
        if (win=='R') {
            ret.push_back('R');
            myr++;
        }
        if (win=='S') {
            ret.push_back('S');
            mys++;
        }
        return ret;
    }

    int mid = (l+r)/2;
    if (win == 'P') {
        string a = solve(l, mid, 'P');
        string b = solve(mid+1, r, 'R');
        if (a>b) return b+a;
        else return a+b;
    }
    else if (win == 'R') {
        string a = solve(l, mid, 'R');
        string b = solve(mid+1, r, 'S');
        if (a>b) return b+a;
        else return a+b;
    }
    else if (win == 'S') {
        string a = solve(l, mid, 'P');
        string b = solve(mid+1, r, 'S');
        if (a>b) return b+a;
        else return a+b;
    }
}

main() {

    pows[0] = 1;
    for (int i=1; i<30; i++) pows[i] = pows[i-1] * 2;

    int t;
    cin>>t;
    for (int te=1; te<=t; te++) {

        cin>>n>>r>>p>>s;
        string cur;

        bool found = 0;

        myp = myr = mys = 0;
        string print = solve(1, pows[n], 'P');
        if (myp == p && myr == r && mys == s) {
            found = 1;
            cur = print;
        }

        myp = myr = mys = 0;
        print = solve(1, pows[n], 'R');
        if (myp == p && myr == r && mys == s) {
            if (found) cur = min(cur, print);
            else {
                found = 1;
                cur = print;
            }
        }

        myp = myr = mys = 0;
        print = solve(1, pows[n], 'S');
        if (myp == p && myr == r && mys == s) {
            if (found) cur = min(cur, print);
            else {
                found = 1;
                cur = print;
            }
        }

        cout<<"Case #"<<te<<": ";

        if (found) cout<<cur<<"\n";
        else cout<<"IMPOSSIBLE\n";
    }
}
