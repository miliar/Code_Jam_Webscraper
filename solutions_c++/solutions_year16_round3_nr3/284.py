#include <cassert>// c
#include <iostream>// io
#include <iomanip>
#include <fstream>
#include <sstream>
#include <vector>// container
#include <map>
#include <set>
#include <queue>
#include <bitset>
#include <stack>
#include <algorithm>// other
#include <complex>
#include <numeric>
#include <functional>
#include <random>
#include <regex>
using namespace std;

typedef long long ll;
typedef unsigned long long ull;

#define ALL(c) c.begin(),c.end()
#define REP(i,n) FOR(i,0,n)
#define REPr(i,n) FORr(i,0,n)
#define FOR(i,l,r) for(int i=(int)(l);i<(int)(r);++i)
#define FORr(i,l,r) for(int i=(int)(r)-1;i>=(int)(l);--i)
#define EACH(it,o) for(auto it = (o).begin(); it != (o).end(); ++it)
#define IN(l,v,r) ((l)<=(v) && (v)<(r))
#define UNIQUE(v) v.erase(unique(ALL(v)),v.end())
//debug
#define DUMP(x)  cerr << #x << " = " << (x)
#define LINE()    cerr<< " (L" << __LINE__ << ")"

class range {
private:
	struct Iter{
		int v;
		int operator*(){return v;}
		bool operator!=(Iter& itr) {return v < itr.v;}
		void operator++() {++v;}
	};
	Iter i, n;
public:
	range(int n) : i({0}), n({n}) {}
	range(int i, int n) : i({i}), n({n}) {}
	Iter& begin() {return i;}
	Iter& end() {return n;}
};
struct rrange{
	struct Iter{
		int v,step;
		Iter& operator++(){v-=step;return *this;}
		bool operator!=(Iter& itr){return v>itr.v;}
		int& operator*(){return v;}
	};
	Iter i, n;
	rrange(int i, int n,int step):i({i-1,step}), n({n-1,step}){}
	rrange(int i, int n):rrange(i,n,1){}
	rrange(int n) :rrange(0,n){}
	Iter& begin(){return n;}
	Iter& end(){return i;}
};
//input
template<typename T1,typename T2> istream& operator >> (istream& is,pair<T1,T2>& p){return is>>p.first>>p.second;}
template<typename T1> istream& operator >> (istream& is,tuple<T1>& t){return is >> get<0>(t);}
template<typename T1,typename T2> istream& operator >> (istream& is,tuple<T1,T2>& t){return is >> get<0>(t) >> get<1>(t);}
template<typename T1,typename T2,typename T3> istream& operator >> (istream& is,tuple<T1,T2,T3>& t){return is >>get<0>(t)>>get<1>(t)>>get<2>(t);}
template<typename T1,typename T2,typename T3,typename T4> istream& operator >> (istream& is,tuple<T1,T2,T3,T4>& t){return is >> get<0>(t)>>get<1>(t)>>get<2>(t)>>get<3>(t);}
template<typename T1,typename T2,typename T3,typename T4,typename T5> istream& operator >> (istream& is, const tuple<T1,T2,T3,T4,T5>& t){return is >> get<0>(t) >> get<1>(t) >> get<2>(t) >> get<3>(t) >> get<4>(t);}
template<typename T1,typename T2,typename T3,typename T4,typename T5,typename T6> istream& operator >> (istream& is, const tuple<T1,T2,T3,T4,T5,T6>& t){return is >> get<0>(t) >> get<1>(t) >> get<2>(t) >> get<3>(t) >> get<4>(t) >> get<5>(t);}
template<typename T1,typename T2,typename T3,typename T4,typename T5,typename T6,typename T7> istream& operator >> (istream& is, const tuple<T1,T2,T3,T4,T5,T6,T7>& t){return is >> get<0>(t) >> get<1>(t) >> get<2>(t) >> get<3>(t) >> get<4>(t) >> get<5>(t) >> get<6>(t);}
template<typename T> istream& operator >> (istream& is,vector<T>& as){for(int i:range(as.size()))is >>as[i];return is;}

//output
template<typename T> ostream& operator << (ostream& os, const set<T>& ss){for(auto a:ss){if(a!=ss.begin())os<<" "; os<<a;}return os;}
template<typename T1,typename T2> ostream& operator << (ostream& os, const pair<T1,T2>& p){return os<<p.first<<" "<<p.second;}
template<typename K,typename V> ostream& operator << (ostream& os, const map<K,V>& m){bool isF=true;for(auto& p:m){if(!isF)os<<endl;os<<p;isF=false;}return os;}
template<typename T1> ostream& operator << (ostream& os, const tuple<T1>& t){return os << get<0>(t);}
template<typename T1,typename T2> ostream& operator << (ostream& os, const tuple<T1,T2>& t){return os << get<0>(t)<<" "<<get<1>(t);}
template<typename T1,typename T2,typename T3> ostream& operator << (ostream& os, const tuple<T1,T2,T3>& t){return os << get<0>(t)<<" "<<get<1>(t)<<" "<<get<2>(t);}
template<typename T1,typename T2,typename T3,typename T4> ostream& operator << (ostream& os, const tuple<T1,T2,T3,T4>& t){return os << get<0>(t)<<" "<<get<1>(t)<<" "<<get<2>(t)<<" "<<get<3>(t);}
template<typename T1,typename T2,typename T3,typename T4,typename T5> ostream& operator << (ostream& os, const tuple<T1,T2,T3,T4,T5>& t){return os << get<0>(t)<<" "<<get<1>(t)<<" "<<get<2>(t)<<" "<<get<3>(t)<<" "<<get<4>(t);}
template<typename T1,typename T2,typename T3,typename T4,typename T5,typename T6> ostream& operator << (ostream& os, const tuple<T1,T2,T3,T4,T5,T6>& t){return os << get<0>(t)<<" "<<get<1>(t)<<" "<<get<2>(t)<<" "<<get<3>(t)<<" "<<get<4>(t)<<" "<<get<5>(t);}
template<typename T1,typename T2,typename T3,typename T4,typename T5,typename T6,typename T7> ostream& operator << (ostream& os, const tuple<T1,T2,T3,T4,T5,T6,T7>& t){return os << get<0>(t)<<" "<<get<1>(t)<<" "<<get<2>(t)<<" "<<get<3>(t)<<" "<<get<4>(t)<<" "<<get<5>(t)<<" "<<get<6>(t);}
template<typename T> ostream& operator << (ostream& os, const vector<T>& as){for(int i:range(as.size())){if(i!=0)os<<" "; os<<as[i];}return os;}
template<typename T> ostream& operator << (ostream& os, const vector<vector<T>>& as){for(int i:range(as.size())){if(i!=0)os<<endl; os<<as[i];}return os;}

