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

void solve(){
	string x; cin >> x;
	int ret = 0;
	FOR(i, 1, x.length()){
		if (x[i] != x[i - 1]) ret++;
	}
	if (x[x.length() - 1] == '-') ret++;
	printf("%d\n", ret);
}

int main(){
	int t; scanf("%d", &t);
	FOE(i, 1, t){
		printf("Case #%d: ", i);
		solve();
	}
    return 0;
}
