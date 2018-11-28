
#include <iostream>
#include <cstdlib>
#include <cstring>
#include <cstdio>
#include <algorithm>
#include <cmath>
#include <vector>
#include <queue>
#define FOR(it,c) for ( __typeof((c).begin()) it=(c).begin(); it!=(c).end(); it++ )
#define INF 2000000000000LL
using namespace std;
typedef pair<int,int> PII;
typedef long long int LL;

int n;
LL b,t[40];

void input(){
	memset(t,0,sizeof(t));
	cin >> b >> n;
	for(int i=0;i<n;i++) cin >> t[i];
	n=37;
}

LL good(int a,LL c){
	LL ans=0;
	if( a==n && c>t[n-1] ) return INF;
	if( a<n  && c>=t[n-1] ) return INF;

	for(int i=0;i<n;i++){
		if(i<a && t[i]<c){
			ans += c-t[i];
		}
		else if(i>=a && t[i]<c+1){
			ans += c+1-t[i];
		}
	}
	return ans;
}

void solve(){
	sort(t,t+n);
	double ans = 0;
	for(int i=1; i<=n; i++){
		LL mn=0,mx=INF,md;
		while(mn<mx){
			md=(mn+mx+1)/2;
			if(good(i,md)<=b) mn=md;
			else mx=md-1;
		}
		//cout << i << ',' << mn << endl;
		double p = 0;
		for(int j=0; j<i; j++) if(mn>t[j]) p += mn-t[j];
		ans = max(ans, 36.0*p/i - good(i,mn));	
	}
	static int zi=0;
	printf("Case #%d: %.9f\n",++zi,ans);
}

int main(){
	int zn;
	scanf("%d",&zn);
	while(zn--){
		input();
		solve();
	}

	return 0;
}

