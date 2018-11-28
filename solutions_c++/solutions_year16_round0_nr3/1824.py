#include<bits/stdc++.h>
using namespace std;
#define FOR(i,a,b) for(int i = (a); i <= (b); ++i)
#define FORD(i,a,b) for(int i = (a); i >= (b); --i)
#define RI(i,n) FOR(i,1,(n))
#define REP(i,n) FOR(i,0,(n)-1)
#define mini(a,b) a=min(a,b)
#define maxi(a,b) a=max(a,b)
#define mp make_pair
#define pb push_back
#define st first
#define nd second
#define sz(w) (int) w.size()
typedef vector<int> vi;
typedef long long ll;
typedef long double ld;
typedef unsigned int ui;
typedef pair<int,int> pii;
const int inf = 1e9 + 5;
const int nax = 1e6 + 5;

vector<vector<ll> > wynik;

vector<ll> witness = {2, 325, 9375, 28178, 450775, 9780504, 1795265022}; // < 2^64

__int128 mnoz(__int128 a, __int128 b, __int128 mod) {
	//return (__int128(a)*b)%mod;
	
	__int128 res = 0;
	while (b) {
		if (b&1) res = (res+a)%mod;
		a = (a+a)%mod;
		b /= 2; //bez modulo szybciej
	}
	return res;
}

__int128 pot(__int128 a, __int128 b, __int128 mod) {
	__int128 res = 1;
	while (b) {
		if (b&1)
			res = mnoz(res,a,mod);
		a = mnoz(a,a,mod);
		b /= 2;
	}
	return res;
}

bool test(__int128 n) {
	if (n == 2)
		return true;
	if (n < 2 || n%2 == 0)
		return false;
	
	__int128 d = n-1;
	__int128 s = 0;
	while (d%2 == 0) {
		d /= 2;
		++s;
	}
	
	for (auto i: witness) if (i%n) {
		__int128 x = pot(i,d,n);
		if (x != 1) {
			bool zlozona = true;
			REP(j,s) {
				if (x == n-1) {
					zlozona = false;
					break;
				}
				x = (x*x)%n;
			}
			if (zlozona)
				return false;
		}
	}
	
	return true;
}



__int128 nwd(__int128 a, __int128 b) {
	return a ? nwd(b%a,a) : b;
}

__int128 f(__int128 x, __int128 mod, __int128 c) {
	ll y = mnoz(x,x,mod) + c;
	if (y > mod)
		y -= mod;
	return y;
}

__int128 absll(__int128 x) {
  if (x < 0) return -x;
  return x;
}

ll rho(__int128 n) {
  FOR(i,2,10000) if (n%i == 0) return i;
  return -1;
  
	if (n <= 1) return -1;
	if (test(n)) {
		return -1;
	}
	
	ll c = 1;
  while(true) {
		__int128 x = 2, y = 2, d = 1;
		while (d == 1) {
			x = f(x,n,c);
			y = f(f(y,n,c),n,c);
			d = nwd(absll(x-y),n);
		}
		if (d < n) {
			return min(d, n/d);
		}
		++c;
    if (c == 10) return -1; 
	}
}


bool check(ui x, int i) {
  fprintf(stderr,"badam %u\n",x);
  wynik[i].pb(x);
  vi c;
  while (x) {
    c.pb(x&1);
    x >>= 1;
  }
  reverse(c.begin(), c.end());
  
  FOR(b,2,10) {
    __int128 l = 0;
    for (auto cc: c) {
      l = l * b + cc;
    }
    
    ll x = rho(l);
    if (x == -1) return false;
    wynik[i].pb(x);
  }
  return true;
}

ui losuj(int dl) {
  ll x = 1LL << (dl-1);
  x += rand()%(x);
  x |= 1;
  return x;
}

void binarnie(ll x) {
  vi res;
  while (x) {
    res.pb(x&1);
    x /= 2;
  }
  reverse(res.begin(), res.end());
  for (auto c: res) printf("%d",c);
}

void licz(int j, int n) {
  set<ui> secik;
  wynik.resize(n);
  
  REP(i,n) {
    fprintf(stderr,"%d\n",i);
    ui x = losuj(j);
    while (secik.count(x) == 1 || !check(x, i)) {
      wynik[i].clear();
      x = losuj(j);
    }
  }
  
  for (auto w: wynik) {
    binarnie(w[0]);
    FOR(i,1,9) printf(" %lld",w[i]); puts("");
  }
}

int main() {
  srand(420);	
  printf("Case #1:\n");
  licz(32, 500);
	return 0;
}
