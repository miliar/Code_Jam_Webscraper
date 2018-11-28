#include <bits/stdc++.h>

using namespace std;

const int N = 1e6;
string s;
char st[] = {'R','P','S'};
string pre[25][3];
string Do(int level,int winner) {
    if(pre[level][winner].length()) return pre[level][winner];
    if(level == 0) {
        string s;
        s+=st[winner];
        pre[level][winner] = s;
        return s;
    }
    else {
        if(winner == 0) {
            string a = Do(level - 1,0);
            string b = Do(level - 1,2);
            pre[level][winner] = min(a + b,b + a);
        }
        else if(winner == 1) {
            string a = Do(level - 1,1);
            string b = Do(level - 1,0);
            pre[level][winner] = min(a + b,b + a);
        }
        else {
            string a = Do(level - 1,1);
            string b = Do(level - 1,2);
            pre[level][winner] = min(a + b,b + a);
        }
        return pre[level][winner];
    }
}

void solve() {
    int n,r,p,s; cin>>n>>r>>p>>s;
    int cr = 0,cp = 0,cs = 0;
    string ans;
    ::s = Do(n,0);
    cr = cp = cs = 0;
    for(int i = 0;i < (1<<n);i++) {
        if(::s[i] == 'R') cr++;
        if(::s[i] == 'P') cp++;
        if(::s[i] == 'S') cs++;
    }
    if(cr == r && cp == p && cs == s) {
        if(ans == "")
            ans = ::s;
        else 
            ans = min(ans,::s);
    }

    ::s = Do(n,1);
   
    cr = cp = cs = 0;
    for(int i = 0;i < (1<<n);i++) {
        if(::s[i] == 'R') cr++;
        if(::s[i] == 'P') cp++;
        if(::s[i] == 'S') cs++;
    }
    if(cr == r && cp == p && cs == s) {
        if(ans == "")
            ans = ::s;
        else 
            ans = min(ans,::s);
    }

    ::s = Do(n,2);
    cr = cp = cs = 0;
    for(int i = 0;i < (1<<n);i++) {
        if(::s[i] == 'R') cr++;
        if(::s[i] == 'P') cp++;
        if(::s[i] == 'S') cs++;
    }
    if(cr == r && cp == p && cs == s) {
        if(ans == "")
            ans = ::s;
        else 
            ans = min(ans,::s);
    }
    if(ans == "") 
        cout<<"IMPOSSIBLE"<<endl;
    else
        cout<<ans<<endl;

}

int main() {
    assert(freopen("input.txt","r",stdin));
    assert(freopen("output.txt","w",stdout));
    int t; cin>>t;
    for(int i = 1;i <= t;i++) {
        cerr<<"Executing Case #"<<i<<endl;
        cout<<"Case #"<<i<<": ";
        solve();
    }

}
