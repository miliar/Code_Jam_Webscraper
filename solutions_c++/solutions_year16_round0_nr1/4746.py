#include <bits/stdc++.h>
 
using namespace std;
 
#define ll long long int
#define pb push_back
#define mp make_pair
#define INF (ll)(1e18)
#define inf 0x7fffffff
#define inff 100000
#define ff first
#define ss second
#define sz(x) ((int) (x).size())
#define fast cin.sync_with_stdio(0);cin.tie(0)
#define rep(i,N) for(int i = 0;i < N;i++)
#define frep(i,a,b) for(int i = a;i <= b;i++)
#define pii pair<int , int>
#define pll pair<ll , ll>
#define vii vector<int>
#define vpii vector< pii >
#define fill(A,v) memset(A,v,sizeof(A))
#define setbits(x) __builtin_popcount(x)
#define print(A,j,k) for(int ii=j;ii<=k;ii++)cout<<A[ii]<<" ";cout<<"\n"
#define all(x) (x).begin(), (x).end()
#define gcd __gcd
#define SQRT 350
#define CASES int t;cin>>t;while(t--)
#define FILE freopen("inp.txt" , "r" , stdin);
#define ld long double

const int N = 3e5 + 5;
const ll MOD = 1e9 + 7;
const ll INV2 = 500000004;

ll solve(ll n) {
	set<int> S;
	ll on = n;
	ll iter = 2;
	while (S.size() != 10) {
		ll x = n;
		while (x) {
			S.insert(x % 10);
			x /= 10;
		}
		if (S.size() == 10)
			return n;
		n = on * iter;
		iter++;
	}
	return n;
}

ll ans[] = {0,10,90,30,92,90,90,70,96,90,90,110,156,104,238,180,256,119,90,190,900,189,198,207,456,900,390,189,476,203,270,310,576,330,918,560,396,370,190,390,920,369,378,301,396,360,506,470,576,490,900,459,936,424,594,495,672,570,290,590,900,549,558,504,576,715,726,469,952,345,560,710,792,730,518,900,912,539,390,790,960,729,574,830,924,680,946,609,792,801,450,910,552,930,564,665,576,970,784,990,900};

int main(int argc, char const *argv[])
{
	fast;

	freopen("gcj_input.txt" , "r" , stdin);
	freopen("gcj_output.txt" , "w" , stdout);

	// frep(i , 1 , 1e6) {
	// 	cout << solve(i) << '\n';
	// }
	
	int t;
	cin >> t;
	for(int i = 0;i < t;i++) {
		ll n;
		cin >> n;
		cout << "Case #" << i + 1 << ": "; 
		if (n == 0)
			cout << "INSOMNIA\n";
		else
			cout << solve(n) << '\n';
	}

	return 0;
}
