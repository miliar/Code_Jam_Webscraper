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
char a[105];
void swap(int x,int y) {
	int l = 0;
	int r = y;
	while(l<r) {
		if(a[l]=='-' && a[r]=='-') { a[l]='+'; a[r]='+'; }
		else if(a[l]=='-' && a[r]=='+') { a[l]='-'; a[r]='+'; }
		else if(a[l]=='+' && a[r]=='-') { a[l]='+'; a[r]='-'; }
		else if(a[l]=='+' && a[r]=='+') { a[l]='-'; a[r]='-'; }
		l++;
		r--;
	}
	if(l==r) {
		if(a[l]=='-') a[l]='+';
		else a[l]='-';
	}
}
int main(int argc, char *argv[])
{
	int t;
	cin >> t;
	int i=1;
	while(t--) {
		scanf("%s",a);
		int n = strlen(a);
		int l = n-1;
		int ans = 0;
		while(1) {
			while(l>=0 && a[l]=='+') l--;
			if(l<0) break;
			ans++;
			if(a[0]=='+') {
				ans++;
				for(int i=0;a[i]=='+';i++) {
					a[i]='-';
				}
			}
			swap(0,l);
		}
		printf("Case #%d: %d\n",i,ans);
		i++;
	}
	return 0;
}
