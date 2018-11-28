#include <bits/stdc++.h>

using namespace std;

#define endl '\n'
#define SZ(c) ((int)(c).size())
#define sqr(x) ((x)*(x))
#define REP(i, c) for(int i=0; i<c; i++)
#ifdef ONLINE_JUDGE
    #define WAIT
#else
    #define WAIT cout<<flush, system("PAUSE")
#endif

typedef long long ll;
typedef pair<int, int> pii;

ll get_div(ll x) {
    if (x % 2 == 0) return 2;
    
    for (ll d = 3; d*d <= x; d+=2)
        if (x % d == 0)
            return d;
    return 1;
}

ll log_mul(ll a, ll b, ll mod) {
    ll s = 0;
    while (b) {
        if (b & 1)
            s = (s + a) % mod;
        a = (a + a) % mod;
        b >>= 1;
    }
    return s;
}
ll log_pow(ll b, ll e, ll mod) {
    ll r = 1;
    while (e) {
        if (e & 1)
            r = log_mul(r, b, mod);
        b = log_mul(b, b, mod);
        e >>= 1;
    }
    return r;
}

ll pr(ll n) //n shouldn't be prime
{
    if(!(n&1)) return 2;
    while(true)
    {
        ll x=(ll)rand()%n,y=x;
        ll c=rand()%n;
        if(c==0||c==2) c=1;
        for(int i=1,k=2;;i++)
        {
            x=log_mul(x,x,n);
            if(x>=c) x-=c; else x+=n-c;
            if(x==n) x=0;
            if(x==0) x=n-1; else x--;
            ll d=__gcd(x>y?x-y:y-x,n);
            if(d==n) break;
            if(d!=1) return d;
            if(i==k) {y=x;k<<=1;}
        }
    }
}


bool witness(ll a, ll s, ll d, ll n)
{
	ll x = log_pow(a, d, n);
	if (x == 1 || x == n - 1) return false; // composite
	for (int i = 0; i < s-1; i++) {
		x = log_mul(x, x, n);
		if (x == 1) return true; // probably prime
		if (x == n - 1) return false; // composite
	}
	return true; // probably prime
}

bool is_prime(ll n)
{
	if (n < 2) return false;
	if (n == 2) return true;
	if (n % 2 == 0) return false;
	ll d = n - 1, s = 0;
	while (d % 2 == 0) ++s, d /= 2;
	ll test[] = {2, 3, 5, 7, 11, 13, 17, 19, 23, 0};
	for (int i = 0; test[i] && test[i] < n; ++i)
		if (witness(test[i], s, d, n))
			return false; // composite
	return true; // probably prime
}


const int N = 16;

ll tc, n, k;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    
    cin >> tc;
    cin >> n >> k;
    
    ll s = (1LL << (n-1)) + 1;
    n -= 2;
    int cnt = 0;
    
    cout << "Case #1:" << endl;
    //for (ll i = 0; i < (1LL << n) && k > 0; i+=6) {
    for (ll i = (1LL << n) - 1; i >= 0 && k > 0; i--) {
        ll x = s + 2*i;
        
        vector<ll> v;
        for (ll b = 2; b <= 10; b++) {
            ll y = x;
            ll p = 1;
            ll z = 0;
            while (y > 0) {
                if (y & 1)
                    z += p;
                p *= b;
                y >>= 1;
            }
            
            ll d = get_div(z);
            if (d == 1) {
                v.clear();
                break;
            }
            
            
            /*
            if (is_prime(z)) {
                v.clear();
                break;
            }
            ll d;
            do { d = pr(z); } while (d == 1 || d == z); 
            */
            
            v.push_back(d);
        }
        if (!v.empty()) {
            k--;
            cnt++;
            //cout << x << endl;
            cout << bitset<N>(x);
            for (auto z : v)
                cout << " " << z;
            cout << endl;
        }
    }
    //cout << cnt << endl;

//    WAIT;
}
