#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <queue>
#include <map>
#include <set>
#include <deque>
#include <bitset>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cctype>
#include <queue>
#include <cstring>
#include <stack>
#include <assert.h>
using namespace std;

#define IT(c) typeof((c).begin())

#define For(i, a, b) for(int (i) =  int(a); i < int(b); ++i)
#define rep(x, n) For(x,0,n)
#define foreach(i, c) for(IT(c) i = (c).begin(); i != (c).end(); ++i)

#define sz(a) int((a).size())
#define pb push_back
#define mp make_pair
#define F first
#define S second

template<class T>
ostream& operator<<(ostream& out, vector<T> v){
	out << "[";
	rep(i, sz(v)){
		if(i) out << ", ";
		out << v[i];
	}
	out << "]";
	return out;
}
template<class A, class B>
ostream& operator<<(ostream& out, pair<A,B> p){
	out << "<" << p.F << ", " << p.S << ">";
	return out;
}
template<class T>
ostream& operator<<(ostream& out, set<T> s){
	out << "(";
	foreach(it, s){
		if(it != s.begin()) out << ", ";
		out << *it;
	}
	out << ")";
	return out;
}
template<class A, class B>
ostream& operator<<(ostream& out, map<A,B> m){
	out << "{";
	foreach(it, m){
		if(it != m.begin()) out << ", ";
		out << *it;
	}
	out << "}";
	return out;
}

typedef long long ll;

const ll mod = 1000002013;
ll add(ll a, ll b){
	return (a+b)%mod;
}
ll mul(ll a, ll b){
	return (a*b)%mod;
}
ll sub(ll a, ll b){
	return (a-b+mod)%mod;
}

ll N;

ll calc(ll dist){
	return sub(mul(dist, N), (dist*(dist+1)/2)%mod);
}

int main(){
int np; cin>>np;
rep(tp,np){
	int M; 
	cin >> N >> M;
	vector<pair<ll, pair<int, ll> > > event;
	ll total_cost = 0;
	rep(i, M){
		ll a, b, p;	cin >> a >> b >> p;
		event.pb(mp(a, mp(0, p)));
		event.pb(mp(b, mp(1, p)));
		total_cost = add(total_cost,  mul(calc(b - a), p));
	}
	sort(event.begin(), event.end());
	
	ll cost = 0;
	stack<pair<ll,ll> > dq;
	foreach(it, event){
		ll time = it->F; int type = it->S.F; ll p = it->S.S;
		if(type == 1){
			while(p > 0){
				ll amnt = min(p, dq.top().S);
				dq.top().S -= amnt;	
				p -= amnt;
				cost = add(cost, mul(calc(time - dq.top().F), amnt));

				if(dq.top().S == 0)
					dq.pop();
			}
		} else if(type == 0){
			dq.push(mp(time, p));
		}
	}
	assert(dq.empty());
	printf("Case #%d: ", tp+1);
	cout << sub(total_cost, cost) << endl;
}
	
}	
