#include<bits/stdc++.h>
using namespace std;
#define ll long long
#define S(x) scanf("%lld", &x);
#define div /

ll dp[3000][3000];

ll check(ll p, ll q,ll t) {
//	cout << p << "  "<< t <<"\n";
	if(p  < 0 || q < 0) {
		return -1;
	}
	if(p == 1 && q == 1) {
//		cout <<"asd\n";
		return t;
	}
	if(p == 0 && q == 1) {
		return t;
	}
	if(dp[p][q] != -1) {
		return dp[p][q];
	}
	else {
		if(q % 2 == 0) {
			ll ma1 = check(p, q div 2, t + 1);
			ll ma2 = check(( p - (q div 2)) , q div 2, t + 1);
			if(ma2 >= 0) {
				dp[p][q] = t + 1; 
				return t + 1;
			}
			else {
				if(ma1 >= 0 && ma2 >= 0) {
					dp[p][q] = min(ma1 ,ma2);
					return min(ma1 ,ma2); 
				}
				else if(ma1 >= 0 && ma2 < 0) {
					dp[p][q] = ma1;
					return ma1; 
				}
				else {
					dp[p][q] = -1;
					return -1; 
				}
			}
			
		}
		else {
			return -1;
		}
		return -1;
	}
}


int main()
{
	freopen("inp.txt.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	ll t;
	S(t);
	ll tt;
	for(tt = 1;tt <= t;tt++) {
		ll p,q;
		string s;
		cin >> s;
		ll i = 0;
		memset(dp , -1, sizeof(dp));
		while(s[i] != '/') {
			i++;
		}
		p = 0;
		for(int j =0;j < i;j++) {
			p = p*10 + (s[j] - 48);
		}
		q = 0;
		for(int j =i + 1;j < s.length();j++) {
			q = q*10 + (s[j] - 48);
		}
//		cout << p << "qw  "<< q <<"\n";
		
		i = __gcd(p,q);
		p = p div i;
		q = q div i;
		if(check(p, q,0)>= 0) {
			printf("Case #%lld: %lld\n", tt, check(p,q,0));
		}
		else {
			printf("Case #%lld: impossible\n",tt);
		}
	}
}


