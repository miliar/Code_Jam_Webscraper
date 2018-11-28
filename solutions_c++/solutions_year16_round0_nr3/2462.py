#include <bits/stdc++.h>
#define ll long long
using namespace std;

ll n , j;

ll isPrime(ll j){

    ll i;
    for( i = 2; i*i <= j; ++i)
        if(j % i == 0)return i;

    return 0;
}

ll power(ll base , ll j){
    if(j == 0)return 1;
    if(j == 1)return base;
    ll ans = power(base , j/2);
    if(j % 2 == 1)return ans*ans*base;
    return ans*ans;
}

ll convert(ll x , ll base){
    ll sum = 0 , j = 0;

    while(x){

        if(x % 2 == 1)sum += power(base , j);
        x/=2;
        ++j;

    }

    return sum;

}

void con(ll x){
    if(x == 0)return;
    con(x/2);
    printf("%d" , x%2);
}

void solve(int i , ll x){
    if(i == n-1){
        if(x % 2 == 0)return;
        vector<ll> ans;
        bool yes = true;
        for(int i = 2; yes && i <= 10; ++i){
            ll z = convert(x , i);
            ll k = isPrime(z);
            if(k == 0)yes = false;
            else{
                ans.push_back(k);
            }
        }
        if(!yes)return;
        con(x);
        printf(" ");
        for(int i = 0; i < ans.size(); ++i){
            printf("%d " , ans[i]);
        }
        printf("\n");
        --j;
        if(j == 0)exit(0);
        return;
    }
    solve(i+1 , x*2);
    solve(i+1 , x*2+1);
}

int main(){
    freopen ("C-small-attempt2.in", "r", stdin);
	freopen ("ans.out","w",stdout);
    ll t;
    cin >> t;
    for(int z = 1; z <= t;++z){
        cin >> n >> j;
        printf("Case #%d:\n" , z);
        solve(0 , 1);
    }

    return 0;
}
