#include "iostream"
#include "cstdio"
#include "cstdlib"
#include "cstring"
#include "cmath"
#include "algorithm"
#include "set"
#include "map"
#include "queue"
#include "vector"
using namespace std;
#define rep(i,n) for(int i=0; i<(n); ++i)
#define repp(i,a,b) for(int i=a; i<a+b; ++i)
#define sz size()
#define X first
#define Y second
#define pb push_back
#define mp make_pair
typedef long long ll;
typedef pair<int,int> pii;
#define maxn 405

double a[maxn];
double dp[maxn], tmp[maxn];
int n,k;
void up(double p){
	// printf("%.2lf\n", p);
	tmp[0] = tmp[n+n+2] = 0;
	repp(i,1,n+n+1){
		tmp[i] = dp[i-1] * p + dp[i+1] * (1-p);
	}	
	repp(i,0,n+n+3) dp[i] = tmp[i];
	// rep(i,n+n) printf("%.1lf ", dp[i]); printf("\n");
}
void run(){
	cin >> n >> k;
	rep(i,n){
		cin >> a[i];
	}
	sort(a, a+n);
	double ans = 0;
	int lst = 0;
	rep(st, 1<<n){
		int cnt = 0;
		rep(j,n) cnt += (st>>j)&1;
		if(cnt==k){
			rep(i,n+n+3) dp[i] = 0; dp[n+1] = 1;
			rep(j,n) if((st>>j)&1) up(a[j]);
			if(dp[n+1] > ans){
				ans = dp[n+1];
				lst = st;
			}
			// printf("%d %.10lf\n", st, dp[n]);
		}
	}

	// int l,r;

	// rep(i,n+n+3) dp[i] = 0; dp[n+1] = 1;
	// up(a[0]); l = 1, r = n-1;
	// rep(kk,k-1){
	// 	if(dp[n+2] > dp[n]) up(a[l++]); else up(a[r--]);
	// }
	// if(dp[n+1] > ans) ans = dp[n+1];
	// // printf("%.10lf ", dp[n+1]);			

	// rep(i,n+n+3) dp[i] = 0; dp[n+1] = 1;
	// up(a[n-1]); l = 0, r = n-2;
	// rep(kk,k-1){
	// 	if(dp[n+2] > dp[n]) up(a[l++]); else up(a[r--]);
	// }
	// if(dp[n+1] > ans) ans = dp[n+1];
	// // printf("%.10lf ", dp[n+1]);			

	// rep(i,n+n+3) dp[i] = 0; dp[n+1] = 1;
	// l = 0;
	// rep(kk,k){
	// 	up(a[l++]);
	// }
	// if(dp[n+1] > ans) ans = dp[n+1];

	// rep(i,n+n+3) dp[i] = 0; dp[n+1] = 1;
	// r = n-1;
	// rep(kk,k){
	// 	up(a[r--]);
	// }
	// if(dp[n+1] > ans) ans = dp[n+1];

	printf("%.10lf\n", ans);			
	// if((lst>>(n-1))&1) printf("#");
	// if((lst>>0)&1) printf("*"); printf("\n");
	// rep(j,n) if((lst>>j)&1) printf(" %.2lf", a[j]); printf("\n");
	// rep(j,n) printf(" %.2lf", a[j]); printf("\n");

}
int main(int argc, char const *argv[])
{
	int cas;
	cin >> cas;
	rep(ca,cas){
		printf("Case #%d: ", ca+1);
		run();
	}
	return 0;
}