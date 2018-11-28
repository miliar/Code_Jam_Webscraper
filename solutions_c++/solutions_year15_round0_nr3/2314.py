#include <bits/stdc++.h>

using namespace std;
typedef long long LL;
typedef pair<int,int> pii;

#define forup(i,a,b) for(int i=(a); i<(b); ++i)
#define fordn(i,a,b) for(int i=(a); i>(b); --i)
#define rep(i,a) for(int i=0; i<(a); ++i)

#define gi(x) scanf("%d ",&x)
#define gl(x) scanf("%lld",&x)
#define gd(x) scanf("%lf",&x)
#define gs(x) scanf(" %s",x)

#define fs first
#define sc second

#define pb push_back
#define mp make_pair

const int inf=numeric_limits<int>::max();
const LL linf=numeric_limits<LL>::max();

const int max_n=10010;

int t,n,l,x;
string s;
int mat[5][5]={
	{0,0,0,0,0},
	{0,1,2,3,4},
	{0,2,-1,4,-3},
	{0,3,-4,-1,2},
	{0,4,3,-2,-1}
};
int a[max_n];
int pre[max_n];

int main() {
	gi(t);
	rep(z,t) {
		printf("Case #%d: ", z+1);
		gi(l); gi(x);
		cin>>s;
		n=l*x;
		rep(i,n) a[i]=(s[i%l]-'i')+2;
		int first_i=inf;
		pre[0]=1;
		rep(i,n) {
			pre[i+1]=mat[abs(pre[i])][a[i]]*(pre[i]/abs(pre[i]));
			if(first_i==inf and pre[i+1]==2) first_i=i+1;
		}
		int suf=1,last_k=-1;
		fordn(i,n-1,-1) {
			suf=mat[a[i]][abs(suf)]*(suf/abs(suf));
			if(suf==4 and pre[i]==4) {
				last_k=i;
				break;
			}
		}
		if(first_i<last_k) printf("YES\n");
		else printf("NO\n");
	}
	return 0;
}