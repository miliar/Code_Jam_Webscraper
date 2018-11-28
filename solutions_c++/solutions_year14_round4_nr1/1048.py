#include <bits/stdc++.h>
#ifdef ONLINE_JUDGE
	#define out(x)
#else
	#define out(x) cerr<<#x"="<<(x)<<endl
#endif
using namespace std;
#define REP(i,n) for(int i=0; i<int(n); i++)
#define PB push_back
#define MP make_pair
#define X first
#define Y second
typedef long long LL;
typedef vector<int> vi;
typedef pair<int, int> pii;
typedef vector<pii> vpii;
int s[11234];
int main(){
	int T;
	scanf("%d", &T);
	REP(tt, T){
		int ans, d, n;
		scanf("%d%d",&n,&d);
		REP(i,n)scanf("%d",s+i);
		sort(s, s+n);
		ans=n;
		for(int l=0, r=n-1; l<r; ++l){
			while(l<r && s[l]+s[r]>d)--r;
			if(l<r){
				--ans;
				--r;
			}
		}
		printf("Case #%d: %d\n", tt+1, ans);
	}
}
