/*
  Beautiful Codes are MUCH better than 'Shorter' ones !
user  : triveni
date  : 10/04/2016
time  : 01:39:48
*/
#include <bits/stdc++.h>

using namespace std;

#define      pii               std::pair<int,int>
#define      vi                std::vector<int>
#define      mp(a,b)           make_pair(a,b)
#define      pb(a)             push_back(a)
#define      each(it,s)        for(auto it = s.begin(); it != s.end(); ++it)
#define      rep(i, n)         for(int i = 0; i < (n); ++i)
#define      fill(a)           memset(a, 0, sizeof (a))
#define      sortA(v)          sort(v.begin(), v.end())
#define      sortD(v)          sort(v.begin(), v.end(), greater<auto>())
#define      X                 first
#define      Y                 second

typedef long long ll;

ll getDivisor(ll n) {
	for(ll i = 2; i * i <= n; ++i) if(n % i == 0) return i;
	return -1;
}

int main()
{
	int T;
	scanf("%d", &T);
	for (int tc = 1; tc <= T; ++tc) {
		printf("Case #%d:\n",tc);
		int n, J;
		scanf("%d %d", &n, &J);
		vector<pair<ll, vector<ll> > > fans;
		for(ll num = (1ll<<(n-1))+1; num < (1ll<<n); num+=2) {
			vector<ll> v;
			for(ll b = 2; b <= 10; ++b) {
				ll val = 0, mul = 1;
				for(int i = 0; i < n; ++i, mul = mul * b) if(num & (1<<i)) {
					val += mul;
				}
				ll d = getDivisor(val);
				// cerr << num << " " <<  b << " " << val << " " << d << "\n";
				if(d == -1) break;
				v.push_back(d);
			}
			if(v.size() == 9) {
				fans.push_back(make_pair(num, v));
			}
			if(fans.size() >= J) break;
		}
		for(auto& it : fans) {
			string num;
			vector<ll>& v = it.Y;
			for(int i = 0; i < n; ++i) if(it.X & (1<<i)) num += '1';
				else num += '0';
			reverse(num.begin(), num.end());
			cout << num << " ";
			for(int i = 0; i < 9; ++i){
				printf("%lld", v[i]);
				putchar(i==8?'\n':' ');
			}
		}
	}
	return 0;
}
