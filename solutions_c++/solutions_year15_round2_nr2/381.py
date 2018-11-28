#define _CRT_SECURE_NO_WARNINGS
#include<iostream>
#include<string>
#include<math.h>
#include<queue>
#include<stack>
#include<sstream>
#include<stdio.h>
#include<map>
#include<set>
#include<memory.h>
#include<algorithm>
#include<vector>
using namespace std;
typedef long long ll;
ll gcd(ll a, ll b){
	if (!b)
		return a;
	return gcd(b, a%b);
}
ll lcm(ll a, ll b){
	return b / gcd(a, b)*a;
}
#define FOR(I,N) for(int(i)=0;i<int(N);++i)
#define FORK(I,N,K) for(int(i)=0;i<int(N);i+=int(K))
int n, m, t;
ll c[5];
ll x;
ll calc1(bool h){
	memset(c, 0, sizeof(c));
	ll ret = 0;
	for (int i = 0; i < n; ++i){
		if (i % 2 == 0){
			c[0] += (m + 1) / 2;
			if (i == 0 || i == n - 1){
				if (m & 1)
					c[3 - h] += m / 2;
				else{
					c[3 - h] += max(m / 2 - 1, 0);
					++c[2 - h];
				}
			}
			else
				c[4 - h] += m / 2;
		}
		else{
			c[0] += m / 2;
			if (i == n - 1){
				int r = (m + 1) / 2;
				if (m & 1){
					c[2 - h] += 2;
					c[3 - h] += max(0, r - 2);
				}
				else{
					c[2 - h]++;
					c[3 - h] += max(r - 1, 0);
				}
			}
			else{
				int r = m / 2 + 1;
				if (m & 1){
					c[4 - h] += max(r - 2, 0);
					c[3 - h] += 2;
				}
				else{
					c[4 - h] += max(r - 1, 0);
					c[3 - h]++;
				}
			}
		}
	}
	ll rem = x;
	FOR(0, 5){
		ll q = min(rem, c[i]);
		ret += q * i;
		rem -= q;
	}
	return ret;
}
ll calc2(bool h){
	memset(c, 0, sizeof(c));
	ll ret = 0;
	for (int i = 0; i < n; ++i){
		if (i % 2 == 0){
			c[0] += m / 2;
			if (i == 0 || i == n - 1){
				int r = (m + 1) / 2;
				if (m & 1){
					c[2 - h] += 2;
					c[3 - h] += max(r - 2, 0);
				}
				else{
					c[2 - h]++;
					c[3 - h] += max(r - 1, 0);
				}
			}
			else{
				int r = (m + 1) / 2;
				if (m & 1){
					c[3 - h] += 2;
					c[4 - h] += max(r - 2, 0);
				}
				else{
					c[3 - h] += 1;
					c[4 - h] += max(r - 1, 0);
				}
			}
		}
		else{
			c[0] += (m + 1) / 2;
			if (i == n - 1){
				if (m & 1)
					c[3 - h] += m / 2;
				else{
					c[3 - h] += max(m / 2 - 1, 0);
					c[2 - h]++;
				}
			}
			else{
				if (m & 1)
					c[4 - h] += m / 2;
				else{
					c[4 - h] += max(m / 2 - 1, 0);
					c[3 - h]++;
				}
			}
		}
	}
	ll rem = x;
	FOR(0, 5){
		ll q = min(rem, c[i]);
		ret += q * i;
		rem -= q;
	}
	return ret;
}
/*int dp[16][1 << 16][16 * 16][2];
int vis[16][1 << 16][16 * 16][2], vs;
int calc(int i, int msk, int rem, bool l){
if (!rem)
return 0;

}*/
int main(){
	freopen("B-large.in", "r", stdin);
	freopen("Blarge.txt", "w", stdout);
	cin >> t;
	for (int k = 1; k <= t; ++k){
		cin >> n >> m >> x;
		if (n > m)
			swap(n, m);
		ll a1 = calc1(n == 1);
		ll a2 = calc2(n == 1);
		printf("Case #%d: %lld\n", k, min(a1, a2));
	}
}