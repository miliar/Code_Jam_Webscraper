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

#define ALL(c) (begin(c)),(end(c))
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
template<typename T1,typename T2> istream& operator >> (istream& is,pair<T1,T2>& p){is>>p.first>>p.second;return is;}
template<typename T1> istream& operator >> (istream& is,tuple<T1>& t){is >> get<0>(t);return is;}
template<typename T1,typename T2> istream& operator >> (istream& is,tuple<T1,T2>& t){is >> get<0>(t) >> get<1>(t);return is;}
template<typename T1,typename T2,typename T3> istream& operator >> (istream& is,tuple<T1,T2,T3>& t){is >>get<0>(t)>>get<1>(t)>>get<2>(t);return is;}
template<typename T1,typename T2,typename T3,typename T4> istream& operator >> (istream& is,tuple<T1,T2,T3,T4>& t){is >> get<0>(t)>>get<1>(t)>>get<2>(t)>>get<3>(t);return is;}
template<typename T1,typename T2,typename T3,typename T4,typename T5> istream& operator >> (istream& is, const tuple<T1,T2,T3,T4,T5>& t){is >> get<0>(t) >> get<1>(t) >> get<2>(t) >> get<3>(t) >> get<4>(t);return is;}
template<typename T1,typename T2,typename T3,typename T4,typename T5,typename T6> istream& operator >> (istream& is, const tuple<T1,T2,T3,T4,T5,T6>& t){is >> get<0>(t) >> get<1>(t) >> get<2>(t) >> get<3>(t) >> get<4>(t) >> get<5>(t);return is;}
template<typename T1,typename T2,typename T3,typename T4,typename T5,typename T6,typename T7> istream& operator >> (istream& is, const tuple<T1,T2,T3,T4,T5,T6,T7>& t){is >> get<0>(t) >> get<1>(t) >> get<2>(t) >> get<3>(t) >> get<4>(t) >> get<5>(t) >> get<6>(t);return is;}
template<typename T> istream& operator >> (istream& is,vector<T>& as){REP(i,as.size())is >>as[i];return is;}

//output
template<typename T> ostream& operator << (ostream& os, const set<T>& ss){for(auto a:ss){if(a!=ss.begin())os<<" "; os<<a;}return os;}
template<typename T1,typename T2> ostream& operator << (ostream& os, const pair<T1,T2>& p){os<<p.first<<" "<<p.second;return os;}
template<typename K,typename V> ostream& operator << (ostream& os, const map<K,V>& m){bool isF=true;for(auto& p:m){if(!isF)os<<endl;os<<p;isF=false;}return os;}
template<typename T1> ostream& operator << (ostream& os, const tuple<T1>& t){os << get<0>(t);return os;}
template<typename T1,typename T2> ostream& operator << (ostream& os, const tuple<T1,T2>& t){os << get<0>(t)<<" "<<get<1>(t);return os;}
template<typename T1,typename T2,typename T3> ostream& operator << (ostream& os, const tuple<T1,T2,T3>& t){os << get<0>(t)<<" "<<get<1>(t)<<" "<<get<2>(t);return os;}
template<typename T1,typename T2,typename T3,typename T4> ostream& operator << (ostream& os, const tuple<T1,T2,T3,T4>& t){os << get<0>(t)<<" "<<get<1>(t)<<" "<<get<2>(t)<<" "<<get<3>(t);return os;}
template<typename T1,typename T2,typename T3,typename T4,typename T5> ostream& operator << (ostream& os, const tuple<T1,T2,T3,T4,T5>& t){os << get<0>(t)<<" "<<get<1>(t)<<" "<<get<2>(t)<<" "<<get<3>(t)<<" "<<get<4>(t);return os;}
template<typename T1,typename T2,typename T3,typename T4,typename T5,typename T6> ostream& operator << (ostream& os, const tuple<T1,T2,T3,T4,T5,T6>& t){os << get<0>(t)<<" "<<get<1>(t)<<" "<<get<2>(t)<<" "<<get<3>(t)<<" "<<get<4>(t)<<" "<<get<5>(t);return os;}
template<typename T1,typename T2,typename T3,typename T4,typename T5,typename T6,typename T7> ostream& operator << (ostream& os, const tuple<T1,T2,T3,T4,T5,T6,T7>& t){os << get<0>(t)<<" "<<get<1>(t)<<" "<<get<2>(t)<<" "<<get<3>(t)<<" "<<get<4>(t)<<" "<<get<5>(t)<<" "<<get<6>(t);return os;}
template<typename T> ostream& operator << (ostream& os, const vector<T>& as){REP(i,as.size()){if(i!=0)os<<" "; os<<as[i];}return os;}
template<typename T> ostream& operator << (ostream& os, const vector<vector<T>>& as){REP(i,as.size()){if(i!=0)os<<endl; os<<as[i];}return os;}

// values
template<typename T> T INF(){assert(false);};
template<> int INF<int>(){return 1<<28;};
template<> ll INF<ll>(){return 1LL<<58;};
template<> double INF<double>(){return 1e16;};
template<> long double INF<long double>(){return 1e16;};

template<class T> T EPS(){assert(false);};
template<> int EPS<int>(){return 1;};
template<> ll EPS<ll>(){return 1LL;};
template<> double EPS<double>(){return 1e-8;};
template<> long double EPS<long double>(){return 1e-8;};

template<typename T,typename U> T pmod(T v,U M){return (v%M+M)%M;}

class Main{
	public:
	void run(){
		int T;cin >> T;
		for(int q:range(T)){
			int R,C;cin >> R >> C;
			vector<string> board(R);
			for(int i:range(R))cin >> board[i];

			int c = 0;bool ok=true;
			vector<int> Ls(R,-1);
			vector<int> Rs(R,-1);
			vector<int> Us(C,-1);
			vector<int> Ds(C,-1);
			vector<vector<bool>> change(R,vector<bool>(C));

			for(int y:range(R))for(int x:range(C))if(board[y][x]!='.'){
				Ls[y]=x;
				if(board[y][x]=='<'){
					change[y][x]=true;
					c++;
				}
				break;
			}
			for(int y:range(R))for(int x:rrange(C))if(board[y][x]!='.'){
				Rs[y]=x;
				if(board[y][x]=='>'){
					change[y][x]=true;
					c++;
				}
				break;
			}
			for(int x:range(C))for(int y:range(R))if(board[y][x]!='.'){
				Us[x]=y;
				if(board[y][x]=='^'){
					change[y][x]=true;
					c++;
				}
				break;
			}
			for(int x:range(C))for(int y:rrange(R))if(board[y][x]!='.'){
				Ds[x]=y;
				if(board[y][x]=='v'){
					change[y][x]=true;
					c++;
				}
				break;

			}
			for(int y:range(R))for(int x:range(C))if(change[y][x]){
				if(Ls[y]==x && Rs[y]==x && Us[x]==y && Ds[x]==y)ok=false;
			}
			if(ok){
				cout << make_tuple("Case","#"+to_string(q+1)+":",c)<<endl;
			}else{
				cout << make_tuple("Case","#"+to_string(q+1)+":","IMPOSSIBLE")<<endl;
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