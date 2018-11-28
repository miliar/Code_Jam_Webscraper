#include <bits/stdc++.h>
using namespace std;
#define dprint(v) cerr << #v"=" << v << endl //;)
#define forr(i,a,b) for(int i=(a); i<(b); i++)
#define forn(i,n) forr(i,0,n)
#define dforn(i,n) for(int i=n-1; i>=0; i--)
#define forall(it,v) for(typeof(v.begin()) it=v.begin();it!=v.end();++it)
#define sz(c) ((int)c.size())
#define zero(v) memset(v, 0, sizeof(v))
#define fst first
#define snd second
#define mkp make_pair
#define pb push_back
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

bool es_primo_prob (ll n, int a)
{
	if (n == a) return true;
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
    if( (n & 1) == 0 ) return 2;
    ll x = 2 , y = 2 , d = 1;
    ll c = rand() % n + 1;
    while( d == 1 ){
        x = (mulmod( x , x , n ) + c)%n;
        y = (mulmod( y , y , n ) + c)%n;
        y = (mulmod( y , y , n ) + c)%n;
        if( x - y >= 0 ) d = gcd( x - y , n );
        else d = gcd( y - x , n );
    }
    return ( (d==n || d==1) ? rho(n) : d) ;
}

int n,j;
#define index(bm,i) ( ((bm)>>(i))&1 )

ll base(int bm, ll b) {
	if (bm==0) return 0;
	return ll(bm&1) + b * base(bm>>1,b);
}

int main() {
	//~ freopen("c.in", "r", stdin);
	//~ freopen("asd.in", "r", stdin);
	//~ freopen("asd.out", "w", stdout);
    ios::sync_with_stdio(0);
    int TC; scanf("%d",&TC);
     for(int tc=1 ; tc<=TC ; tc++) {
		scanf("%d %d",&n,&j);
		printf("Case #%d:\n",tc);
		forn(bm,(1<<(n-2))-1) {
			if (!j) break;
			int rbm = (1<<(n-1)) + (bm<<1) + 1;
			vector<int> r;
			forr(b,2,11) {
				ll num = base(rbm,b);
				if (!rabin(num))
					r.pb(rho(num));
			}
			if (sz(r)==9) {
				forn(i,n) printf("%d",index(rbm,n-1-i));
				printf(" ");
				forn(i,sz(r)) printf("%d%c",r[i],(i==sz(r)-1?'\n':' '));
				j--;
			}
		}
		
	}
	return 0;
}
