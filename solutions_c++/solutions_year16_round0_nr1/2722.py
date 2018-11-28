#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
const int N = 1e6 + 10;

ll calc(ll x){
    bool v[10];
    memset(v, 0, sizeof v);
    int cnt = 0;
    for(int i = 1; cnt < 10 && i <= 72; ++i){   // at most 72 steps with x <= N
        for(ll y = x * i; y; y /= 10){
            if(!v[y % 10]) ++cnt;
            v[y % 10] = true;
        }
        if(cnt == 10) return x * i;
    }
    return -1;
}

int main(){
    // int cnt = 0;
    // for(int i = 0; i < N; ++i){
    //     if(calc(i) == -1) ++cnt;
    // }
    // cout << cnt << endl;
    int T, n;
    cin >> T;
    for(int cas = 1; cas <= T; ++cas) {
        cin >> n;
        cout << "Case #" << cas << ": ";
        if(n) cout << calc(n) << endl;
        else cout << "INSOMNIA" << endl;
    }
    return 0;
}