#include <bits/stdc++.h>

#define ld long double
#define ll long long 
#define vi vector<int>
#define pii pair<int,int>
#define pll pair<long long ,long long >
#define vl vector<long long >
#define si set<int>
#define qi queue<int>
#define pll pair<long long ,long long >
#define mp make_paird

#define inf (1000000000+7)
#define pb push_back
#define sz size()
#define set(a,x) memset(a,x,sizeof(a))
#define all(a) a.begin(),a.end()
#define fr first
#define se second

using namespace std;

int main()  {
	ios::sync_with_stdio(false);
	cin.tie(0);
	
	int t;
	cin >> t;
	
	for(int tt = 1;tt <= t;tt++) {
		ll n;
		cin >> n;
		
		int cnt[11];
		set(cnt,0);
		int mul = 1,f = 0;
		for(int i=1;i <= 1e7;i++) {
			ll x = n*i;	
			while(x) {
				ll r = x % 10;
				if(!cnt[r]) f++;
				cnt[r]++;
				x /= 10;
			}
			if(f == 10) {
				mul=i;break;
			}
		}
		if(f) cout << "Case #" << tt << ": " << mul*n << "\n";
		else cout << "Case #" << tt << ": " << "INSOMNIA\n";
	}
	return 0;
}
