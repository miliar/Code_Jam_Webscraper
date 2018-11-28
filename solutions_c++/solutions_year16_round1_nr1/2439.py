#include <cstdio>
#include <cstring>
#include <iostream>

using namespace std;

const int MAXN = 1000+1;

string s;
string f[MAXN];
bool u[MAXN];
int n;

void solve(int n) {
    if (u[n]) return;
    f[n] = "";
    string suffix = "";
    for (int i = n; i>=1; --i) {
        solve(i-1);
        string tmp = s[i-1]+f[i-1]+suffix;
        if (tmp>f[n]) f[n] = tmp;
        suffix = s[i-1]+suffix;
    }
    u[n] = 1;
}

int main() {
    int T;
    cin>>T;
    for (int loop = 1; loop<=T; ++loop) {
        printf("Case #%d: ",loop);
        cin>>s;
        n = s.length();
        f[0] = "";
        f[1] = s[0];
        memset(u,0,sizeof(u));
        u[0] = u[1] = 1;
        solve(n);
        cout<<f[n]<<endl;
    }
    return 0;
}