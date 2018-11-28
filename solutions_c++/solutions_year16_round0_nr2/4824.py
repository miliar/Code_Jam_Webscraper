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

string s;

void reverse(int l , int r) {
	for(int i = l,j=r;j > i;i++,j--)
		swap(s[i] , s[j]);
}

void flip(int l , int r) {
	for(int i = l;i <= r;i++)
		if (s[i] == '+')
			s[i] = '-';
		else
			s[i] = '+';
}

string form(string s) {
	string x = "";
	x.pb(s[0]);
	for(int i = 1;i < s.size();i++)
		if (s[i] != s[i - 1])
			x.pb(s[i]);
	return x;
}

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
	for(int tt = 0;tt < t;tt++) {
		cout << "Case #" << tt + 1 << ": "; 
		
		cin >> s;
		s = form(s);
		int n = s.size();	
		int ans = 0;
		int l = 0;
		for(int i = n - 1;i >= l;i--) {
			if (s[i] == '+')
				continue;
			else {
				if (s[l] == '-') {
					ans++;
					reverse(l , i);
					flip(l , i);
				}
				else {
					ans += 2;
					l++;
					// s.erase(s.begin());
					reverse(l , i - 1);
				}
			}
		}
		cout << ans << '\n';
	}

	return 0;
}
