#include <iterator>
#include <cstring>
#include <map>
#include <deque>
#include <queue>
#include <stack>
#include <sstream>
#include <bitset>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <fstream>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <algorithm>
#include <numeric>
#include <vector>
#include <set>
#include <complex>
#include <list>
#include <valarray>
#ifdef _MSC_VER
#include <hash_set>
#include <hash_map>
using namespace stdext;
#else
#include <ext/hash_set>
#include <ext/hash_map>
using namespace __gnu_cxx;
#endif
using namespace std;

#define SZ(v)                   (int)v.size()
#define FOR(i,a,b)				for(int i=(a);i<(b);++i)
#define rev(i,a,b)				for(int i=(b);i>=(a);--i)
#define sz(v)                   (int)v.size()
#define all(v)					v.begin(), v.end()
#define rall(v)					v.rbegin(), v.rend()
#define pb						push_back
#define mp						make_pair
typedef long long ll;
typedef vector<int> vi;
typedef pair<int,int> pi;
typedef vector<pi> vpi;
const int OO = 1 << 28;

int di[] = { -1, 0, 1, 0 };
int dj[] = { 0, 1, 0, -1 };
#define Nd 0
#define Ed 1
#define Sd 2
#define Wd 3

ll n,p;

ll worst(ll rnk){
	ll loses = 0;
	while(rnk){
		loses ++;
		rnk = (rnk-1)/2;
	}
	ll ret = 0;
	FOR(i,0,loses){
		ret |= (1LL<<(n-i-1));
	}
	return ret;
}
ll best(ll rnk){
	ll wins = 0;
	ll rem = (1LL<<n)-rnk-1;
	while(rem){
		wins ++;
		rem = (rem-1)/2;
	}
	ll ret = 0;
	FOR(i,0,n-wins){
		ret |= (1LL<<i);
	}
	return ret;
}
int main() {
#ifndef ONLINE_JUDGE
	freopen("in.in", "rt", stdin);
	freopen("out.out", "wt", stdout);
#endif
//	n = 3;
//	FOR(i,0,8)
//		cout << best(i) << endl;
	int t;
	cin >> t;
	FOR(cs,1,t+1){
		cin >> n >> p;
		ll st = 0, end = (1LL<<n)-1;
		cout << "Case #" << cs<<": ";
		while(st < end){
			ll mid = st + (end - st + 1)/2;
			if(worst(mid) < p)
				st = mid;
			else
				end = mid - 1;
		}
		cout << st << " ";
		st = 0, end = (1LL<<n)-1;
		while(st < end){
			ll mid = st + (end - st + 1)/2;
			if(best(mid) < p)
				st = mid;
			else
				end = mid - 1;
		}
		cout << st << "\n";
	}
	return 0;
}




