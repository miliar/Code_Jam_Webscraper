#include <bits/stdc++.h>
#include <fstream>
#define INF 800000000000
#define MOD 1000000007
#define MAXN 100005
#define ins insert
#define pb push_back
#define mp make_pair
#define sz size
#define all(a) a.begin(), a.end()
#define rep(i, a, b) for(int i = a; i < b; ++i)
#define sd(n) scanf("%d",&n)
#define sll(n) scanf("%I64d",&n)
#define pdn(n) printf("%d\n",n)
#define plln(n) printf("%I64d\n",n)
#define pd(n) printf("%d ",n)
#define nl() printf("\n")
using namespace std;

typedef long long ll;
typedef unsigned long long ull;
typedef vector<int> vl;
typedef vector<ll> vi;
typedef vector<vi> vvi;
typedef vector<vl> vvl;
typedef pair<int, int> pii;

namespace patch
{
    template < typename T > std::string to_string( const T& n )
    {
        std::ostringstream stm ;
        stm << n ;
        return stm.str() ;
    }
}

ll modpow(ll base, ll exponent, ll modulus)
{
    ll result = 1;
    while (exponent > 0)
    {
        if (exponent % 2 == 1)
            result = (result * base) % modulus;
        exponent = exponent >> 1;
        base = (base * base) % modulus;
    }
    return result;
}

ll gcd(ll u, ll v)
{
    return (v != 0) ? gcd(v, u % v) : u;
}

ll mulmod(ll a, ll b, ll c){
    ll x = 0, y = a%c;
    while(b > 0){
        if(b%2 == 1){
            x = (x+y) % c;
        }
        y = (y*2) % c;
        b /= 2;
    }
    return x%c;
}

int t; 
ll n;

int main() {
    ios_base::sync_with_stdio(0); cin.tie(0); cout.tie(0);
    cin >> t;
    rep(i, 0, t) {
        cout << "Case #" << i+1 << ": ";
        cin >> n;
        if(!n) {
            cout << "INSOMNIA\n";
            continue;
        }
        int mask = 0;
        rep(j, 1, 500001) {
            ll temp = (ll)j*n;
            while(temp) {
                mask |= 1<<(temp%10);
                temp /= 10;
            }
            if(mask == 1023) {
                cout << j*n << '\n';
                break;
            }
        }
    }
    return 0;
}