#include<bits/stdc++.h>
using namespace std;
#define ll long long
ll t, i, n, p, mn, r, s, start, cnt, _t;
string st[5], str, c[5], ans;
string go(string str) {
    if(str.length() == 1) return str;
    ll l = str.length();
    string st1 = str.substr(0, l/2);
    string st2 = str.substr(l/2, l/2);
    string ans1 = go(st1);
    string ans2 = go(st2);
    string ans = "";
    if(ans1 > ans2) {
        ans = ans2+ans1;
    }
    else {
        ans = ans1+ans2;
    }

    return ans;
}
int main() {
    cin>>t;
    for(_t = 1; _t <= t; _t++) {
        cin>>n>>r>>p>>s;
        mn = 0;
        mn = min(min(p, r), s);
        str = "";
        printf("Case #%lld: ", _t);
        if(p-mn > 1|| r-mn>1 || s-mn>1) {
            cout<<"IMPOSSIBLE\n";
            continue;
        }
        st[0] = "PR";
        st[1] = "PS";
        st[2] = "RS";
        c[0] = "P";
        c[1] = "R";
        c[2] = "S";
        if(n%2 == 0) {
            if(p > mn) {
                start = 0;
            }
            else if(r > mn) {
                start = 1;
            }
            else if(s > mn) {
                start = 2;
            }
            cnt = 0;
            while(cnt < (1<<n)) {
                str += c[start];
                start++;
                start %= 3;
                cnt++;
            }
        }
        else {
            if(p > mn && r > mn) {
                start = 0;
            }
            else if(p > mn && s > mn) {
                start = 1;
            }
            else if(r > mn && s > mn) {
                start = 2;
            }
            cnt = 0;
            while(cnt < (1<<(n-1))) {
                str += st[start];
                start++;
                start %= 3;
                cnt++;
            }
        }
        ans = go(str);
        cout<<ans<<endl;
    }

    return 0;
}
