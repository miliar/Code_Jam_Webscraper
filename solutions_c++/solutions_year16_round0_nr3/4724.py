#include <bits/stdc++.h>

#define PI 3.141592653589793
#define EPS 0.000000001
#define INF 1000000000

#define _ ios_base::sync_with_stdio(0), cin.tie(0), cin.tie(0), cout.tie(0), cout.precision(15);
#define FOR(i, a, b) for(int i=int(a); i<int(b); i++)
#define FORC(cont, it) for(typeof((cont).begin()) it = (cont).begin(); it != (cont).end(); it++)
#define pb push_back

using namespace std;

typedef long long ll;
typedef pair<int, int> ii;
typedef vector<int> vi;
typedef vector<ii> vii;
typedef vector<ll> vl;

#define MAXN 10
#define MOD 1000000007

ll pot[13][20];
ll N, j;
int cant = 0;

// ********************************  IS PRIME()   *****************************************
//Para TODOS los primos

ll mulmod(ll a, ll b, ll c) { // returns (a * b) % c, and minimize overflow
	ll x = 0, y = a % c;
	while (b) {
		if (b & 1) x = (x + y) % c;
		y = (y<<1) % c;
		b >>= 1;
	}
	return x % c;
}

ll fastPow(ll x, ll n, ll c) { // returns (a ** b) % c, and minimize overflow
	ll ret = 1;
	while (n) {
		if (n & 1) ret = mulmod(ret, x, c);
		x = mulmod(x, x, c);
		n >>= 1;
	}
	return ret;
}

// Miller-Rabin primality test
bool millerRabin(ll n) {
	ll d = n - 1;
	int s = 0;
	while (d % 2 == 0) {
		s++;
		d >>= 1;
	}
	// It's garanteed that these values will work for any number smaller than 2^64
	int a[12] = { 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37 };
	FOR(i, 0, 12) {
	    if(n==a[i]) return true;
	}
	FOR(i, 0, 12) {
	    bool comp = fastPow(a[i], d, n) != 1;
		if(comp) FOR(j, 0, s) {
			ll fp = fastPow(a[i], (1LL << (ll)j)*d, n);
			if (fp == n - 1) {
				comp = false;
				break;
			}
		}
		if(comp) return false;
	}
	return true;
}
// ****************************************************************************************


// ********************************  GET PRIME FACTORS()   ********************************
/*
 Devuele los factores primos de un numero. No olvidar hacer unique para quitar repetidos
 int tamano = unique(factors.begin(), factors.end()) - factors.begin();
*/

ll A, B;

ll f(ll x, ll n) {
    return (mulmod(x, (x + A), n) + B) % n;
}

ll pollardRho(ll n) {
    ll d = n, x, y;
    while(d == n) {
        d = 1;
        x = y = 2;
        A = 2 + rand() % (n - 2);
        B = 2 + rand() % (n - 2);

        while (d == 1) {
            x = f(x, n);
            y = f(f(y, n), n);
            d = __gcd(abs(x - y), n);
        }
    }

	return d;
}
// ****************************************************************************************

// To return value of a char. For example, 2 is
// returned for '2'.  10 is returned for 'A', 11
// for 'B'
ll val(char c) {
    if (c >= '0' && c <= '9')
        return (ll)c - '0';
    else
        return (ll)c - 'A' + 10;
}

// Function to convert a number from given base 'b'
// to decimal
ll toDeci(string str, int base) {
    ll len = str.length();
    ll num = 0;

    for (int i = len - 1, j = 0; i >= 0; i--, j++) {
        num += val(str[i]) * pot[base][j];
    }

    return num;
}

void solve(string s) {
    ll numeros[11];
    FOR(i, 2, 11) {
        numeros[i] = toDeci(s, i);
        if(millerRabin(numeros[i])) {
            return;
        }
        //cout << i << endl;
    }

    cout << s << " ";
    FOR(i, 2, 11) {
        cout << pollardRho(numeros[i]) << " \n"[i==10];
    }
    cant++;
    //cout << "salgo con cant " << cant << endl;
    //cout << cant << " " << s << endl;
}

void gen(string s) {
    if (cant == j)  return;
    if (s.length() == N - 1) {
        return solve(s + "1");
    }
    //cout << s << endl;
    gen(s + "1");
    gen(s + "0");
}



int main(){ _
    freopen("c.in", "r", stdin);
    freopen("c.out", "w", stdout);

    FOR(i, 0, 13) {
        pot[i][j] = 1;
        FOR(j, 1, 20) {
            pot[i][j] = pot[i][j-1] * i;
        }
    }

    int T;
    cin >> T;

    FOR(t, 1, T+1) {
        cin >> N >> j;
        cout << "Case #" << t << ":" << endl;

        string s = "1";
        gen(s);
    }

    return 0;
}


