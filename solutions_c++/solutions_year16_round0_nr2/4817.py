#include <bits/stdc++.h>
using namespace std;

typedef long long ll;

ll solve(string s){
    ll cnt = 0;
    for(int i = 1; i < s.size(); i++){
        if(s[i] != s[i-1]){
            cnt++;
        }
    }
    if(s.back() == '-'){cnt++;}
    return cnt;
}

int main(){
    freopen("inp.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
    ll T;
    cin >> T;
    for(ll i = 1; i <= T; i++){
        string s;
        cin >> s;
        printf("Case #%lld: %lld\n", i, solve(s));
    }
    return 0;
}
