#include <bits/stdc++.h>
#ifdef ONLINE_JUDGE
	#define out(x)
#else
	#define out(x) cerr<<#x"="<<(x)<<endl
#endif
using namespace std;
typedef long long LL;
typedef vector<int> vi;
typedef pair<int, int> pii;
typedef vector<pii> vpii;
#define REP(i,n) for(int i=0; i<int(n); i++)
#define pb push_back
#define mp make_pair
#define X first
#define Y second
int a[1123];
int main(){
	int T;
	scanf("%d",&T);
	REP(tt,T){
		int n, ma=0, ans=1000;
		scanf("%d",&n);
		REP(i,n){
			scanf("%d",a+i);
			ma=max(ma,a[i]);
		}
		for(int t=1;t<=ma;++t){
			int tmp=0;
			REP(i,n)tmp+=(a[i]+t-1)/t-1;
			ans=min(ans,tmp+t);
		}
		printf("Case #%d: %d\n", tt+1, ans);
	}
}
