#include <iostream>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <cstring>
#include <map>
#include <vector>
#include <string>
#include <queue>
#include <stack>
using namespace std;

#define S second
#define F first
#define mp make_pair
typedef pair<int, int> PII;
#define pb push_back
typedef long long ll;

ll power[15][20];
ll ans[15];

ll cal(ll x){
	for(ll i = 2; i*i <= x; ++i){
		if(x%i == 0) return i;
	}
	return -1;
}

void out(int x, int N){
	cout << 1;
	for(int i = N-3; i >= 0; --i){
		cout << (((1<<i)&x)!=0);
	}
	cout << 1;
	for(int i = 2; i <= 10; ++i) cout << ' ' << ans[i];
	puts("");
}

int main () {
	for(int i = 2; i <= 10; ++i) for(int j = 0; j < 17; ++j) {
		if(!j) power[i][j] = 1;
		else power[i][j] = power[i][j-1] * i;
	}
	int t, N, J;
	cin >> t;
	for(int tt = 1; tt <= t; ++tt){
		printf("Case #%d:\n", tt);
		int cnt = 0;
		cin >> N >> J;
		for(int i = 0; i < (1<<(N-2)) && cnt < J; ++i){
			memset(ans, -1, sizeof(ans));
			for(int j = 2; j <= 10; ++j){
				ll x = 1 + power[j][N-1];
				for(int k = 0; (1<<k)<= i; ++k) if((1<<k)&i){
					x += power[j][k+1];
				}
		//		cout << x << ' ' << j <<endl;
				ans[j] = cal(x);
				if(ans[j] == -1) break;
				if(j == 10){
					++cnt;
					out(i, N);
				}
			}
		}
	}
}