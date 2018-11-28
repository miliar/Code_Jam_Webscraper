#include <bits/stdc++.h>
using namespace std;
typedef long long int ll;
typedef vector<int> vi;
typedef pair<int, int> ii;
typedef vector<ii> vii;
#define sc(x) scanf("%d", &x)
#define scl(x) scanf("%lld", &x)
#define loop(i,s,e) for(int i=s ; i<e ; i++)
#define rep(i,s,e) for(int i=s ; i>=e ; i--)
#define INF 1e6
#define MOD 1000000007  
#define f first
#define s second
#define EPS 1e-9
#define Rd freopen("in.txt", "r", stdin)
#define Wr freopen("out.txt", "w", stdout)
#define PS push_back
//#define DFS_WHITE -1
//#define DFS_BLACK 0

int main(){
	Rd;
	Wr;

	int T, n;
	ll arr[1010];
	sc(T);
	loop(t,0,T){
		ll mx = 0;
		ll ans1 = 0, ans2 = 0;
		printf("Case #%d: ", t+1);
		sc(n);
		loop(i,0,n) {
			scl(arr[i]);
			if(i > 0){
				ans1 += (arr[i-1] - arr[i] > 0 )? arr[i-1] - arr[i] : 0;
				mx = max(mx, arr[i-1] - arr[i]);
			}
		}
		loop(i,0,n-1){
			if(arr[i] <= mx){
				ans2 += arr[i];
			}
			else ans2 += mx;
		}
		printf("%lld %lld\n", ans1 , ans2);
	}	

	
	return 0;
}