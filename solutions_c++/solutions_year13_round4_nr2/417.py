
#include <list>
#include <map>
#include <set>
#include <stack>
#include <queue>
#include <algorithm>
#include <sstream>
#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cstring>
#include <climits>
#include <cfloat>
#include <numeric>

using namespace std;

typedef long long ll;
typedef unsigned long long ull;
typedef vector<int> vi;
typedef vector<string> vs;
typedef pair<int, int> pii;

const int oo = 0x3f3f3f3f;
const double eps = 1e-9;

#define sz(c) int((c).size())
#define all(c) (c).begin(), (c).end()
#define FOR(i,a,b) for (int i = (a); i < (b); i++)
#define FORD(i,a,b) for (int i = int(b)-1; i >= (a); i--)
#define FORIT(i,c) for (__typeof__((c).begin()) i = (c).begin(); i != (c).end(); i++)
#define mp(a,b) make_pair(a,b)
#define pb(a) push_back(a)

ll P, N;

ll lowPos(ll r, ll n){
	if(r == 0)return 0;
	if(r == n-1)return n-1;
	return n / 2 + lowPos((r - 1) / 2, n / 2);
}

ll hiPos(ll r, ll n){
	if(r == 0)return 0;
	if(r == n-1)return n-1;
	return hiPos((r + 1) / 2, n / 2);
}

ll calc(){
	cin >> N >> P;
	ll lo = 0, hi = (1LL<<N) - 1;
	while(lo < hi){
		ll mid = lo + ( hi - lo + 1) / 2;
		if(lowPos(mid, 1LL<<N) >= P)hi = mid - 1;
		else lo = mid;
	}
	cout << lo;
	lo = 0, hi = (1LL << N) - 1;
	while(lo < hi){
		ll mid = lo + (hi - lo + 1) / 2;
		if(hiPos(mid , 1LL<<N) >= P)hi = mid - 1;
		else lo = mid;
	}
	cout << " " << lo << endl;
}

int main() {
	int tc;
	cin >> tc;
	FOR(tcc, 1, tc + 1){
		cout << "Case #" << tcc << ": ";
		calc();
	}
	return 0;
}
