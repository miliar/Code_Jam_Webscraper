#include<bits/stdc++.h>
using namespace std;
#define ll long long
ll n, t, _t, i, l, cnt, tot;
string s;
int main() {
    cin>>t;
    for(_t = 1; _t <= t; _t++) {
        cin>>s;
        l = s.length();
        cnt = 0;
        if(s[0] == '-') cnt = 1;
        tot = 0;
        for(i = 0; i < l-1; i++) {
            if(s[i] == '+' && s[i+1] == '-') {
                tot++;
            }
        }
        tot*=2;
        printf("Case #%lld: %lld\n", _t, tot+cnt);
    }


    return 0;
}
