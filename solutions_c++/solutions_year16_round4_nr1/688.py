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

int r, p, s, m, t, n;
int ok = 0;

int v[60001], x[60001];
int res[60001];

int y[60001];

void ck(){
	FOE(i, 1, m) x[i] = v[i];
	FOE(i, 1, n){
		for (int j = 1; j <= m; j += (1 << (i))){
			int nt = j + (1 << (i - 1));
//			printf("%d %d %d %d\n", j, nt, v[j], v[nt]);
			if (x[nt] == x[j]) return;

			int w;
			if (x[nt] == x[j] - 1 || (x[j] == 1 && x[nt] == 3)) w = x[nt]; else w = x[j];
			x[j] = w;
		}
	}

	if (!ok) FOE(i, 1, m) res[i] = v[i]; 
	else {
		int ck = 0;
		FOE(j, 1, m){
			if (!ck && res[j] > v[j]) ck = 1;
			if (!ck && res[j] < v[j]) ck = -1;
		}
		if (1 == ck) FOE(j, 1, m) res[j] = v[j];
	}
	ok = 1;
}

void go(int a, int cp, int cs, int cr, int b){
	if (a == m){
		ck();
		return;
	}
	if (cp){
		v[a + 1] = 1; 
		go(a + 1, cp - 1, cs, cr, b);
	}
	if (cs){
		v[a + 1] = 2;
		go(a + 1, cp, cs - 1, cr, b);
	}
	if (cr){
		v[a + 1] = 3;
		go(a + 1, cp, cs, cr - 1, b);
	}
}

void solve(){
	cin >> n >> r >> p >> s;
	m = r + p + s;

	ok = 0;
	go(0, p, r, s, 0);

	if (!ok) puts("IMPOSSIBLE");
	else {
		FOE(i, 1, m){
			if (res[i] == 1) printf("P");
			else if (res[i] == 2) printf("R");
			else printf("S");
		}
		puts("");
	}

}

int main(){
	scanf("%d", &t);
	int tc = 0;
	while (t--){
		tc++;
		printf("Case #%d: ", tc);
		solve();
	}
    return 0;
}
