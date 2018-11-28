#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <queue>
#include <cmath>
#include <iostream>
#include <set>
#include <fstream>
#include <string>
#include <vector>
#include <bits/stdc++.h>

using namespace std;
#define FOR(i,s,e) for (int i=(s); i<(e); i++)
#define FOE(i,s,e) for (int i=(s); i<=(e); i++)
#define FOD(i,s,e) for (int i=(s); i>=(e); i--)
#define pb(x) push_back(x)
#define ppb() pop_back()
#define mp(x,y) make_pair(x,y)
#define LL long long
#define ULL unsigned long long
#define eps 1e-9
#define pi acos(-1.0)
LL max(LL a,LL b){if (a>b){return a;} else {return b;}}
LL min(LL a,LL b){if (a<b){return a;} else {return b;}}

int n;
int a[61][61];
int b[61][61], c[61][61];
int res;
int t[61];
int dp[51], dp2[51]; 

bool ck(){
	
	FOE(i, 1, n){
		int tx = 0;
		FOE(j, 1, n) tx += b[i][j] * (1 << (j - 1));
		FOE(k, 0, (1 << n) - 1) dp[k] = 0;
		dp[0] = 1;
		FOE(j, 1, n) if (i != j){
			FOR(k, 0, 1 << n) dp2[k] = 0;
			FOR(k, 0, 1 << n) if (dp[k]){
				dp2[k] = dp[k];
				FOE(p, 1, n) if (b[j][p] && !((1 << (p - 1)) & k)) dp2[k + (1 << (p - 1))] = 1;
			}
			FOR(k, 0, 1 << n) dp[k] = dp2[k];
		}
		FOR(k, 0, 1 << n){
			if (dp[k] && ((k & tx) == tx)) return false;
		}
	}
	return true;
}

void go(int cx, int cy, int co){
	if (cy > n){go(cx + 1, 1, co); return;}
	if (cx > n){
		if (ck()) {
			res = min(res, co);
		}
		return;
	}
	if (a[cx][cy]){
		b[cx][cy] = 1; go(cx, cy + 1, co);
	} else {
		b[cx][cy] = 0; go(cx, cy + 1, co);
		b[cx][cy] = 1; go(cx, cy + 1, co + 1);
	}
}

void solve(){
	scanf("%d", &n);
	FOE(i, 1, n){
		string x; cin >> x;
		FOE(j, 1, n) a[i][j] = (int)(x[j - 1] - '0');
	}

	res = n * n;
	go(1, 1, 0);
	printf("%d\n", res);
}

int main(){
	int t; scanf ("%d", &t);
	int tc = 0;
	while (t--){
		tc++;
		printf("Case #%d: ", tc);
		solve();
	}
    return 0;
}
