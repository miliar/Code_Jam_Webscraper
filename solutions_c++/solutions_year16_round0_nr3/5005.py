#include <bits/stdc++.h>
using namespace std;
#define dprint(v) cerr << #v"=" << v << endl //;)
#define forr(i,a,b) for(int i=(a); i<(b); i++)
#define forn(i,n) forr(i,0,n)
#define dforn(i,n) for(int i=n-1; i>=0; i--)
#define forall(it,v) for(auto it=v.begin();it!=v.end();++it)
#define sz(c) ((int)c.size())
#define zero(v) memset(v, 0, sizeof(v))
#define pb push_back
#define fst first
#define snd second
typedef long long ll;
typedef pair<int,int> ii;


ll gcd(ll a, ll b){return a?gcd(b %a, a):b;}

ll mulmod (ll a, ll b, ll c) { //returns (a*b)%c, and minimize overfloor
	ll x = 0, y = a%c;
	while (b > 0){
		if (b % 2 == 1) x = (x+y) % c;
		y = (y*2) % c;
		b /= 2;
	}
	return x % c;
}

ll expmod (ll b, ll e, ll m){//O(log b)
	if(!e) return 1;
	ll q= expmod(b,e/2,m); q=mulmod(q,q,m);
	return e%2? mulmod(b,q,m) : q;
}

bool es_primo_prob (ll n, ll a)
{
	if (n==a) return true;
	if (n%a==0) return false;
	ll s = 0,d = n-1;
	while (d % 2 == 0) s++,d/=2;
	
	ll x = expmod(a,d,n);
	if ((x == 1) || (x+1 == n)) return true;
	
	forn (i, s-1){
		x = mulmod(x, x, n);
		if (x == 1) return false;
		if (x+1 == n) return true;
	}
	return false;
}
		
bool rabin (ll n){ //devuelve true si n es primo
	if (n == 1)	return false;
	const int ar[] = {2,3,5,7,11,13,17,19,23};
	forn (j,9)
		if (!es_primo_prob(n,ar[j]))
			return false;
	return true;
}

ll rho(ll n){
    forr(i, 2, sqrt(n)+1){
        if(n%i==0) return i;
    }
    if( (n & 1) == 0 ) return 2;
    if( n==9) return 3;
    ll x = 2 , y = 2 , d = 1;
    ll c = rand() % n + 1;
    while( d == 1 ){
        x = (mulmod( x , x , n ) + c)%n;
        y = (mulmod( y , y , n ) + c)%n;
        y = (mulmod( y , y , n ) + c)%n;
        if( x - y >= 0 ) d = gcd( x - y , n );
        else d = gcd( y - x , n );
    }
    return d;
}
int N,J;

ll trans(ll x, ll b){
    ll r=0;
    ll mul=1;
    while(x){
        if(x&1) r+=mul;
        mul*=b;
        x>>=1;
    }
    return r;
}

void print(ll x){
    if(!x) cout << 0;
    vector<bool> ans;
    while(x){
        ans.pb(x&1);
        x>>=1;
    }
    dforn(i, sz(ans)) cout << ans[i];
}

ll fa[30];
ll conv[30];
bool is_coin(ll x){
    forr(b, 2, 11){
        //~ dprint(b);
        conv[b]=trans(x, b);
        
        assert(conv[b]>0);
        //~ assert(conv[b]<MAXP);
        if(rabin(conv[b])) return false;
    }
    forr(b, 2, 11){
        //~ dprint(b);
        //~ dprint(conv[b]);
        fa[b]=rho(conv[b]);
        //~ dprint(conv[b]);
        //~ dprint(fa[b]);
        //~ dprint(conv[b]);
        //~ dprint(fa[b]);
        assert(conv[b]!=fa[b]);
        assert(1!=fa[b]);
        assert(conv[b]%fa[b]==0);
    }
    return true;
}

int main() {
    //~ freopen("input.in", "r", stdin);
    freopen("C-small-attempt0.in", "r", stdin);
    //~ freopen("C-large.in", "r", stdin);
    freopen("asd.out", "w", stdout);
    ios::sync_with_stdio(0);    
    int TC; cin >> TC;
    for(int TT=1; TT<=TC; TT++){
        cout << "Case #" << TT << ":\n";
        cin >> N >> J;
        for(ll i=0; J && i<=1<<(N-2); i++){
            ll x=(2*i+1)^(1LL<<(N-1));
            //~ if(i%10==0) dprint(i);
            //~ print(x); cout << endl;
            if(is_coin(x)){
                print(x);
                forr(b, 2, 11) cout << ' ' << fa[b];
                cout << endl;
                J--;
            }
        }
        cout << endl;
    }
    return 0;
}
