// spnauT
//
#include <bits/stdc++.h>
using namespace std;
#define FOR(i,a,b) for(int _b=(b),i=(a); i<_b; ++i)
#define ROF(i,b,a) for(int _a=(a),i=(b); i>_a; --i)
#define REP(n) for(int _n=(n); --_n>=0;)
#define _1 first
#define _2 second
#define PB(x) push_back(x)
#define SZ(x) int((x).size())
#define MT(x) (x).empty()
#define ALL(x) (x).begin(), (x).end()
#define MSET(m,v) memset(m,v,sizeof(m))
#define MAX_PQ(T) priority_queue <T>
#define MIN_PQ(T) priority_queue <T,vector<T>,greater<T>>
#define IO() {ios_base::sync_with_stdio(0); cin.tie(0);}
#define nl '\n'
#define cint1(a) int a; cin>>a
#define cint2(a,b) int a,b; cin>>a>>b
#define cint3(a,b,c) int a,b,c; cin>>a>>b>>c
#define MP(a,b) make_pair((a),(b))
typedef long long LL;
typedef pair<int,int> PII;
typedef vector<int> VI; typedef vector<LL> VL; typedef vector<PII> VP;
template<class A, class B> inline bool mina(A &x, B y) {return(y<x)?(x=y,1):0;}
template<class A, class B> inline bool maxa(A &x, B y) {return(x<y)?(x=y,1):0;}
template<class A, class B> inline A geta(A &x, const B y) {A t=x;x=y;return t;}

#define MAXN (10005)

int main(int argc, char *argv[])
{
	cint1(t);
	int jj=0;
	while(t--) {
		jj++;
		char in[1005];
		char ans[1005];
		scanf("%s",in);
		int n = strlen(in);
		int l = 0;
		int r = n-1;
		for(int i=n-1;i>=0;i--) {
			int m=0;
			for(int j=0;j<i;j++) {
				if(in[j]>in[i]) {
					m=1;
					break;
				}
			}
			if(m) {
				ans[r]=in[i];
				r--;
			}
			else {
				ans[l]=in[i];
				l++;
			}
		}
		ans[n]=0;
		printf("Case #%d: %s\n",jj,ans);
	}
	return 0;
}
