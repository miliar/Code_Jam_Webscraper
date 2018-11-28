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

class MaximamFlow{
private:
    typedef int Flow;
    struct Edge{int to;Flow icap,cap;};
    typedef vector<vector<Edge>> Graph;

    //iter　次に調べる時の開始位置 距離
    vector<int> iter,dist;

    //sからのbfs距離
    void bfs_dist(int s){
        fill(ALL(dist),-1); dist[s]=0;
        queue<int> que; que.push(s);
        while(!que.empty()){
            int v=que.front();que.pop();
            for(Edge& e:G[v])if(e.cap > 0 && dist[e.to] == -1){
                dist[e.to]=dist[v]+1;
                que.push(e.to);
            }
        }
    }
    // s->t 増加パス
    Flow dfs_best_path(int s,int t,Flow f){
        if(s==t)return f;
        for(int &i = iter[s];i < (int)G[s].size();i++){
            Edge &e=G[s][i];Edge &reve = G[e.to][eid[e.to][s]];
            if(e.cap <= 0 || dist[s]>=dist[e.to])continue;
            //search
            Flow d = dfs_best_path(e.to,t,min(f,e.cap));
            if(d==0)continue;
            //found
            e.cap-=d;reve.cap+=d;
            return d;
        }
        return 0;
    }
public:
    int V;Graph G;
    vector<vector<int>> eid;
    MaximamFlow(int V):V(V){
        G=Graph(V);
        eid=vector<vector<int>>(V,vector<int>(V,-1));
        dist=vector<int>(V,-1);iter=vector<int>(V);
    }

    void add_edge(int s,int t,Flow cap){
        if(eid[s][t]<0){eid[s][t]=G[s].size();G[s].push_back({t,0,0});}
        if(eid[t][s]<0){eid[t][s]=G[t].size();G[t].push_back({s,0,0});}
        G[s][eid[s][t]].icap=cap;
        G[s][eid[s][t]].cap=cap;
    }

    Flow change_cost(int S,int T,int s,int t,int c){
        if(eid[s][t]<0)add_edge(s,t,c);

        Edge& e =G[s][eid[s][t]];Edge& reve = G[t][eid[t][s]];
        Flow flow = 0;
        if(e.icap <= c){// 単純に増やす
            e.cap += c - e.icap;
            e.icap = c;
        }else if(c >= e.icap-e.cap){ // 単純に減らす
            e.cap -= e.icap - c;
            e.icap = c;
        }else{// フローを戻してから減らす
            Flow d = e.icap - e.cap - c;
            e.cap = 0;reve.cap = 0;
            //(1) S <- s <- t <- T のフローを戻す
            Flow fs = max_flow(s,S,d),ft = max_flow(T,t,d),f = min(fs,ft);
            max_flow(S,s,fs-f); max_flow(t,T,ft-f);
            flow -= f;
            //(2) (1)で戻せない分は t <- s <- t 内で無駄な t <- s 路ができているので除去する
            max_flow(s,t,d-f);
            e.cap = 0;reve.cap = c + reve.icap;
            e.icap = c;
        }
        flow+=max_flow(S,T);//
        return flow;
    }

    int max_flow(int s,int t,Flow Mf=INF<Flow>()){
        if(s==t)return Mf;
        Flow flow=0;
        while(Mf>0){
            bfs_dist(s);
            if(dist[t] == -1)break;
            Flow f;
            fill(ALL(iter),0);
            while((f=dfs_best_path(s,t,Mf))>0)flow+=f,Mf-=f;
        }
        return flow;
    }
};

class Main{
	public:
	void run(){

		int T;cin >> T;
		for(int q:range(T)){
			int n;cin >> n;
			vector<string> board(n); cin >> board;

			int mv = n*n;
			for(int bit:range(1 << (n*n))){
				bool ok = true;
				for(int i:range(n))for(int j:range(n))if(board[i][j] == '1'){
					if(!(bit&(1<<(i*n+j)))) ok = false;
				}
				if(!ok) continue;
				for(int k:range(n)){
					int c = 0;
					MaximamFlow mf(2*n +2);int S = 2*n, T = S+1;
					for(int i:range(n)) mf.add_edge(S,i,1);
					for(int j:range(n))if((bit&(1<<(k*n+j)))) mf.add_edge(n+j,T,1),c++;
					for(int i:range(n))for(int j:range(n))if((bit&(1<<(i*n+j))))if(k!=i){
						mf.add_edge(i,n+j,1);
					}

					ok&= mf.max_flow(S,T) < c || c == n;
				}
				{
					MaximamFlow mf(2*n +2);int S = 2*n, T = S+1;
					for(int i:range(n)) mf.add_edge(S,i,1);
					for(int j:range(n)) mf.add_edge(n+j,T,1);
					for(int i:range(n))for(int j:range(n))if((bit&(1<<(i*n+j)))){
						mf.add_edge(i,n+j,1);
					}
					ok&= mf.max_flow(S,T) == n;
				}
				if(ok)mv = min(mv,__builtin_popcount(bit));
			}
			int ini = 0;
			for(int i:range(n))for(int j:range(n))if(board[i][j] == '1')ini++;
			cout << make_tuple("Case","#"+to_string(q+1)+":",mv-ini)<<endl;

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
