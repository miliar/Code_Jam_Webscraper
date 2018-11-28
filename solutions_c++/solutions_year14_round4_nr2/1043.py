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
int a[1123], s[1123];
int f[1123][1123];
int c[1123];
void takemin(int &x, int y){
    x=min(x, y);
}
int main(){
	int T;
	scanf("%d", &T);
	REP(tt, T){
		int n, ans;
		scanf("%d", &n);
		ans=n*(n-1)/2;
		REP(i,n)scanf("%d",a+i);
		vpii b;
		b.reserve(n);
		REP(i,n)b.PB(MP(a[i], i));
		sort(b.begin(), b.end());
		REP(i,n){
		    c[i]=0;
		    REP(j,n)if(b[j].X>b[i].X && b[j].Y<b[i].Y)
		        c[i]++;
		}
	    REP(i,n+1)REP(j,n+1)f[i][j]=n*n;
	    f[0][0]=0;
		for(int i=0; i<n; i++){
		    for(int j=0; j<=i; j++){
		        takemin(f[i+1][j+1], f[i][j]+c[i]);
		        takemin(f[i+1][j], f[i][j]+(n-i-c[i]-1));
		    }
		}
		REP(j,n+1)ans=min(ans, f[n][j]);
		printf("Case #%d: %d\n", tt+1, ans);
	}
}
