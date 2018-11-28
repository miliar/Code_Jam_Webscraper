#include <bits/stdc++.h>
using namespace std;

typedef long long ll;

ll a[11][17];

ll f(ll n){
    for(int i = 2; i <= sqrt(n); i++){
        if(n%i == 0){
            return i;
        }
    }
    return -1;
}

ll create(ll base, string s){
    ll x = 0;
    for(int i = s.size() - 1; i >= 0; i--){
        if(s[i] == '1'){
            x += a[base][s.size() - i - 1];
        }
    }
    return x;
}


int main(){
    srand(13);
//    freopen("inp.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
    for(int i = 1; i <= 10; i++){
        ll x = 1;
        for(int j = 0; j <= 16; j++){
            a[i][j] = x;
            x *= i;
        }
    }
    string s = "1000000000000001";
    set<string> used;
    pair<string,vector<ll>> ans[50];
    int cnt = 0;
    while(cnt < 50){
        for(int i = 1; i < s.size()-1; i++){
            s[i] = rand()%2 + '0';
        }
        if(used.find(s) != used.end()){
            continue;
        }
        used.insert(s);
        vector<ll> cur;
        for(int v = 2; v <= 10; v++){
            cur.push_back(create(v, s));
        }
        vector<ll> anscur;
        for(int i = 0; i < cur.size(); i++){
            anscur.push_back(f(cur[i]));
        }
        if(all_of(anscur.begin(), anscur.end(), [](ll x){return x != -1;})){
            ans[cnt] = {s, anscur};
            cnt++;
        }
    }
    cout << "Case #1:\n";
    for(int i = 0; i < 50; i++){
        cout << ans[i].first << ' ';
        for(auto j : ans[i].second){
            cout << j << ' ';
        }
        cout << endl;
    }
    return 0;
}
