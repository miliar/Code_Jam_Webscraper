//Rupinder

#include<bits/stdc++.h>
#define debug 0
#define lld long long
#define FOR(i,a,b) for(i= a ; i <= b ; ++i)
#define rep(i,n) for(i= 0 ; i < n ; ++i)
#define repn(i,n) FOR(i,1,n)
#define all(x) x.begin(),x.end()
#define LET(x,a) __typeof(a) x(a)
#define IFOR(i,a,b) for(LET(i,a);i!=(b);++i)
#define EACH(it,v) IFOR(it,v.begin(),v.end())
#define pb push_back
#define sz size()
#define pii pair<int, int>
#define pll pair <lld ,lld>
#define mp make_pair
#define fill(x,v) memset(x,v,sizeof(x))
#define scan(v,n) vector<int> v(n);rep(i,n)cin>>v[i];
#define vi vector<int>
#define MOD 1000000007
#define ff first
#define ss second

using namespace std;
lld modpow(lld a,lld n,lld temp){lld res=1;while(n>0){if(n&1)res=(res*a)%temp;a=(a*a)%temp;n>>=1;}return res%temp;} 
vector<bool> h;
void hash(lld n) {
	if (n == 0)
		h[0] = 1;

	while (n > 0) {
		h[n%10] = 1;
		n /= 10;
	}
	return;
}

bool check() {
	for (int i = 0; i < 10; i++)
		if (h[i] == 0)
			return 0;
	return 1;
}

int main()
{
	ios_base::sync_with_stdio(false);
	int t;
	cin>>t;
	int T=t;
	while (t--) {
		lld n;
		cin>>n;
		lld N=0;
		bool pos = 0;
		h = vector<bool> (10, 0);
		for (int i = 0; i < 1e6; i++) {
			N += n;
			hash(N);
			if (check()) {
				pos = 1;
				break;
			}
		}
		cout<<"Case #"<<T-t<<": ";
		if (pos) {
			cout<<N<<"\n";
		} else {
			cout<<"INSOMNIA\n";
		}
	}

	if(debug)cerr << "Time elapsed: " << 1.0 * clock() / CLOCKS_PER_SEC << " s.\n";
	return 0;
}
