#include<bits/stdc++.h>
#define mp(x,y) make_pair(x,y)
#define pii pair<int,ll>
#define pb push_back


using namespace std;

typedef long long ll;

ll toDec(ll val, ll base){
    ll ans = 0;
    ll cur = 1ll;

    for(int i = 0; i < 16; i ++){
        if(val & 1<<i){
            ans += cur;
        }
        cur *= base;
    }


    return ans;

}

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    freopen("coin.in", "r",stdin);
    freopen("coin.out", "w",stdout);
    int n, J, t;
    cin >> t;
    cin >> n >> J;

    cout << "Case #1:\n";

    ll ans = 0;
    for(ll i = 1; i < (1 << (n - 1)); i ++){
        ll cur = i * 2 + 1;
        if(!(cur & 1<<(n - 1)))
            continue;
        vector<ll> div;
        //cout << "probando " << cur << endl;
        for(ll j = 2; j <= 10; j ++){
            ll val = toDec(cur, j);
          //  cout << "cur en base " << j << " " << val << endl;
            for(ll k = 2; k * k <= val; k ++){
                if(val % k == 0){
                    div.pb(k);
                    break;
                }
            }
        }
        if(div.size() == 9){
            ans ++;
            for(int j = n - 1; j >= 0;j --)
                cout << (cur&(1<<j)?1:0);
            for(ll j = 0; j < div.size(); j ++)
                cout << " " << div[j];
            cout << '\n';
        }

        if(ans == J)
            break;
    }








    return 0;
}
