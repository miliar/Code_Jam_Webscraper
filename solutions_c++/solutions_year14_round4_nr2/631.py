#include <bits/stdc++.h>
using namespace std;

#define typeof(...) remove_cv<__typeof(__VA_ARGS__)>::type
#define REP(i,n) for(typeof(n)i=0;i<(n);++i)
#define DBG(...) ;
namespace cheapwine{
	typedef vector<int>VI;
	template<class C>int size(C const &c){return c.size();}
}
using namespace cheapwine;
//END OF TEMPLATE CODE

int N;
VI a;

void solvecase(){
	cin>>N;
	a.resize(N);
	REP(i,N)cin>>a[i];
	int total=0;
	while(!a.empty()){
		auto pos=min_element(a.begin(),a.end());
		int p=pos-a.begin();
		total+=min(p,size(a)-1-p);
		a.erase(pos);
	}
	cout<<total;
}

void gcj_main(){
	int T;
	cin >> T;
	for (int i = 1; i <= T; ++i) {
		DBG(i);
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
