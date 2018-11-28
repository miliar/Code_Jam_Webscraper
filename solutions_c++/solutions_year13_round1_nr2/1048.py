#include <cstdio>
#include <cstring>
#include <algorithm>
#include <cmath>
#include <cstdlib>
#include <queue>
#include <map>
#include <vector>
#include <string>
#include <cctype>
#include <set>
#include <utility>
#include <stack>
#include <iostream>

using namespace std;

int t,k;
typedef long long ll;
typedef pair<int, int> pii;
const double eps = 1e-1;
ll e, r, n;
ll val[10005];
ll pts[10005];

void calc(bool frente, ll inicial, ll ini, ll fim){
	if(ini > fim) return;
	/*if(ini >= fim){
		if(ini == fim) pts[ini] = inicial;
		return;
	}*/
	ll maior = 0;
	ll ind = 0;
	for(int i = ini; i <= fim; ++i){
		if(val[i] > maior){
			maior = val[i];
			ind = i;
		}
	}
	if(frente){
		ll tot = inicial + (ind-ini)*r;
		if(tot <= e) pts[ind] = tot;
		else{
			pts[ind] = e;
			calc(false, inicial, ini, ind-1);
		}
		calc(true, r, ind+1, fim);
	}
	else{
		ll tot = min(e, inicial + (ind-ini)*r);
		ll prox = tot + (fim+1-ind)*r;
		if(prox>e){
			pts[ind] = min(e,prox-e);
			if(prox>(2*e))
				calc(false, r, ind+1, fim);
				
			tot = inicial + (ind-ini)*r;
			if(tot > e)
				calc(false, inicial, ini, ind-1);
		}
		
	}
}

int main (){
	#ifdef INTERNO
		freopen("in", "r", stdin);
		freopen("out", "w", stdout);
	#endif
	scanf("%d", &t);
	for(int _ = 1; _ <= t; ++_){
		
		scanf("%lld %lld %lld", &e, &r, &n);
		r = min(r,e);
		memset(pts, 0, sizeof pts);
		for(int i = 0; i < n; ++i) scanf("%lld", val+i);
		calc(true, e, 0, n-1);
		ll resp = 0;
		for(int i = 0; i < n; ++i) resp += pts[i]*val[i];
		printf("Case #%d: %lld\n", _, resp);
	}
	return 0;
}
