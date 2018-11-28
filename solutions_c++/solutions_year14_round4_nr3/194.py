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

typedef pair<ll,ll> pll;
ll W,H,N;
ll x0s[1010], y0s[1010], x1s[1010], y1s[1010];

ll dist[1010];
ll visit[1010];

ll getd(ll x0a, ll x1a, ll x0b, ll x1b){
	if(x0b-x1a>0){
		return x0b - x1a-1;
	}
	if(x0a>x1b){
		return x0a-x1b-1;
	}
	return 0;
}

void _main(istream &inp){
	ll T;
	inp >> T;
	rep(tt,T){
		inp >> W >> H >> N;
		x0s[0]=-1;
		x1s[0]=-1;
		y0s[0]=0;
		y1s[0]=H-1;

		x0s[1]=W;
		x1s[1]=W;
		y0s[1]=0;
		y1s[1]=H-1;


		rep(j,N){
			inp >> x0s[j+2] >> y0s[j+2] >> x1s[j+2] >> y1s[j+2];
		}
		priority_queue<pll, vector<pll>, greater<pll> > Q;
		Q.emplace(0, 0);
		clr(visit);
		while(!Q.empty()){
			ll d = Q.top().first;
			ll id = Q.top().second;
			Q.pop();
			if(visit[id])continue;
			visit[id]=1;
			dist[id] = d;
			rep(id2,N+2){
				ll nd = d + max(getd(x0s[id], x1s[id], x0s[id2], x1s[id2]),  getd(y0s[id], y1s[id], y0s[id2], y1s[id2]) );
				Q.emplace(nd, id2);
			}
		}
		ll ans = dist[1];
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
