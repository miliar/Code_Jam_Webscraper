#include <bits/stdc++.h>

using namespace std;

#define rep(i, a, b) for(int i = (a); i < int(b); ++i)
#define rrep(i, a, b) for(int i = (a) - 1; i >= int(b); --i)
#define trav(it, v) for(typeof((v).begin()) it = (v).begin(); it != (v).end(); ++it)
#define all(v) (v).begin(), (v).end()
#define what_is(x) cerr << #x << " is " << x << endl;

typedef double fl;
typedef long long ll;
typedef pair<int, int> pii;
typedef vector<int> vi;
typedef vector<pii> vpi;

int sum[1005];
ll val[1005];
ll diff[1005];
ll l[1005], h[1005];

void solve(){
	int N,K;
	scanf("%d%d", &N, &K);
	int ans=0;
	rep(i,0,N-K+1){
		scanf("%d", sum+i);
		int S=0;
		rep(j,i,i+K-1){
			S += val[j];
		}
		val[i+K-1]=sum[i]-S;
	}
	rep(i,0,K){
		int Min=1000000000;
		int Max=-1000000000;
		for(int j=i; j < N; j += K){
			if(val[j] > Max)
				Max=val[j];
			if(val[j] < Min)
				Min=val[j];
		}
		ans=max(ans, Max-Min);
		diff[i]=Max-Min;
		l[i]=Min;
		h[i]=Max;
	}
	for(int lo=-15000000; lo <= 15000000; ++lo){
		int hi=lo+ans;
		ll Min=0, Max=0;
		rep(i,0,K){
			Min += lo-l[i];
			Max += hi-h[i];
		}
		if(Min <= 0 && Max >= 0){
			printf("%d\n", ans);
			return;
		}
	}
	printf("%d\n", ans+1);
	/*int ans=1000000000;
	rep(i,0,30000){
		int Max=0, Min=0;
		rep(j,0,N){
			if(val[j] > val[Max])
				Max=j;
			if(val[j] < val[Min])
				Min=j;
		}
		ans=min(ans, Max-Min);
		Max%=K;
		Min%=K;
		for(int j=Min; j < N; j += K)
			++val[j];
		for(int j=Max; j < N; j += K)
			--val[j];
	}
	printf("%d\n", ans);*/
}

int main(){
	int T;
	scanf("%d", &T);
	for(int t=1; t <= T; ++t){
		printf("Case #%d: ", t);
		solve();
	}
}
