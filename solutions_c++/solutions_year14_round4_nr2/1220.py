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
inline bool check(vector<int> &p) {
	vector<int> L(SIZE(p),0);
	vector<int> R(SIZE(p),0);
	int n=SIZE(p);
	L[0]=1;
	REP(i,1,n)	L[i]=L[i-1]&&(p[i]>p[i-1]);
	R[n-1]=1;
	FORD(i,n-2,0)	R[i]=R[i+1]&&(p[i]>p[i+1]);
	// rep(i,n)	printf("%d ", L[i]);	puts("");
	// rep(i,n)	printf("%d ", R[i]);	puts("");
	rep(i,n) if(L[i]&&R[i])
		return 1;	
	return 0;
}
int gao(vector<int> &a, vector<int> &b) {
	int n=SIZE(a);
	vector<int> pos(SIZE(a));
	rep(i,SIZE(b))	pos[b[i]]=i;
	vector<int> p(n);
	rep(i,SIZE(a))	p[i]=pos[a[i]];
	int r = 0;
	rep(i,n)
	REP(j,i+1,n)	r+=p[i]>p[j];
	return r;
}
int main(int argc, char const *argv[])
{
	#ifndef ONLINE_JUDGE
    freopen("B.in", "r", stdin);	
    freopen("B.out", "w", stdout);
    #endif
	// ios::sync_with_stdio(false);    cin.tie(0);
	int T;	cin>>T;
	FOR(cs,1,T) {
		printf("Case #%d: ", cs);
		int n;	cin>>n;
		vector<int> p(n);
		rep(i,n)	cin>>p[i];
		vector<int> q=p;		
		sort(ALL(q));	auto uf=unique(ALL(q));	q.erase(uf,q.end());
		// rep(i,SIZE(p))	printf("%d ", q[i]);	puts("");
		rep(i,n) {			
			p[i]=(int)(lower_bound(ALL(q),p[i])-q.begin());				
		}	
		// rep(i,SIZE(p))	printf("%d ", p[i]);
		// puts("");
		vector<int> A(n);
		rep(i,n)	A[i]=i;
		int res=0x3f3f3f3f;
		rep(mask, 1<<n) if(!(mask>>(n-1)&1)) {
			vector<int> B(n);
			int k=0;
			rep(i,n) if(mask>>i&1)	B[k++]=i;
			B[k++]=n-1;
			FORD(i,n-2,0) if(!(mask>>i&1))	B[k++]=i;
			// rep(i,n)	printf("%d ", B[i]);	puts("");			
			int rr = gao(B,p);
			res=min(res,rr);
		}
		printf("%d\n", res);
	}
	// vector<int> p={1,8,10,7,3};
	// DEBUG(check(p));
	return 0;
}