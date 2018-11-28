#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef unsigned long long ull;
typedef pair<int, int> ii;

void preprocess() {

}

bool valid(const string s) {
    if (s.size() == 1)
        return true;
    const int n = s.size();
    string s2;
    for (int i = 0; i < n; i += 2) {
        char a = s[i];
        char b = s[i+1];
        char c = 0;
        if (a == 'R') {
            if (b == 'P')
                c = 'P';
            else if (b == 'S')
                c = 'R';
        } else if (a == 'P') {
            if (b == 'S')
                c = 'S';
            else if (b == 'R')
                c = 'P';
        } else if (a == 'S') {
            if (b == 'R')
                c = 'R';
            else if (b == 'P')
                c = 'S';
        }
        if (c == 0)
            return false;
        s2.push_back(c);
    }
    return valid(s2);
}

string ans;
string str;
void solve(int nn, int r, int p, int s) {
    if (!ans.empty()) return;
    if (nn == 0) {
        if (valid(str))
            ans = str;
        return;
    }
    if (r == 0 && p == 0 && s == 0) {
        return;
    }
    if (p) {
        str.push_back('P');
        solve(nn-1, r, p-1, s);
        str.pop_back();
    }
    if (r) {
        str.push_back('R');
        solve(nn-1, r-1, p, s);
        str.pop_back();
    }
    if (s) {
        str.push_back('S');
        solve(nn-1, r, p, s-1);
        str.pop_back();
    }
}

void process_testcase(const int testcase, const int should_run){
    int n, r, p, s;
    cin>>n>>r>>p>>s;
    const int nn = 1<<n;
    if (should_run) {
        ans="";
        str="";
        solve(nn, r, p, s);
        cout<<"Case #"<<testcase<<": ";
        if (ans.empty())
            cout<<"IMPOSSIBLE\n";
        else
            cout<<ans<<'\n';
    }
}
