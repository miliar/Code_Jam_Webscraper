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

#define TWO(x) (1LL<<(x))
bool bit_set(ll seed, ll idx){
	return seed & TWO(idx);
}

vector<bool> target;


ll N,P;
bool check(ll depth, ll better, ll worse, bool clear){
	assert(better >= 0 && worse >= 0);
	assert(better + worse + 1 == TWO(N - depth));

	if(depth == N)
		return true;

	//loose node
	if(clear || (target[depth] == false)){
		if(worse + 1 >= better){
			return true;
		} else{
			ll rem = better - (worse+1);
			assert((rem % 2) == 0);
			if(check(depth+1, rem/2, TWO(N-(depth+1)) - 1 - rem/2, clear))
				return true;
		}
	}

	//win node
	bool n_clear = clear || (target[depth] == false);
	if(better % 2){
		//odd better, even worse
		if(worse >= 2){
			if(check(depth+1, (better-1)/2 + 1, (worse-2)/2, n_clear))
				return true;
		}
	} else{
		//even better
		if(worse >= 1){
			if(check(depth+1, better/2, (worse-1)/2, n_clear))
				return true;
		}
	}

	return false;
}

//is guarenteed to win
bool check2(ll depth, ll better, ll worse){
	assert(better >= 0 && worse >= 0);
	assert(better + worse + 1 == TWO(N - depth));

	if(depth == N)
		return true;

	bool can_loose = better > 0;

	if(can_loose){
		if(target[depth] == true)
			return false;
		else{
			if(better % 2){
				if(!check2(depth+1, (better-1)/2, worse/2))
					return false;
			}
			else{
				if(!check2(depth+1, (better-2)/2, (worse-1)/2 + 1))
					return false;
			}
		}
	}
	
	if(target[depth] == true){
		ll rem = ((better+1) - worse);
		assert((rem % 2) == 0);
		if(rem > 0){
			if(!check2(depth+1, better + rem/2, 0))
				return false;
		} else{
			if(!check2(depth+1, better, (-rem)/2))
				return false;
		}
	}
	
	return true;
}

ll search1(){
	ll a = 0, b = TWO(N);
	while(a+1 != b){
		ll m = (a+b)/2;	
		if(check(0, m, TWO(N)-m-1, false))
			a = m;
		else
			b = m;
	}
	return a;
}

ll search2(){
	ll a = 0, b = TWO(N);
	while(a+1 != b){
		ll m = (a+b)/2;	
		if(check2(0, m, TWO(N)-m-1))
			a = m;
		else
			b = m;
	}
	return a;
}

int main(){
int np; cin>>np;
rep(tp,np){
	cin >> N >> P;
	target = vector<bool>(N);
	rep(i, N)
		target[i] = bit_set(TWO(N) - P, N-i-1);

	ll worst = search1();
	ll best = search2();

	printf("Case #%d: %lld %lld\n", tp+1, best, worst);
	/*
	rep(i, TWO(N)){
		if(check2(0, i, TWO(N) - i - 1)){
			cout << i << " ";
		}
	}
	cout << endl;
	*/

}
	
}	
