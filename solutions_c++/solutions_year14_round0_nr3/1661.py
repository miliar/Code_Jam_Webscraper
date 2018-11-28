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

int visit[5][5];

pii check(vvi field){
	int h = field.size();
	int w = field[0].size();
	rep(sx,h) rep(sy,w) if(field[sx][sy]==0){
		queue<pii> Q;
		Q.emplace(sx, sy);
		clr(visit);
		while(!Q.empty()){
			int x = Q.front().first;
			int y = Q.front().second;
			assert(field[x][y]==0);
			Q.pop();
			if(visit[x][y])continue;
			visit[x][y]=1;
			int cnt = 0;
			FOR(dx,-1,2) FOR(dy,-1,2){
				int nx = x+dx, ny=y+dy;
				if(0<=nx && nx<h && 0<=ny && ny<w && field[nx][ny]==1)cnt++;
			}
			if(cnt==0)	FOR(dx,-1,2) FOR(dy,-1,2){
				int nx = x+dx, ny=y+dy;
				if(0<=nx && nx<h && 0<=ny && ny<w && field[nx][ny]==0){
					Q.emplace(nx, ny);
				}
			}
		}
		bool ok = true;
		rep(x,h)rep(y,w) if(field[x][y]==0 && visit[x][y]==0)ok=false;
		if(ok)return pii(sx,sy);
	}
	return pii(-1,-1);
}

vector<string> pre_comp[10][10][30];

void solve(int R, int C){
	vector<vvi> answer(R*C);
	vector<pii> answer_c(R*C, pii(-1,-1));
	rep(b,1<<(R*C)){
		int M = __builtin_popcount(b);
		if(M==R*C)continue;
		if(answer[M].size()!=0)continue;
		vvi field(R, vi(C));
		rep(x,R) rep(y,C){
			field[x][y] = (b>>(x*C+y))%2;
		}
		pii p = check(field);
		if(p.first!=-1){
			answer[M] = field;
			answer_c[M] = p;
		}
	}

	rep(M,R*C){
		pii p = answer_c[M];
		vector<string> ret;
		if(p.first!=-1){
			vector<string> res(R, string(C, '.'));
			rep(x,R) rep(y,C) if(answer[M][x][y]) res[x][y] = '*';
			res[p.first][p.second] = 'c';
			ret = res;
		}
		else{
			ret.pb("Impossible");
		}
		pre_comp[R][C][M] =ret;
		//deb(M);deb(ret);debl;

	}
}

void _main(istream &inp){
	FOR(R,1,6) FOR(C,1,6) solve(R,C);
	int T;
	inp >> T;
	rep(tt,T){
		int R,C,M;
		inp >> R >> C >> M;
		cout << "Case #" << tt+1 << ":" << endl;
		for(string s:pre_comp[R][C][M]){
			cout << s << endl;
		}
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
