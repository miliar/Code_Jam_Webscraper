#include <bits/stdc++.h>
using namespace std;

#define typeof(...) remove_cv<__typeof(__VA_ARGS__)>::type
#define PB(...) push_back(__VA_ARGS__)
#define REP(i,n) for(typeof(n)i=0;i<(n);++i)
#define REPC(i,c) for(int i=0;i<(int)(c).size();++i)
namespace cheapwine{
	typedef vector<int>VI;
	typedef vector<VI>VVI;
	typedef vector<string>VS;
	template<class C>int size(C const &c){return c.size();}
}
using namespace cheapwine;
//END OF TEMPLATE CODE



int M,N;
VS s;
VI a;


int maxc;
int ways;

int count(VI& v){
	set<string> x;
	REPC(i,v){
		string& str=s[v[i]];
		for(int i=1;i<=size(str);++i){
			x.insert(str.substr(0,i));
		}
	}
	return size(x)+1;
}

void dfs(int p){
	if(p==M){
		VVI r(N);
		REPC(i,a){
			r[a[i]].PB(i);
		}

		REPC(i,r)if(size(r[i])==0)return;

		int cnt=0;
		REPC(i,r){
			cnt+=count(r[i]);
		}

		if(cnt>maxc){
			maxc=cnt;
			ways=1;
		}else
		if(cnt==maxc){
			++ways;
		}

		return;
	}
	REP(i,N){
		a[p]=i;
		dfs(p+1);
	}
}

void solvecase(){
	cin>>M>>N;
	s.resize(M);
	a.resize(M);
	REP(i,M)cin>>s[i];
	maxc=0;
	ways=0;
	dfs(0);

	cout<<maxc<<' '<<ways;
}

void gcj_main(){
	int T;
	cin >> T;
	for (int i = 1; i <= T; ++i) {
		printf("Case #%d: ", i);
		solvecase();
		printf("\n");
	}
	exit(0);
}

int main() {
	//try some IO related performance boost
	//comment the next line iff iostreams(cin/cout/cerr) are mixed with stdio(stdin/stdout/stderr)
	//ios_base::sync_with_stdio(0);
	//comment the next line iff interactive console is required
	cin.tie(0);

	//for embeded debug
	//freopen("1.in","r",stdin);

	//google code jam starts here
	gcj_main();

	return 0;
}
