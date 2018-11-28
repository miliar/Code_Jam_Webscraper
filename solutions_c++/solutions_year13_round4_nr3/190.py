#include <iostream>
#include <cstring>
#include <vector>
#include <cassert>
#include <algorithm>
using namespace std;
int N;
const int MN = 2048;
int A[MN], B[MN];
int pprev[MN];
vector<int> es[MN];
bool done[MN];
int res[MN];
void setLess(int a, int b) {
	es[b].push_back(a);
//	cout<<a<<" < "<<b<<'\n';
}
void pp(bool b) {
	memset(pprev,-1,sizeof(pprev));
	for(int i=0; i<N; ++i) {
		int id = b ? N-1-i : i;
		int x = b ? B[id] : A[id];
		int p = pprev[x];
		int p2 = pprev[x-1];
		if (p>=0) setLess(id, p);
		if (p2>=0) setLess(p2, id);
		pprev[x] = id;
	}
}
vector<int> act;
bool lol[MN];
void dfs(int n) {
	lol[n]=1;
	bool fail=0;
	for(int i: es[n]) {
//		if (!fail && !done[i]) cout<<"fail "<<n<<' '<<i<<'\n';
		fail |= !done[i];
		if (!done[i] && !lol[i]) dfs(i);
	}
	if (!fail) act.push_back(n);
}
int main() {
	int t;cin>>t;
	for(int a=1; a<=t; ++a) {
		cin>>N;
		for(int i=0; i<N; ++i) cin>>A[i];
		for(int i=0; i<N; ++i) cin>>B[i];
		for(int i=0; i<N; ++i) es[i].clear();
		pp(0);
		pp(1);
		memset(done,0,sizeof(done));
		for(int i=0; i<N; ++i) {
			memset(lol,0,sizeof(lol));
			act.clear();
			for(int i=0; i<N; ++i) if (!done[i] && !lol[i]) dfs(i);
			assert(!act.empty());
			int x = *min_element(act.begin(), act.end());
//			cout<<"lol "<<i<<' '<<act.size()<<' '<<x<<'\n';
			res[x] = 1+i;
			done[x] = 1;
		}
		cout<<"Case #"<<a<<":";
		for(int i=0; i<N; ++i) cout<<' '<<res[i];
		cout<<'\n';
	}
}
