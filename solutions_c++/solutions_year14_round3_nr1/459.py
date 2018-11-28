#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <cstring>
#include <cmath>
#include <vector>
#include <map>
#include <queue>
#include <stack>
#include <algorithm>

using namespace std;

typedef long long ll;
typedef unsigned long long ul;
typedef pair<int,int> ii;
typedef pair<ll,ll> pll;
typedef vector<ii> vii;

ul one = 1;

int t;
ll a,b,c,ans;
bool ok;

ll gcd(ll x, ll y){
	if (y == 0) return x;
	return gcd(y, x%y);
}

int main(){
	scanf("%d",&t);
	for (int jj=1; jj<=t; jj++){
		scanf("%lld/%lld",&a,&b);
		if (a > b){
			ans = 0;
		} else {
			ans = 0;
			c = gcd(a,b);
			a /= c;
			b /= c;
			while (a < b && b % 2 == 0){
				b /= 2;
				ans++;
			}
			ok = 0;
			while (a > b){
				a -= b;
				while (a < b && b % 2 == 0){
					b /= 2;
				}
			}
			if (a == b) ok = 1;
			else ans = 0;
		}
		printf("Case #%d: ",jj);
		if (ans == 0) printf("impossible\n");
		else printf("%lld\n",ans);
	}
	return 0;
}
