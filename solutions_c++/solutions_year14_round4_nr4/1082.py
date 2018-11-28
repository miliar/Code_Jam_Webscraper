#include <bits/stdc++.h>
using namespace std;
#define TR(i,v) 		for(__typeof((v).begin())i=(v).begin();i!=(v).end();++i)
#define DEBUG(x) 		cout << #x << " = "; cout << x << endl;
#define SIZE(p) 		(int)(p).size()
#define MP(a, b)		make_pair((a), (b))
#define ALL(p)			(p).begin(), (p).end()
#define rep(i, n)		for(int (i)=0; (i)<(int)(n); ++(i))
#define REP(i, a, n)	for(int (i)=(a); (i)<(int)(n); ++(i))
#define FOR(i, a, b)   	for(int (i)=(int)(a); (i)<=(int)(b); ++(i))
#define FORD(i, b, a)  	for(int (i)=(int)(b); (i)>=(int)(a); --(i)) 
typedef long long LL;
typedef pair<int, int> pii;
int N,M;
int B[100];
vector<string> S;
map<int,LL> C;
bool use[100];
int gao(vector<string> &s) {
	set<string> d;
	for(auto &w : s) {
		rep(i, SIZE(w))
			d.insert(w.substr(0, i+1));
	}
	// puts("///");
	// for(auto &w : d) {
	// 	DEBUG(w);
	// }
	return SIZE(d);
}
int get() {
	int r = 0;
	rep(i, N) {
		vector<string> c;
		int mask=B[i];
		rep(j,M) if(mask>>j&1)	c.push_back(S[j]);
		r += gao(c);
	}		
	return r;
}
void dfs1(int cur) {
	if(cur==N) {
		int s = 0;
		int s1=0;
		rep(i, N)	s |= B[i], s1+=B[i];
		// rep(i,N)	printf("%d ", B[i]);	puts("");	DEBUG(s);
		assert(s == ((1<<M)-1));
		assert(s1==s);
		int r=get()+N;
		// DEBUG(r);
		++C[r];
		return;
	}	
	int mask=0;
	rep(i,M) if(!use[i])	mask |= 1<<i;
	if(cur+1==N) {
		// DEBUG(mask);
		B[cur] = mask;
		rep(j,M) if(mask>>j&1)	use[j]=1;
		dfs1(cur+1);
		rep(j,M) if(mask>>j&1)	use[j]=0;
		return;
	}
	for(int i=(mask-1)&mask; i; i=(i-1)&mask) {
		B[cur]=i;
		rep(j,M) if(i>>j&1)	use[j]=1;
		dfs1(cur+1);
		rep(j,M) if(i>>j&1)	use[j]=0;
	}	
}
vector<string> D[100];
void dfs(int cur) {
	if(cur==M) {
		rep(i,N) if(D[i].empty())	return;
		int r=0;
		// rep(i,N) {
		// 	DEBUG(i);
		// 	for(auto &w : D[i])	{
		// 		DEBUG(w);
		// 	}
		// 	puts("");
		// }
		rep(i,N)	r+=gao(D[i]);
		r+=N;
		++C[r];
		return;
	}
	rep(i,N) {
		D[i].push_back(S[cur]);
		dfs(cur+1);
		D[i].pop_back();
	}
}
int main(int argc, char const *argv[])
{
	#ifndef ONLINE_JUDGE
    freopen("D.in", "r", stdin);	
    freopen("D.out", "w", stdout);
    #endif
	// ios::sync_with_stdio(false);    cin.tie(0);
	int T;	cin>>T;
	FOR(cs,1,T) {
		printf("Case #%d: ", cs);
		int m, n;	cin>>m>>n;	M=m;
		N=n;
		S.clear();
		rep(i,m) {
			string w;	cin>>w;	S.push_back(w);
		}
		C.clear();
		rep(i,m)	use[i]=0;
		rep(i,N)	D[i].clear();
		dfs(0);
		auto it = C.end();	--it;
		printf("%d %I64d\n", it->first, it->second);
	}
	return 0;
}