#include <bits/stdc++.h>
using namespace std;

#define typeof(...) remove_cv<__typeof(__VA_ARGS__)>::type
#define REP(i,n) for(typeof(n)i=0;i<(n);++i)
#define DBG(...) ;
namespace cheapwine{
	typedef vector<int>VI;
}
using namespace cheapwine;
//END OF TEMPLATE CODE


void solvecase(){
	int N,T;
	cin>>N>>T;
	//DBG(N,T);
	VI a(N);
	REP(i,N)cin>>a[i];
	map<int,int> m;
	REP(i,N)m[a[i]]++;
	int cnt=0;
	while(!m.empty()){
		//DBG(m);
		auto v=m.rbegin();
		auto val=v->first;
		if(--(v->second)==0){
			m.erase(v->first);
		}
		++cnt;
		if(m.empty())break;
		auto p=m.lower_bound(T-val+1);
		if(p==m.end())p=m.begin();
		if(p!=m.begin())--p;
		if(p->first+val<=T){
			if(--(p->second)==0){
				m.erase(p);
			}
		}
	}
	cout<<cnt;
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