// values
template<typename T> inline T INF(){assert(false);};
template<> inline int INF<int>(){return 1<<28;};
template<> inline ll INF<ll>(){return 1LL<<58;};
template<> inline double INF<double>(){return 1e16;};
template<> inline long double INF<long double>(){return 1e16;};

template<class T> inline T EPS(){assert(false);};
template<> inline int EPS<int>(){return 1;};
template<> inline ll EPS<ll>(){return 1LL;};
template<> inline double EPS<double>(){return 1e-8;};
template<> inline long double EPS<long double>(){return 1e-8;};

// min{2^r | n < 2^r}
template<typename T> T upper_pow2(T n){
	T res=1;while(res<n)res<<=1;return res;
}
// max{d | 2^d  <= n}
template<typename T> T msb(T n){
	int d=30;while((1<<d)>n)d--;return d;
}

template<typename T,typename U> T pmod(T v,U M){return (v%M+M)%M;}

class Main{
	public:

	int J,P,S,K;
	int MV = 0;
	vector<vector<int>> jp,ps,sj;

	int dfs(int j,int p,int s){
		if(s == S) return 0;
		int Mv = 0;
		if(jp[j][p] < K and ps[p][s] < K and sj[s][j] < K){
			jp[j][p]++;ps[p][s]++;sj[s][j]++;
			if(j+1<J)Mv= max(Mv,1+dfs(j+1,p,s));
			else if(p+1<P) Mv = max(Mv,1+dfs(0,p+1,s));
			else Mv = max(Mv,1+dfs(0,0,s+1));
			jp[j][p]--;ps[p][s]--;sj[s][j]--;
		}
		if(j+1<J)Mv= max(Mv,dfs(j+1,p,s));
		else if(p+1<P) Mv = max(Mv,dfs(0,p+1,s));
		else Mv = max(Mv,dfs(0,0,s+1));
		return Mv;
	}
	bool found = false;
	vector<tuple<int,int,int>> res;
	void dfs2(int j,int p,int s,int c){
		if(c == MV){
			found = true;
			return;
		}
		if(s == S) return;
		if(jp[j][p] < K and ps[p][s] <K and sj[s][j] < K){
			jp[j][p]++;ps[p][s]++;sj[s][j]++;
			res.push_back(make_tuple(j+1,p+1,s+1));
			if(j+1<J) dfs2(j+1,p,s,c+1);
			else if(p+1<P) dfs2(0,p+1,s,c+1);
			else dfs2(0,0,s+1,c+1);
			if(found) return;
			jp[j][p]--;ps[p][s]--;sj[s][j]--;
			res.pop_back();
		}
		if(j+1<J)dfs2(j+1,p,s,c);
		else if(p+1<P) dfs2(0,p+1,s,c);
		else dfs2(0,0,s+1,c);
	}
	void run(){
		int T;cin >> T;
		for(int q:range(T)){
			cin >> J >> P >> S >> K;
			jp = vector<vector<int>>(J,vector<int>(P));
			ps = vector<vector<int>>(P,vector<int>(S));
			sj = vector<vector<int>>(S,vector<int>(J));
			MV = dfs(0,0,0);
			found = false;res.clear();
			dfs2(0,0,0,0);
			assert(found);
			// // J*P <= P*P < S!
			// for(int j:range(J)){
			// 	int s = 0;
			// 	for(int p:range(P)){
			// 		for(int k:range(K))if(s < S){
			// 			res.push_back(make_tuple(j+1,p+1,s+1));
			// 			s++;
			// 		}
			// 	}
			// 	// K 個
			// 	for(int s:range(S)){
			// 	}
			// 	if(jp.count({j,p}) || ps.count({p,s}) || sj.count({s,j})) continue;
			// 	jp.insert({j,p});ps.insert({p,s});sj.insert({s,j});
			// 	res.push_back(make_tuple(j+1,p+1,s+1));
			// }
			// int d = min<int>(all,res.size()+K);
			// for(int j:range(J))for(int p:range(P))for(int s:range(S)){
			// 	if(d != res.size()){
			// 		bool uni = true;
			// 		for(tuple<int,int,int> t:res) uni&= t != make_tuple(j+1,p+1,s+1);
			// 		if(uni) res.push_back(make_tuple(j+1,p+1,s+1));
			// 	}
			// }
			cout << make_tuple("Case","#"+to_string(q+1)+":",MV)<<endl;
			for(auto t:res){
				cout << t << endl;
			}
		}
	}
};

int main(){
	cout <<fixed<<setprecision(20);
	cin.tie(0);
	ios::sync_with_stdio(false);
	Main().run();
	return 0;
}
