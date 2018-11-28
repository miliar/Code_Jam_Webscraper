#include <iostream>
#include <string>
#include <vector>
#include <deque>
#include <map>
#include <set>
#include <cmath>
#include <cstdio>
#include <algorithm>
#include <string>
#include <sstream>
typedef long long ll;
using namespace std;

#define FORi(n) for(int i=0;i<n;++i)
#define FOR(i,a,b) for(int i=a;i<=b;++i)
#define mp make_pair
#define pb push_back
#define sz(x) int((x).size())

string inttostr (int a) {
    string s;
    ostringstream os;
    os << a;
    s = os.str();
    return s;
}

int solve_simple (ll E, ll R, ll N, vector<ll> v) {
	vector<ll> gn (E+1,0);
	vector<ll> gn2(E+1,0);
	FORi(N) {
		for (ll s = 0; s <= E; ++s) {
			ll g = v[i]*s;
			for (ll k = s; k <= E; ++k) {
				ll new_en = min(k-s+R,E);
				gn2[new_en] = max(gn[k]+g,gn2[new_en]);
			}
		}
		for (ll j = 0; j <= E; ++j) {
			gn[j]  = gn2[j];
		}
	}
	ll res = 0;
	FORi(E+1) res = max(res,gn[i]);
	return res;
}

void solve () {
	int Ntests = 0;
	cin >> Ntests;
	for (int test_id = 1; test_id <= Ntests; test_id++) {
		ll E, R, N;
		cin >> E >> R >> N;
		vector<ll> v (N,0);
		FORi(N) cin>>v[i];
		cout << "Case #" << test_id << ": " << solve_simple(E,R,N,v) << endl;
	}
}

void main()
{
    #ifdef _DEBUG
        freopen("input.txt","r",stdin);
        freopen("output.txt","w",stdout);
    #endif

    solve();
}