#include <cstdlib>
#include <cmath>
#include <climits>
#include <cfloat>
#include <map>
#include <utility>
#include <set>
#include <iostream>
#include <memory>
#include <string>
#include <vector>
#include <algorithm>
#include <functional>
#include <sstream>
#include <deque>
#include <complex>
#include <stack>
#include <queue>
#include <cstdio>
#include <cctype>
#include <cstring>
#include <ctime>
#include <iterator>
#include <bitset>
#include <numeric>
#include <list>
#include <iomanip>
using namespace std;


typedef long long LL;
typedef pair<int,int> pii;
typedef pair<LL,LL> pll;

typedef vector<int> vint;
typedef vector<vector<int> > vvint;
typedef vector<long long> vll, vLL;
typedef vector<vector<long long> > vvll, vvLL;

#define VV(T) vector<vector< T > >

template <class T>
void initvv(vector<vector<T> > &v, int a, int b, const T &t = T()){
	v.assign(a, vector<T>(b, t));
}

template <class F, class T>
void convert(const F &f, T &t){
	stringstream ss;
	ss << f;
	ss >> t;
}


#define REP(i,n) for(int i=0;i<int(n);++i)
#define ALL(v) (v).begin(),(v).end()
#define RALL(v) (v).rbegin(),(v).rend()
#define PB push_back
#define ITR ::iterator


#define MOD 1000002013LL
#define EPS 1e-8


LL calccost(LL n, LL d){
	return (n * d + d - d * (d + 1) / 2) % MOD;
}


LL solve(){
	LL n, m;
	cin >> n >> m;
	vLL fs(m), ts(m), ps(m);
	map<LL,LL> mp;
	
	LL pay = 0;
	for(int i = 0; i < m; ++i){
		cin >> fs[i] >> ts[i] >> ps[i];
		mp[fs[i]] += ps[i];
		mp[ts[i]] -= ps[i];
		pay += calccost(n, ts[i] - fs[i]) * ps[i];
		pay %= MOD;
	}
	vector<pll> ev(ALL(mp));

	LL sum = 0;
	stack<pll> st;
	for(int i = 0; i < ev.size(); ++i){
		if(ev[i].second > 0){
			st.push(ev[i]);
		}
		else if(ev[i].second < 0){
			LL t = -ev[i].second;
			while(t > 0){
				pll s = st.top();
				st.pop();
				LL p = min(s.second, t);
				t -= p;
				s.second -= p;
				if(s.second > 0){
					st.push(s);
				}
				
				sum += calccost(n, ev[i].first - s.first) * p;
				sum %= MOD;
			}
		}
	}

	return (pay - sum + MOD * 10) % MOD;
}


int main(){
	cout << fixed << setprecision(10);

	int T = 0;
	scanf("%d", &T);
	for(int i = 1; i <= T; ++i){
		fprintf(stderr, "%4d / %4d\n", i, T);
		cout << "Case #" << i << ": " << solve() << endl;
	}
}
