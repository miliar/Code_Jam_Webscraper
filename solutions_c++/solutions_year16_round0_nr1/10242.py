#include <bits/stdc++.h>

#define pb push_back
#define endl "\n"
#define mp make_pair 
#define fi first
#define se second
#define all(x) x.begin(), x.end()
#define fname ""
#define sz(x) (int)(x.size())
#define rep(i,x,y) for(long long i=x;i<=y;++i)
#define repr(i,x,y) for(long long i=x;i>=y;--i)

typedef long long ll;

using namespace std;

const ll N = (ll)(5e5) + 322;
const ll INF = (ll)(1e9);
const ll mod = (ll)(1e9) + 7;
const double eps = 1e-9;

int n, x, test; 

int main () {
	ios_base :: sync_with_stdio (false); cin.tie(0);
	//freopen(fname".in", "r", stdin);
	//freopen(fname".out", "w", stdout);
	cin >> n;
	rep(i, 1, n) {
		cin >> x;
		if (x == 0) {
			cout << "Case #"<< i <<": " << "INSOMNIA" << endl;
		}else {
			int mask = 0, cur = 0, q = 0;
			while (mask != 1023) {
			  cur += x;
				q = cur;
				while (q) {
					mask |= (1 << (q % 10));	
					q /= 10;	
				}
			}	
			cout << "Case #"<< i <<": "<< cur << endl;
		}
	}
	return 0;
} 
