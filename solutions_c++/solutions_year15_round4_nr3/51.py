#include<iostream>
#include<algorithm>
#include<vector>
#include<queue>
#include<map>
#include<set>
#include<string>
#include<stack>
#include<cstdio>
#include<cmath>
using namespace std;

typedef long long ll;
typedef long double ld;
typedef pair<int,int> P;
typedef pair<int,P> P1;

#define fr first
#define sc second
#define mp make_pair
#define pb push_back
#define rep(i,x) for(int i=0;i<x;i++)
#define rep1(i,x) for(int i=1;i<=x;i++)
#define rrep(i,x) for(int i=x-1;i>=0;i--)
#define rrep1(i,x) for(int i=x;i>0;i--)
#define sor(v) sort(v.begin(),v.end())
#define rev(s) reverse(s.begin(),s.end())
#define lb(vec,a) lower_bound(vec.begin(),vec.end(),a)
#define ub(vec,a) upper_bound(vec.begin(),vec.end(),a)
#define uniq(vec) vec.erase(unique(vec.begin(),vec.end()),vec.end())
#define mp1(a,b,c) P1(a,P(b,c))

const int INF=1000000000;
const int dir_4[4][2]={{1,0},{0,1},{-1,0},{0,-1}};
const int dir_8[8][2]={{1,0},{1,1},{0,1},{-1,1},{-1,0},{-1,-1},{0,-1},{1,-1}};

struct edge{
	int to;
	int cap;
	int rev;
};

edge mke(int t,int c,int r){
	edge ed;
	ed.to = t;
	ed.cap = c;
	ed.rev = r;
	return ed;
}

vector<edge> G[8010];
bool used[8010];

void init(){
	rep(i,8010){
		G[i].clear();
	}
}

void add_edge(int from,int to,int cap){
	//printf("%d %d %d\n",from,to,cap);
	G[from].pb(mke(to,cap,G[to].size()));
	G[to].pb(mke(from,0,G[from].size()-1));
}

int dfs(int v,int t,int f){
	if(v == t)return f;
	used[v] = true;
	rep(i,G[v].size()){
		edge &e = G[v][i];
		if(!used[e.to] && e.cap > 0){
			int d = dfs(e.to,t,min(f,e.cap));
			if(d > 0){
				e.cap -= d;
				G[e.to][e.rev].cap += d;
				return d;
			}
		}
	}
	return 0;
}

int max_flow(int s,int t){
	int flow = 0;
	for(;;){
		memset(used,0,sizeof(used));
		int f = dfs(s,t,INF);
		//puts("");
		if(f == 0)return flow;
		flow += f;
	}
}

struct trie{
	int siz;
	int t;
	int G[40010][30];
	int id[40010];
	void init(){
		siz = 1;
		t = 1;
		rep(i,40010){
			rep(j,30){
				G[i][j] = -1;
			}
			id[i] = -1;
		}
	}
	void add_str(string s){
		int loc = 0;
		rep(i,s.size()){
			if(G[loc][s[i]-'a'] == -1){
				G[loc][s[i]-'a'] = siz;
				siz ++;
			}
			loc = G[loc][s[i]-'a'];
		}
		if(id[loc] == -1){
			id[loc] = t;
			t ++;
		}
	}
	int query(string s){
		int loc = 0;
		rep(i,s.size()){
			loc = G[loc][s[i]-'a'];
		}
		return id[loc];
	}
}trie;

int main(){
	int T;
	cin >> T;
	rep1(ppp,T){
		printf("Case #%d: ",ppp);
		
		int n;
		vector<string> s[202];
		scanf("%d\n",&n);
		rep(i,n){
			string str = "";
			char c = '$';
			while(1){
				scanf("%c",&c);
				if(c == ' '){
					s[i].pb(str);
					str = "";
				}
				else if(c == '\n'){
					s[i].pb(str);
					break;
				}
				else {
					str += c;
				}
			}
		}
		
		init();
		trie.init();
		rep(i,s[0].size()){
			trie.add_str(s[0][i]);
			add_edge(0,2*trie.query(s[0][i])+1,1);
		}
		rep(i,s[1].size()){
			trie.add_str(s[1][i]);
			add_edge(2*trie.query(s[1][i]),1,1);
		}
		for(int i = 2 ; i < n ; i ++){
			int t[12];
			rep(j,s[i].size()){
				trie.add_str(s[i][j]);
				t[j] = trie.query(s[i][j]);
			}
			rep(j,s[i].size()){
				rep(k,s[i].size()){
					if(j == k)continue;
					add_edge(2*t[j],2*t[k]+1,1);
				}
			}
		}
		for(int i = 1; i < trie.t ; i ++){
			add_edge(2*i+1,2*i,1);
		}
		
		printf("%d\n",max_flow(0,1));
		
		/*rep(i,n){
			printf("%d:\n",s[i].size());
			rep(j,s[i].size()){
				cout << s[i][j] << endl;
			}
		}*/
	}
}
			
