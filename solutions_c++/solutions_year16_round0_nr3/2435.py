#include <bits/stdc++.h>
using namespace std;
typedef unsigned long long int ull;
typedef long long int ll;
#define FOR(i,a,b) for (int i=(a); i<(b); i++)
typedef pair<int,int> PII;
typedef pair<int,pair<int,int> > PIII;
typedef pair<ll,ll> PLL;

//const ll MMM=1000000;
//bool isprime[MMM];
//int  yakusuu[MMM];
//

string i2b(ll a, ll len)
{
    string res;
    FOR(i,0,len) {
        res.push_back( ((a>>(len-i-1))&1) + '0' );
    }
    return res;
}

// xを基底baseで認識
ll toInt(ll x, int base) {
    ll res=0, p=1;
    FOR(i,0,64) {
        res += ((x>>i) & 1) * p;
        p *= base;
    }
    return res;
}

// ビット列xの各baseにおける数の集合
vector<ll> nums(ll x) {
    vector<ll> res;
    FOR(base,2,11){
        res.push_back(toInt(x,base));
    }
    return res;
}
//
// 返値: jamcoinかどうか
// vec: 約数一覧
//bool isjamcoin (ll x, int len, vector<int> &vec) {
    //vec = nums(x);
//}

// jamcoinkどうか
//bool isjamcoin(ll x, int len) {
//}

map<ll,ll> memo;
ll yakusuu(ll x) {
    if(memo.find(x) != memo.end()) { return memo[x]; }
    ll ans=-1;
    for(ll i=2; i<=sqrt(x); i++) {
        if(x%i==0) {
            ans=i;
            break;
        }
    } 
    return memo[x]=ans;
}

int main(void) {
    // 素数表を作成
    //FOR(i,0,MMM) isprime[i]=true;
    //isprime[0] = isprime[1] = false;
    //FOR(i,2,MMM) {
    //    if(isprime[i]){
    //        for (int k=2; k*i < MMM; k++) {
    //            isprime[k*i] = false;
    //            yakusuu[k*i] = i;
    //        }
    //    }
    //}

    //FOR(i,0,20) {
    //    if(isprime[i]) {
    //        cout<<i<<endl;
    //    }
    //}
    //ll x = 9;
    //auto vec = nums(x);
    //for (auto x: vec) {
    //    cout<<x<<endl;
    //}

    int T;
    cin>>T;
    FOR(t,0,T) {
        int N,J,k=0;
        cin>>N>>J;

        cout<<"Case #"<<(t+1)<<":"<<endl;
        for (ull i=0; i<1<<(N-2); i++) {
            ll x = (1L<<(N-1)) + (i<<1) +1L;
            vector<ll> vec = nums(x);
            vector<ll> yaku(9);  //約数一覧
            bool isjamcoin = true;
            FOR(i,0,9) {
                yaku[i] = yakusuu(vec[i]);
                if(yaku[i]==-1) {
                    isjamcoin = false;
                    break;
                }
            }
            if(isjamcoin) {
                cout<<i2b(x,N);
                //cout<<x;
                // 約数一覧
                FOR(i,0,9) {
                    cout<<" "<<yaku[i];
                }
                cout<<endl;
                k++;
            }
            if(k>=J) { break; }
        }
    }
    return 0;
}
