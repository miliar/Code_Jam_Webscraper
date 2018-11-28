#include <bits/stdc++.h>
using namespace std;

#define pb push_back
#define mp make_pair
#define PI 3.14159265358979323846
#define FILE "A-large"

#define LOCIN 0
#define LOCOUT 0
#define DEBUG 0
#define dout if(DEBUG) cout

typedef long long ll;
typedef unsigned long long ull;


const int INF = numeric_limits<int>::max();
const ll LINF = numeric_limits<ll>::max();

const double EPS = 1e-9;
const ll MOD = 1000000007;
const int MAXN = 1000;
int test = 0;


void solve() {
    ll n; cin >> n;
    if(!n) {
		cout << "INSOMNIA";
		return;
    }
    bool left[10];
    for(ll i = 0; i < 10; ++i)
		left[i] = false;
	for(ll i = 1; i < 10000; ++i) {
        ll x = n * i;
        while(x) {
			left[x%10] = true;
			x/=10;
        }
        bool ok = true;
        for(ll j = 0; j < 10; ++j)
			if(left[j] == false)
				ok = false;
		if(ok) {
			cout << n*i;
			return;
		}
	}
	cout << "INSOMNIA";
}

int main() {
    if(!LOCIN)
		freopen(FILE".in", "r", stdin);
	if(!LOCOUT)
		freopen(FILE".out", "w", stdout);
	int t; cin >> t;
	for(test = 0; test < t; ++test) {
        cout << "Case #" << test+1 << ": ";
        solve();
        cout << "\n";
	}
}
