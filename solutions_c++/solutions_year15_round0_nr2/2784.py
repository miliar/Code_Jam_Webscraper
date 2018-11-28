#include<stdio.h>
#include<string>
#include<algorithm>
#include<iostream>
#include<vector>
#include<set>
#include<map>
#include<queue>
#include<list>
#include<memory.h>
#include<cassert>
#include<bitset>
#include<cmath>
using namespace std;

typedef long long ll;
typedef unsigned long long ull;
typedef vector<int> vi;
typedef vector<ll> vll;
typedef long double ld;
typedef pair<int, int> pii;
typedef pair<unsigned char, unsigned char> pcc;
typedef pair<ld, int> pdi;
typedef pair<ll, ll> pll;
typedef pair<pll, ll> pplll;
typedef pair<pii, int> ppiii;
typedef pair<int, pii> pipii;
typedef unsigned int uint;

#define mp make_pair

const int inf = 1e9+7;
const ll llinf = (ll)inf * inf;
const ld eps = 1e-6;
const int maxn = 11000;
const ld pi = acos(-1.0);

template<typename T>
T sqr(T x){
	return x * x;
}

int a[1100];

int main(){
#if 0
	freopen("kolmogorov.in", "r", stdin);
	freopen("kolmogorov.out", "w", stdout);
#endif
	
	int t;
	scanf("%d", &t);
	for(int T = 1; T <= t; T++){
		int n;
		scanf("%d", &n);
		
		for(int i = 0; i < n; i++){
			scanf("%d", &a[i]);
		}
		
		int ans = inf;
		for(int i = 1; i <= 1000; i++){
			int res = i;
			for(int j = 0; j < n; j++){
				res += (a[j] - 1) / i;
			}
			ans = min(ans, res);
		}
		
		printf("Case #%d: %d\n", T, ans);
	}
	
	return 0;
}
