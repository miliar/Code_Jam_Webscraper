//satyaki3794
#include <bits/stdc++.h>
#include <iomanip>
#define ff first
#define ss second
#define pb push_back
#define MOD (1000000007LL)
#define LEFT(n) (2*(n))
#define RIGHT(n) (2*(n)+1)

using namespace std;
typedef long long ll;
typedef pair<ll, ll> ii;
typedef pair<int, ii> iii;

ll pwr(ll base, ll p, ll mod = MOD){
ll ans = 1;while(p){if(p&1)ans=(ans*base)%mod;base=(base*base)%mod;p/=2;}return ans;
}

ll gcd(ll a, ll b){
    if(b == 0)  return a;
    return gcd(b, a%b);
}


int n, s;
double x[1003], y[1004], z[1004], dist[1004][1002];
vector<int> adj[1004];
bool visited[1003];


void dfs(int v){

	visited[v] = true;
	for(auto vv : adj[v])
		if(!visited[vv])
			dfs(vv);
}


bool ok(double mid){

	for(int i=1;i<=n;i++){
		adj[i].clear();
		visited[i] = false;
	}
	for(int i=1;i<=n;i++)
		for(int j=1;j<=n;j++)
			if(i != j && dist[i][j] <= mid)
				adj[i].pb(j);

	dfs(1);
	return visited[2];
}


int main(){

	ios_base::sync_with_stdio(0);
	
	freopen("C-small-attempt0 (1).in", "r", stdin);
	freopen("output.txt", "w", stdout);

	int t, cases = 1;
	cin>>t;
// t=1;
	while(t--){

		cout<<"Case #"<<cases++<<": ";
		cin>>n>>s;
		for(int i=1;i<=n;i++){
			cin>>x[i]>>y[i]>>z[i];
			cin>>s>>s>>s;
		}
		for(int i=1;i<=n;i++)
			for(int j=1;j<=n;j++)
				dist[i][j] = sqrt((x[i]-x[j])*(x[i]-x[j])+(y[i]-y[j])*(y[i]-y[j])+(z[i]-z[j])*(z[i]-z[j]));

// cout<<ok(1000);

		double lo = 0, hi = 2000, ans = 2000;
		int iter = 100;
		while(iter--){

			double mid = (lo+hi)/2;
			if(ok(mid)){
				ans = min(ans, mid);
				hi = mid;
			}
			else
				lo = mid;
		}

		cout<<fixed<<setprecision(5)<<ans<<endl;
	}

    return 0;
}








