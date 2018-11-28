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
		int s;
		scanf("%d ",&s);
		REP(i,s+1)a[i]=getchar()-'0';
		int ans=0, tot=0;
		REP(i,s+1){
			if(tot>=i){
				tot+=a[i];
			} else {
				ans+=i-tot;
				tot=i+a[i];
			}
		}
		printf("Case #%d: %d\n", tt+1, ans);
	}
}
