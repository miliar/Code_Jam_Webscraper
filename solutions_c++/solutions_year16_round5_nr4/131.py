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



set<string> good;


int main(){

	ios_base::sync_with_stdio(0);
	
	freopen("D-small-attempt2.in", "r", stdin);
	freopen("output.txt", "w", stdout);

	int t, cases = 1;
	cin>>t;
// t=1;
	while(t--){

		cout<<"Case #"<<cases++<<": ";
		int n, l;
		cin>>n>>l;

		good.clear();
		for(int i=0;i<n;i++){
			string s;
			cin>>s;
			good.insert(s);
		}

		string bad;
		cin>>bad;

// if(l <= 7 && n <= 10){
// 	cout<<endl<<n<<" "<<l<<endl;
// 	for(auto s : good)	cout<<s<<" ";
// 	cout<<endl<<bad<<endl<<endl;
// }

		if(good.find(bad) != good.end()){
			cout<<"IMPOSSIBLE\n";
			continue;
		}

		if(l == 1){
			cout<<"0 ?\n";
			continue;
		}

		int k = l-1;
		while(l--)
			cout<<"0?";
		cout<<" ";
		while(k--)
			cout<<"1";
		cout<<"\n";
	}

    return 0;
}








