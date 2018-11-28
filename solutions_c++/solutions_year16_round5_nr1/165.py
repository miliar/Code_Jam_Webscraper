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


stack<char> st;

int main(){

	ios_base::sync_with_stdio(0);
	
	freopen("A-large.in", "r", stdin);
	freopen("output.txt", "w", stdout);

	int t, x = 1;
	cin>>t;
	while(t--){

		cout<<"Case #"<<x++<<": ";
		string str;
		cin>>str;
		while(!st.empty())
			st.pop();

		int n = str.length();

		int ans = 0;
		for(int i=0;i<n;i++)
			if(!st.empty() && st.top() == str[i]){
				ans += 10;
				st.pop();
			}
			else
				st.push(str[i]);

		ans += ((int)st.size()/2)*5;
		cout<<ans<<endl;
	}

    return 0;
}








