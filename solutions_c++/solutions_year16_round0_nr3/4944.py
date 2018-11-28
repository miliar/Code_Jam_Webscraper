#include<bits/stdc++.h>
#define ll long long

using namespace std;

#define N   11234567

bool isPrime[N+1];
ll Divisor[N+1];

ll power(ll a, ll b) {
    ll r = 1;
    while(b) {
        if(b & 1) r = r * a ;
        a = a * a;
        b >>= 1;
    }
    return r;
}

void sieve() {
    for(ll i = 0; i <= N;++i) {
        isPrime[i] = true;
    }
    for(ll i = 2; i * i <= N; ++i) {
        if(isPrime[i] == true) {
            for(ll j = i * i; j <= N ;j += i){
                isPrime[j] = false;
                Divisor[j] = i;
            }
        }
    }
}

int main(){
    #ifndef ONLINE_JUDGE
            freopen("C-small-attempt0.in","r",stdin);
            freopen("output.txt","w",stdout);
    #endif
    sieve();
    int t;
    cin >> t;
    for(int qq = 1; qq <= t; qq++){
        printf("Case #%d:\n",qq);
        ll n,k;
        cin >> n >> k;
        ll x = power(2,n-1);
        ll p2n = power(2,n);
        ll cnt = 0;
        for(ll i = x; i < p2n; i++){
            string Inbinary = bitset<32>(i).to_string();
            if( Inbinary[31] != '1' )   continue;
            string rev = Inbinary;
            reverse(rev.begin(),rev.end());
            int c = 0;
            vector<ll>v;
            for(ll j = 2; j <= 10; j++){
                ll cur = 0;
                for(ll l = 0; l <= 32; l++ ){
                    if( rev[l] == '1' ){
                        cur += power(j,l);
                    }
                }
                if( cur < N && !isPrime[cur] ){
                    c++;
                    v.push_back(Divisor[cur]);
                }
                else if( cur >= N ){
                    bool flag = true;
                    ll Di;
                    for(ll idx = 2 ; idx * idx <= cur ; idx++){
                        if( cur%idx == 0 ){
                            flag = false;
                            Di = idx;
                            break;
                        }
                    }
                    if( !flag ){
                        c++;
                        v.push_back(Di);
                    }
                }
            }
            if( c == 9 ){
                cout << Inbinary.substr(Inbinary.length()-n,n) << " ";
                for(ll m = 0; m < 9; m++){
                    cout << v[m] << " ";
                }
                cout << endl;
                cnt++;
                if( cnt == k )  break;
            }
        }
    }
    return 0;
}
