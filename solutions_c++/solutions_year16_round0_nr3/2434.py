#include <bits/stdc++.h>

#define si(n) scanf("%d", &n)
#define sii(n, m) scanf("%d %d", &n, &m)
#define sc(c) scanf("%c", &c)
#define ss(s) scanf("%s", s)

#define sz(x) (int)x.size()

#define forn(i, n) for(int i = 0 ; i < n ; ++i)
#define forr(i, a, b) for(int i = a ; i < b ; ++i)

#define rforn(i, n) for(int i = n-1 ; i >= 0 ; --i)
#define rforr(i, a, b) for(int i = b-1 ; i >= a ; --i)

#define mset(x, y) memset(x, y, sizeof(x))
#define all(x) x.begin(), x.end()

#define TEST(t) int T; cin >> T; for(int t = 1 ; t <= T ; ++t)

using namespace std;
typedef long long ll;
typedef vector<ll> vi;

vi v;

void add(vi &vt){
    int n = sz(vt);
    int r = 1;

    rforn(i, n){
        if(r == 0)break;
        if(v[i]){
            v[i] = 0;
            r = 1;
        }
        else{
            v[i] = 1;
            r = 0;
        }
    }
}

map<ll, ll> prime;

ll isPrime(ll n){
    if(prime.count(n))return prime[n];

    if(n <= 1)return prime[n] = -1;
    if(n == 2)return prime[n] = 2;
    if(n%2 == 0)return prime[n] = 2;

    int m = sqrt(n);

    for(int i = 3; i <= m; i += 2)if(n%i==0)return prime[n]= i;

    return prime[n] = -1;
}

ll check(int b, vi vt){
    int n = sz(vt);
    ll aux = 0LL;
    ll nb = 1LL;

    rforn(i, n){
        aux += vt[i]*nb*1LL;
        nb *= b;
    }

    return isPrime(aux);
}

ll print(int b, vi vt){
    int n = sz(vt);
    ll aux = 0LL;
    ll nb = 1LL;

    rforn(i, n){
        aux += vt[i]*nb*1LL;
        nb *= b*1LL;
    }
    cout << aux;
}

int main(){
    int n, j;
    freopen("C-small-attempt1.in", "r", stdin);
    freopen("C-small-attempt1.out", "w", stdout);
    TEST(t){
        printf("Case #%d:\n", t);
        sii(n, j);
        v.resize(n);
        v[0] = v[n-1] = 1;
        while(j){
            vi ans;
            ll x;

            forr(i, 2, 11){
                x = check(i, v);
                if(x == -1)break;
                ans.push_back(x);
            }

            if(x == -1){
                add(v);
                v[n-1] = 1;
                continue;
            }
            j--;

            forn(i, sz(v))printf("%d", v[i]);

            forn(i, sz(ans))printf(" %d", ans[i]);
            puts("");

            add(v);
            v[n-1] = 1;
        }
    }

    return 0;
}
