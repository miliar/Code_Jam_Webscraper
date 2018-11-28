#include <cstdio>
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
#include <complex>
#include <stack>
#include <queue>
#include <cstring>
#include <assert.h>
#include <sys/time.h>
#include <fstream>
#include <iomanip>

#define FOR(i,a,b) for(int i=(a);i<(b);++i)
#define rep(i,n)  FOR(i,0,n)
#define REP(i,n)  FOR(i,0,n)
#define each(i,c) for(auto i=(c).begin(); i!=(c).end(); ++i)
#define EACH(i,c) for(auto i=(c).begin(); i!=(c).end(); ++i)
#define exist(s,e) ((s).find(e)!=(s).end())

#define dump(x)  cerr << #x << " = " << (x) << endl;
#define debug(x) cerr << #x << " = " << (x) << " (L" << __LINE__ << ")" << " " << __FILE__ << endl;
#define deb(x) cerr << #x << " = " << (x) << " , ";
#define debl cerr << " (L" << __LINE__ << ")"<< endl;
#define sz(s) (int)((s).size())


#define clr(a) memset((a),0,sizeof(a))
#define nclr(a) memset((a),-1,sizeof(a))
#define pb push_back
#define INRANGE(x,s,e) ((s)<=(x) && (x)<(e))
#define MP(x,y) make_pair((x),(y))

double pi=3.14159265358979323846;

using namespace std;
typedef long long ll;
typedef pair<int,int> pii;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef vector<ll> vl;
typedef vector<vl> vvl;
typedef vector<double> vd;
typedef vector<vd> vvd;
typedef vector<string> vs;

template<typename T> std::ostream& operator<<(std::ostream& os, const vector<T>& z){
	os << "[ ";
	REP(i,z.size())os << z[i] << ", " ;
	return ( os << "]" << endl);
}

template<typename T> std::ostream& operator<<(std::ostream& os, const set<T>& z){
	os << "set( ";
	EACH(p,z)os << (*p) << ", " ;
	return ( os << ")" << endl);
}

template<typename T,typename U> std::ostream& operator<<(std::ostream& os, const map<T,U>& z){
	os << "{ ";
	EACH(p,z)os << (p->first) << ": " << (p->second) << ", " ;
	return ( os << "}" << endl);
}

template<typename T,typename U> std::ostream& operator<<(std::ostream& os, const pair<T,U>& z){
	return ( os << "(" << z.first << ", " << z.second << ",)" );
}

double get_time(){
	struct timeval tv;
	gettimeofday(&tv, NULL);
	return tv.tv_sec + tv.tv_usec*1e-6;
}

typedef unsigned int uint32_t;
struct RND{
	uint32_t x;
	uint32_t y;
	uint32_t z;
	uint32_t w;
	RND(){
		x=123456789;
		y=362436069;
		z=521288629;
		w=88675123;
	}
	void init(int seed){
		x=123456789;
		y=362436069;
		z=521288629;
		w=seed+100;
		REP(i,10)get();
	}
	uint32_t get(){
		uint32_t t;
		t=x^(x<<11);
		x=y;y=z;z=w;
		w=(w^(w>>19))^(t^(t>>8));
		return w;
	}
};
RND rnd;

ll double_to_ll(double d){
	if(d>0)return d+0.5;
	return d-0.5;
}

vl a;
ll N;
ll cal1(){
	vl ri(N), le(N);
	rep(i,N) rep(j,N) if(a[j]>a[i]){
		if(j<i)le[i]++;
		if(j>i)ri[i]++;
	}
	ll val = 0;
	rep(i,N) val += ri[i];
	ll ans = val;
	rep(i,N){
		val += le[i] - ri[i];
		ans = min(ans, val);
	}
	return ans;
}

ll cal2(){
	ll best = 1e16;
	rep(b, 1<<N){
		vl le,ri;
		rep(j,N) {
			if((b>>j)%2==0){
				le.push_back(a[j]);
			}
			else{
				ri.push_back(a[j]);
			}
		}
		ll ans = 0;
		ll a1=0,a2=0,a3=0;
		rep(i2,le.size()) rep(i1,i2){
			if(le[i1]>le[i2])a1++;
		}
		rep(i2,ri.size()) rep(i1,i2){
			if(ri[i1]<ri[i2])a2++;
		}
		rep(i2,a.size()) rep(i1,i2){
			if((b>>i1)%2==1 && (b>>i2)%2==0)a3++;
		}
		ans = a1+a2+a3;
		if(b==24){
			//deb(a1);deb(a2);deb(a3);debl;
		}
		best = min(ans, best);
	}
	return best;
}

void _main(istream &inp){
	ll T;
	inp >> T;
	rep(tt,T){
		inp >> N;
		a.resize(N);
		rep(j,N) inp >> a[j];
		deb(cal1());deb(cal2());debl;
		ll ans = cal2();
		cout << "Case #" << tt+1 << ": " << ans << endl;
	}

}

int main(){
	if(0){
		ifstream ifs("test.txt");
		_main(ifs);
	}
	else{
		_main(cin);
	}
	return 0;
}
